import cv2


def shrink(image, factor):
    h, w = image.shape[:2]
    return cv2.resize(image, (w // factor, h // factor), interpolation=cv2.INTER_AREA)


cv2.imwrite(
    "data/rgb_align/sobel01.jpg", shrink(cv2.imread("data/rgb_align/sobel1.jpg"), 2)
)
