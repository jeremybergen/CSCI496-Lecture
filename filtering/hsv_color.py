import cv2
import numpy as np


def create_window() -> np.ndarray:
    # img = np.zeros((390, 640, 3), dtype=np.uint8)
    img = np.full((390, 640, 3), (0, 0, 255), dtype=np.uint8)
    # cv2.circle(img, (100, 100), 30, (255, 255, 255), 50)
    # img = cv2.medianBlur(img, 5)
    return img


img = create_window()


def display_image() -> None:
    # img2 = np.zeros((390, 640, 3), dtype=np.uint8)
    img2 = np.full((390, 640, 3), (0, 0, 255), dtype=np.uint8)
    # cv2.cvtColor(img, img2, cv2.COLOR_HSV2BGR)
    img2 = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    cv2.imshow('HSV Plot', img2)


def ontrackbar_changed(val) -> None:
    # img = np.full((390, 640, 3), (0, 0, 255), dtype=np.uint8)
    # hue_value = cv2.getTrackbarPos('Hue', "HSV Plot")

    # print(f"val: {val}")
    # hue_value = 0
    step = 1
    for i in range(5, 55):
        hue_range = 0
        for j in range(50, 408):
        # for j in range(50, 587):
            if hue_range >= 179:
                hue_value = 0
            step += 1
            if step == 3:
                hue_range += 1
                step = 1
            pix = np.zeros(3, np.uint8)
            # print(pix)
            pix[0] = hue_range
            pix[1] = 255
            pix[2] = 255

            img[i, j] = pix
    hue_value = cv2.getTrackbarPos('Hue', "HSV Plot")
    sat_value = cv2.getTrackbarPos('Saturation', "HSV Plot")
    val_value = cv2.getTrackbarPos('Value', "HSV Plot")

    sat_range = 0
    value_range = 255
    for i in range(75, 330):
        value_range -= 1
        sat_range = 0
        for j in range(10, 265):
            pix = np.zeros(3, np.uint8)
            pix[0] = hue_value
            sat_range += 1
            pix[1] = sat_range
            pix[2] = value_range
            img[i, j] = pix

    img[100:200, 300:400] = np.array((hue_value, sat_value, val_value), dtype=np.uint8)

    draw_marks(0, 0, 0, 0, 0)

    # cv2.imshow("test", img)
    # cv2.waitKey(0)

    display_image()
    # print(img[5:55, 50:587, :])
    # img2 = np.zeros((390, 640, 3), dtype=np.uint8)
    # # img2 = np.full((390, 640, 3), (0, 0, 255), dtype=np.uint8)
    # # cv2.cvtColor(img, img2, cv2.COLOR_HSV2BGR)
    # img2 = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    # cv2.imshow('HSV Plot', img2)
    # cv2.waitKey(0)

    # cv2.rectangle(create_window(), (0, 0), (640, 390), (0, 255, 0), 2)
    # for i in range()
    # cv2.rectangle(img, )


def draw_marks(event, x, y, flags, param) -> None:
    # img = np.full((390, 640, 3), (0, 0, 255), dtype=np.uint8)
    hue_value = cv2.getTrackbarPos('Hue', "HSV Plot")
    sat_value = cv2.getTrackbarPos('Saturation', "HSV Plot")
    val_value = cv2.getTrackbarPos('Value', "HSV Plot")

    #     for i in range(75, 330):
    #         value_range -= 1
    #         sat_range = 0
    #         for j in range(10, 265):
    #     for i in range(5, 55):
    #         hue_value = 0
    #         # for j in range(50, 408):
    #         for j in range(50, 587):

    if event == cv2.EVENT_LBUTTONDOWN:
        if 10 <= x <= 265 and 75 <= y <= 330:
            cv2.setTrackbarPos('Saturation', "HSV Plot", x - 10)
            cv2.setTrackbarPos('Value', "HSV Plot", 255-(y-75))
            cv2.circle(img, (x, y), 2, (0, 0, 255), 2)
            cv2.circle(img, ((hue_value*2)+50, 30), 2, (0, 0, 255), 2)
        elif 50 <= x <= 408 and 5 <= y <= 55:
            cv2.setTrackbarPos('Hue', "HSV Plot", (x - 50)//2)
            cv2.circle(img, (x, 30), 2, (0, 0, 255), 2)
            cv2.circle(img, ((sat_value+10), 255-(val_value - 75)), 2, (0, 0, 255), 2)
    else:
        cv2.circle(img, ((sat_value + 10), 255 - (val_value - 75)), 2, (0, 0, 255), 2)
        cv2.circle(img, ((hue_value * 2) + 50, 30), 2, (0, 0, 255), 2)


    display_image()
    #
    # img2 = np.zeros((390, 640, 3), dtype=np.uint8)
    # # img2 = np.full((390, 640, 3), (0, 0, 255), dtype=np.uint8)
    # # cv2.cvtColor(img, img2, cv2.COLOR_HSV2BGR)
    # img2 = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    # cv2.imshow('HSV Plot', img2)

    pass


def main() -> None:
    # img = create_window()
    window = "HSV Plot"

    cv2.namedWindow(window)

    cv2.createTrackbar("Hue", window, 90, 179, ontrackbar_changed)
    cv2.createTrackbar("Saturation", window, 128, 255, ontrackbar_changed)
    cv2.createTrackbar("Value", window, 128, 255, ontrackbar_changed)

    ontrackbar_changed(0)
    cv2.setMouseCallback(window, draw_marks)
    while True:
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    pass


if __name__ == '__main__':
    main()