import cv2
import numpy as np

def load_image(filename):
    image = cv2.imread(filename)
    if image is None:
        print("Error: Could not open image.")
        return None
    return image

def scale_image(image, scale_x, scale_y):
    height, width, channels = image.shape
    new_height, new_width = int(height * scale_y), int(width * scale_x)
    scaled_image = np.zeros((new_height, new_width, channels), dtype=np.uint8)
    
    for i in range(new_height):
        for j in range(new_width):
            orig_x, orig_y = int(j / scale_x), int(i / scale_y)
            scaled_image[i, j] = image[orig_y, orig_x]
    
    return scaled_image

def rotate_image(image, angle):
    height, width, channels = image.shape
    rotated_image = np.zeros((width, height, channels), dtype=np.uint8)
    
    for i in range(height):
        for j in range(width):
            new_x = j
            new_y = height - 1 - i
            rotated_image[new_x, new_y] = image[i, j]
    
    return rotated_image if angle == 90 else image

def flip_image(image, mode):
    height, width, channels = image.shape
    flipped_image = np.zeros_like(image)
    
    if mode == 'horizontal':
        for i in range(height):
            for j in range(width):
                flipped_image[i, width - 1 - j] = image[i, j]
    elif mode == 'vertical':
        for i in range(height):
            for j in range(width):
                flipped_image[height - 1 - i, j] = image[i, j]
    
    return flipped_image

# Load image
image = load_image("input.jpg")
if image is not None:
    # Perform transformations
    scaled = scale_image(image, 0.5, 0.5)
    rotated = rotate_image(image, 90)
    flipped = flip_image(image, 'horizontal')
    
    # Show images
    cv2.imshow("Original", image)
    cv2.imshow("Scaled", scaled)
    cv2.imshow("Rotated", rotated)
    cv2.imshow("Flipped", flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
