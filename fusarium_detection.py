# Tan intensity evaluation for fusarium detection
# Kabir Hossain
import numpy as np
import cv2
from skimage import morphology
import matplotlib.pyplot as plt

from PIL import Image


def tan_intensity_fusarium(ImageFile):
    # Define lower bound for RGB values
    lower_bound = np.array([220, 220, 120], dtype=np.uint8)
    img = np.array(Image.open(ImageFile))
    # Mask to detect pixels with RGB values greater than the lower bound
    mask = cv2.inRange(img, lower_bound, np.array([255, 255, 255], dtype=np.uint8))

    # Perform morphological operations to merge neighboring contours
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(mask, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)

    # Find contours and hierarchy
    contours, _ = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contour_names = {}
    i = 0
    avgR = []
    avgG = []
    avgB = []

    # Filter out small contours inside larger ones and handle overlapping contours
    for contour in contours:
        contour_area = cv2.contourArea(contour)
        if contour_area > 50:
            x, y, w, h = cv2.boundingRect(contour)
            is_overlapping = False
            for name, (ex, ey, ew, eh) in contour_names.items():
                # Check if contours overlap based on area similarity
                overlap_area = min((x + w, ex + ew)) - max(x, ex)
                min_area = min(w * h, ew * eh)
                overlap_ratio = overlap_area / min_area
                if overlap_ratio > 0.5:  # Adjust overlap threshold as needed
                    is_overlapping = True
                    break
            if not is_overlapping:

                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                contour_names[i + 1] = (x, y, w, h)
                i += 1

    for name, (x, y, w, h) in contour_names.items():
        # Determine text position
        text_size, _ = cv2.getTextSize(str(name), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
        text_x = max(x + int((w - text_size[0]) / 2), 0)
        text_y = max(y - 10, text_size[1])
        # Draw contour names
        cv2.putText(img, str(name), (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the image with rectangles
    plt.imshow(img, cmap='gray')
    plt.show()


ImageFile = "test_image.jpg"

# Detect fusarium by a boundary box
tan_intensity_fusarium(ImageFile)


