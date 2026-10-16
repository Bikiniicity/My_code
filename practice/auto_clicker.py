import sys
import time
import cv2
import keyboard
import numpy as np
import pyautogui

# DPI 설정 보정
try:
    import ctypes

    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    pass

# ==========================================
# 🎯 [사용자 설정 영역]
# ==========================================
NORTH_WEST_X, NORTH_WEST_Y = 251, 358  # 탐색 구역 좌상단
SOUTH_EAST_X, SOUTH_EAST_Y = 704, 601  # 탐색 구역 우하단

TARGET_COLOR = "0x83B372"  # 찾으려는 좌석 HEX 색상 코드
TOLERANCE = 32.0  # 색상 감지 오차 범위
SEAT_COUNT = 2  # 🔢 기본 찾을 연석 수 (1, 2, 3...)

is_running = False


def hex_to_rgb(hex_input):
    cleaned = str(hex_input).strip().lstrip("#").replace("0x", "")
    if len(cleaned) != 6:
        cleaned = "83B372"
    return tuple(int(cleaned[i : i + 2], 16) for i in (0, 2, 4))


def find_and_move_mouse():
    global is_running
    target_rgb = hex_to_rgb(TARGET_COLOR)
    width = SOUTH_EAST_X - NORTH_WEST_X
    height = SOUTH_EAST_Y - NORTH_WEST_Y

    if width <= 0 or height <= 0:
        return

    # 1. 화면 캡처
    screenshot = pyautogui.screenshot(
        region=(NORTH_WEST_X, NORTH_WEST_Y, width, height)
    )
    img_np = np.array(screenshot)

    # 2. 색상 범위 마스크
    diff = img_np.astype(int) - np.array(target_rgb)
    distances = np.sqrt(np.sum(diff**2, axis=2))
    mask = (distances <= TOLERANCE).astype(np.uint8) * 255

    # 3. 개별 좌석(윤곽선) 감지
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    detected_seats = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if 3 <= w <= 25 and 3 <= h <= 25:
            cx = x + w // 2
            cy = y + h // 2
            detected_seats.append({"y": cy, "x": cx, "w": w, "h": h})

    if not detected_seats:
        return

    # 4. 좌석들을 Y 좌표 기준으로 '같은 가로 행(줄)' 단위 그룹화
    ROW_THRESHOLD = 7  # 같은 줄로 볼 Y축 오차 범위(px)
    detected_seats.sort(key=lambda s: s["y"])

    rows = []
    for seat in detected_seats:
        added = False
        for row in rows:
            avg_y = sum(s["y"] for s in row) / len(row)
            if abs(seat["y"] - avg_y) <= ROW_THRESHOLD:
                row.append(seat)
                added = True
                break
        if not added:
            rows.append([seat])

    # 5. 각 행 내부에서 C구역(화면 중앙 X좌표)과 가까운 순서대로 후보 정렬
    center_x_pixel = width // 2  # 탐색 영역의 가로 중앙값 (C구역 중심)

    target_seat = None

    for row in rows:
        # 각 행의 좌석을 X 오름차순으로 정리 (연석 판단용)
        row.sort(key=lambda s: s["x"])

        if len(row) < SEAT_COUNT:
            continue

        candidate_groups = []

        # 해당 행에서 가능한 연석 묶음들을 모두 수집
        for i in range(len(row) - SEAT_COUNT + 1):
            group = [row[i]]
            for j in range(i + 1, len(row)):
                prev = group[-1]
                curr = row[j]
                if 0 < (curr["x"] - prev["x"]) <= (prev["w"] * 2.2):
                    group.append(curr)
                    if len(group) == SEAT_COUNT:
                        break
                else:
                    break

            if len(group) == SEAT_COUNT:
                # 연석 묶음의 중간 X좌표와 중앙(C구역) 간 거리 계산
                group_center_x = (group[0]["x"] + group[-1]["x"]) / 2
                dist_from_center = abs(group_center_x - center_x_pixel)
                candidate_groups.append((dist_from_center, group[0]))

        # C구역(중앙)에 가장 가까운 연석을 우선 선택
        if candidate_groups:
            candidate_groups.sort(key=lambda item: item[0])
            target_seat = candidate_groups[0][1]
            break

    # 만약 연석을 찾지 못하면 가장 앞줄에서 중앙과 가장 가까운 단일 좌석 지정
    if not target_seat and rows and rows[0]:
        rows[0].sort(key=lambda s: abs(s["x"] - center_x_pixel))
        target_seat = rows[0][0]

    # 6. 마우스 커서 이동 및 대기
    if target_seat:
        abs_x = NORTH_WEST_X + target_seat["x"]
        abs_y = NORTH_WEST_Y + target_seat["y"]

        pyautogui.moveTo(abs_x, abs_y)
        is_running = False
        print(f"🎯 [C구역/중앙 우선 {SEAT_COUNT}연석 포착] 위치: ({abs_x}, {abs_y}) -> 수동 클릭하세요!")


def start_automation():
    global is_running
    if not is_running:
        is_running = True
        print(f"\n▶ [C구역 우선 탐색 시작 - {SEAT_COUNT}연석 찾는 중...]")


def stop_automation():
    global is_running
    if is_running:
        is_running = False
        print("\n⏸ [일시정지]")


def set_seat_count(count):
    global SEAT_COUNT
    SEAT_COUNT = count
    print(f"\n⚙️ [연석 설정 변경] -> {SEAT_COUNT}연석")


def exit_program():
    print("\n👋 프로그램 종료")
    sys.exit(0)


if __name__ == "__main__":
    pyautogui.FAILSAFE = True

    # 🎯 단축키 (A: 시작 | S: 일시정지)
    keyboard.add_hotkey("a", start_automation)
    keyboard.add_hotkey("s", stop_automation)

    # 🔢 연석 수 실시간 변경 (숫자키 1, 2, 3, 4)
    keyboard.add_hotkey("1", lambda: set_seat_count(1))
    keyboard.add_hotkey("2", lambda: set_seat_count(2))
    keyboard.add_hotkey("3", lambda: set_seat_count(3))
    keyboard.add_hotkey("4", lambda: set_seat_count(4))

    keyboard.add_hotkey("esc", exit_program)

    print("=" * 60)
    print(" 🎯 STAGE C구역(중앙) 우선 탐색 보조 프로그램")
    print("=" * 60)
    print(" • 탐색 우선순위: 최상단 앞줄 ➔ C구역(중앙) ➔ 연석 자리")
    print(" • 동작 방식: A 키 누름 -> C구역 연석으로 커서 이동 -> 대기")
    print("=" * 60)
    print(" [조작키] 탐색: A | 정지: S | 연석 변경: 1, 2, 3, 4 | 종료: Esc\n")

    try:
        while True:
            if is_running:
                find_and_move_mouse()
                time.sleep(0.05)
            else:
                time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n프로그램이 종료되었습니다.")