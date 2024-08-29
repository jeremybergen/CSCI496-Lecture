import cv2
import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    # # img = cv2.imread('OpenCV_Logo.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('tyu.jpg', cv2.IMREAD_GRAYSCALE)
    img2 = np.copy(img)

    filter = np.zeros((9, 9))
    filter[5][0] = 1
    '''
    [0, 0, 0]
    [1, 0, 0]
    [0, 0, 0]
    '''

    cv2.filter2D(img, 0, filter, img2, borderType=cv2.BORDER_CONSTANT)

    #
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # mean_img = np.mean(img, axis=2)
    # mean_img = mean_img.astype(np.uint8)
    #
    # grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # print(f"Image size: {img.shape}")
    # img_slice = img[200:600, :]
    # img_swap = np.copy(img_slice)
    # # img_swap = img[600:200:-1, :]
    # img_swap = img_slice - 100
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # x = np.linspace(len(img[0]), 0, len(img[0]))
    # y = np.linspace(0, len(img), len(img))
    # X, Y = np.meshgrid(x, y)
    #
    # fig = plt.figure(dpi=len(img)/2)
    # ax = fig.add_subplot(111, projection='3d')
    # ax.plot_surface(X, Y, img, cmap='Greys', linewidth=1, antialiased=True, alpha=1, rstride=3, cstride=3)
    #
    # ax.set_xlabel('X')
    # ax.set_ylabel('Y')
    # ax.set_zlabel('Elevation')
    # ax.elev=74
    # ax.dist = 12
    # ax.azim = 140
    # fig.show()
    # plt.matshow(img)
    # plt.show()
    # fig.show()

    # cv2.imshow('image', img_swap)
    # cv2.waitKey(0)
    # print(img)
    cv2.imshow('image', img)
    cv2.imshow('image2', img2)
    # cv2.imshow('image', grey_img)
    cv2.waitKey(0)
    pass


if __name__ == '__main__':
    main()
