import cv2 as cv
import numpy as np

def ft_load(path: str) -> np.ndarray:
    try:
        image = cv.imread(path)
        if image is None:
            raise ValueError("Error: can't read the image")
        print(f"The shape of image is: {image.shape}")
        image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        return image_rgb

    except Exception as e:
        print(str(e))
        return None