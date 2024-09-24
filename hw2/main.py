import cv2
import numpy as np


def sign_lines(img_edges) -> np.ndarray:
    lines = cv2.HoughLinesP(img_edges, 
                           rho=1, 
                           theta=np.pi/180, 
                           threshold=35, 
                           minLineLength=5, 
                           maxLineGap=5)
    if lines is not None:
        return lines
    return None


def sign_line_axis(lines, sign=None):
    xaxis = np.empty(0, dtype=np.int32)
    yaxis = np.empty(0, dtype=np.int32)
    # print(lines[0][0][0])
    for line in lines:
        for x0, y0, x1, y1 in line:
            if sign == "Green":
                pass
                # Do stuff for green sign
            elif sign == "Stop":
                pass
                #do stuff for stop sign


            xaxis = np.append(xaxis, x0)
            xaxis = np.append(xaxis, x1)
            yaxis = np.append(yaxis, y0)
            yaxis = np.append(yaxis, y1)

    return xaxis, yaxis


def main() -> None:
    green_sign = cv2.imread("green_box.jpg")
    blank_img = np.zeros(green_sign.shape)
    green_sign_hsv = cv2.cvtColor(green_sign, cv2.COLOR_BGR2HSV)
    # print(green_sign_hsv[50:60, 50:60])
    color_low = np.array([52, 250, 165])
    color_high = np.array([56, 255, 175])
    mask = cv2.inRange(green_sign_hsv, color_low, color_high)
    edges = cv2.Canny(mask, 100, 200)

    lines = sign_lines(edges)
    if lines is None:
        return None
    
    xaxis, yaxis = sign_line_axis(lines, sign="Green")

    xmin = xaxis.min()
    xmax = xaxis.max()
    ymin = yaxis.min()
    ymax = yaxis.max()
    print(f"{xmin} {xmax} {ymin} {ymax}")

    cv2.circle(green_sign, (((xmax - xmin)//2)+xmin, ((ymax - ymin)//2)+ymin), int(2), (0, 0, 255), 2)

    # xmin = lines.min()
    # xmax = lines.max()
    for line in lines:
        x0, y0, x1, y1 = line[0]
        cv2.line(blank_img, (x0, y0), (x1, y1), (0, 0, 255), 2, cv2.LINE_AA)


    cv2.imshow("green_box", green_sign)
    cv2.waitKey(0)
    pass


if __name__ == "__main__":
    main()
