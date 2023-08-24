import cv2
import numpy as np

def adaptive_median_filter(image, max_window_size):
    result = np.copy(image)
    height, width = image.shape

    for y in range(height):
        for x in range(width):
            window_size = 3
            while True:
                offset = window_size // 2
                neighbors = image[
                    max(y - offset, 0): min(y + offset + 1, height),
                    max(x - offset, 0): min(x + offset + 1, width)
                ]
                median = np.median(neighbors)
                pixel_value = image[y, x]

                if median > np.min(neighbors) or  median< np.max(neighbors):
                    if  pixel_value<= np.min(neighbors) or pixel_value >= np.max(neighbors):
                        result[y, x] = median
                    break
                else:
                    window_size += 2
                    if(window_size>max_window_size):
                        result[y, x] = median
                        

    return result

image = cv2.imread('d:\Fig0510(a)(ckt-board-saltpep-prob.pt05).tif', cv2.IMREAD_GRAYSCALE)


filtered_image = adaptive_median_filter(image, max_window_size=7)



cv2.imshow('Filtered Image', filtered_image)
filtered_image_2 = cv2.medianBlur(image, ksize=3)
cv2.imshow('med Image', filtered_image_2)

cv2.imshow('diff Image', cv2.absdiff(filtered_image_2, filtered_image))

cv2.waitKey(0)
cv2.destroyAllWindows()

