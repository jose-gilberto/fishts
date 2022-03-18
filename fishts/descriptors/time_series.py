import numpy as np
import cv2
import math


def extract_ts_descriptor(
    image: np.ndarray,
    start_angle: int,
    end_angle: int,
    step: float
):
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    reference = np.zeros_like(image)
    # TODO: select the biggest contour only
    cv2.drawContours(reference, [contours[0]], 0, 255, 2)

    # Calculate the center of mass
    M = cv2.moments(reference)
    centroid_x = int(M['m10']/M['m00'])
    centroid_y = int(M['m01']/M['m00'])

    height, width = image.shape

    distances = []
    for i in np.arange(start_angle, end_angle, step):
        tmp = np.zeros_like(image)
        thickness = 1

        radius = max(tmp.shape)
        theta = np.deg2rad(i)

        out_coord = (
            int(centroid_x + np.cos(theta) * radius),
            int(centroid_y - np.sin(theta) * radius)
        )
        # Handle diferent line gaps
        cv2.line(tmp, (centroid_x, centroid_y), out_coord, 255, thickness)
        
        (row, col) = np.nonzero(np.logical_and(tmp, reference))

        while (len(row) == 0 or len(col) == 0):
            tmp = np.zeros_like(image)
            thickness += 1
            cv2.line(tmp, (centroid_x, centroid_y), out_coord, 255, thickness)
            (row, col) = np.nonzero(np.logical_and(tmp, reference))

        distance = math.sqrt(
            (col[0] - centroid_x)**2 + (row[0] - centroid_y)**2
        )

        distances.append(distance)

    return np.array(distances)
