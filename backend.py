import cv2
import numpy as np
from PIL import Image

# Affine Transformation
def wrapaffine(image):
    rows, cols, ch = image.shape
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[50, 100], [200, 50], [150, 200]])
    points = cv2.getAffineTransform(pts1, pts2)
    img = cv2.warpAffine(image, points, (cols, rows))
    return Image.fromarray(img)

# Edge Detection
def edge_detetion(image):
    edges = cv2.Canny(image, 40, 80, L2gradient=True)
    return Image.fromarray(edges)

# Grayscale
def gray_scale(image):
    if len(image.shape) == 3 and image.shape[2] == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image
    return Image.fromarray(gray_image)

# Negative Transformation 
def neg_trans(image):
    neg_img = 255 - image  
    return Image.fromarray(neg_img)

# Gaussian Blur
def gaussian_blur(image):
    blur = cv2.GaussianBlur(image, (5, 5), cv2.BORDER_DEFAULT)
    return Image.fromarray(blur)

# Reduce Noise
def reduce_noise(image):
    noiseless = cv2.fastNlMeansDenoisingColored(image, None, 20, 20, 7, 21)
    return Image.fromarray(noiseless)

# Sharpening
def sharp_image(image):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    sharpened = cv2.filter2D(image, -1, kernel)
    return Image.fromarray(sharpened)
