from typing import Any, List
import numpy as np
import cv2
from .base import BaseTransformer


class Resize(BaseTransformer):
    def __init__(self, proportion_scale: bool, g_measure: int) -> None:
        super().__init__()
        self.proportion_scale = proportion_scale
        self.g_measure = g_measure

    def __call__(self, image: np.ndarray) -> Any:
        y, x = image.shape
        if self.proportion_scale:
            if x < y:
                y_i = self.g_measure
                x_i = (self.g_measure * x) / y
                return cv2.resize(image, dsize=(int(x_i), int(y_i)))
            elif x > y:
                x_i = self.g_measure
                y_i = (self.g_measure * y) / x
                return cv2.resize(image, dsize=(int(x_i), int(y_i)))
        return cv2.resize(image, dsize=(int(self.g_measure), int(self.g_measure)))


class ConvertColor(BaseTransformer):
    def __init__(self, conversion_code) -> None:
        super().__init__()
        self.conversion_code = conversion_code

    def __call__(self, image: np.ndarray) -> Any:
        return cv2.cvtColor(image, self.conversion_code)


class GaussianBlur(BaseTransformer):
    def __init__(self, kernel_size: List[int], sigma_x: int) -> None:
        self.ksize = kernel_size
        self.sigma_x = sigma_x

    def __call__(self, image: np.ndarray):
        return cv2.GaussianBlur(image, self.ksize, self.sigma_x)


class CannyEdge(BaseTransformer):
    def __init__(self, threshold_1, threshold_2) -> None:
        self.t1 = threshold_1
        self.t2 = threshold_2

    def __call__(self, image: np.ndarray):
        return cv2.Canny(image, self.t1, self.t2)


class Dilate(BaseTransformer):
    def __init__(self, kernel, iterations) -> None:
        self.kernel = kernel
        self.iterations = iterations

    def __call__(self, image: np.ndarray):
        return cv2.dilate(image, self.kernel, iterations=self.iterations)


class Erode(BaseTransformer):
    def __init__(self, kernel, iterations) -> None:
        self.kernel = kernel
        self.iterations = iterations

    def __call__(self, image: np.ndarray):
        return cv2.erode(image, self.kernel, self.iterations)



class Threshold(BaseTransformer):
    def __init__(self, t, p, code) -> None:
        super().__init__()
        self.t = t
        self.p = p
        self.code = code

    def __call__(self, image: np.ndarray):
        return cv2.threshold(image, self.t, self.p, self.code)[1]
