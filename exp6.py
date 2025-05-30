import cv2
import numpy as np

def edge_detection_medical_image(image_path, output_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: Could not open image.")
        return

    # Apply Canny edge detection
    edges = cv2.Canny(image, threshold1=50, threshold2=150)
    
    # Save and display the result
    cv2.imwrite(output_path, edges)
    print(f"Edge-detected image saved as '{output_path}'")
    return edges

# Example usage
edge_detection_medical_image("MRI_of_Human_Brain.jpg", "edges.jpg")
