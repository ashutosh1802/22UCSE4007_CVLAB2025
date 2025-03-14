import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(image, title):
    plt.hist(image.ravel(), bins=256, range=[0, 256], color='black', alpha=0.7)
    plt.title(title)
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")

def histogram_equalization(image_path):
    # Read the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: Could not open image.")
        return
    
    # Perform histogram equalization
    equalized_image = cv2.equalizeHist(image)
    
    # Plot histograms
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title("Original Image")
    plt.axis("off")
    
    plt.subplot(2, 2, 2)
    plt.imshow(equalized_image, cmap='gray')
    plt.title("Equalized Image")
    plt.axis("off")
    
    plt.subplot(2, 2, 3)
    plot_histogram(image, "Histogram (Before Equalization)")
    
    plt.subplot(2, 2, 4)
    plot_histogram(equalized_image, "Histogram (After Equalization)")
    
    plt.tight_layout()
    plt.show()
    
    # Save the results
    cv2.imwrite("equalized_image.jpg", equalized_image)
    print("Equalized image saved as 'equalized_image.jpg'")

# Example usage
histogram_equalization("input.jpg")
