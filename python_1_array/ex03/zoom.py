import load_image
import cv2 as cv

if __name__ == "__main__":
    img = load_image.ft_load("animal.jpeg")
    print(img)
    # grey_img_zoomed = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    grey_img_zoomed = cv.cvtColor(img, cv.COLOR_RGB2GRAY)[100:500, 455:855]
    print(f"New shape after slicing: {grey_img_zoomed.shape}")
    print(grey_img_zoomed)
    cv.imshow("animal", grey_img_zoomed)
    cv.waitKey(0)
    cv.destroyAllWindows()
    # zoomed = img[]