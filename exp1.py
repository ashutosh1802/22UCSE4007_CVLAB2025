import cv2

def capture_image():
    # Open the webcam (0 is the default camera)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    # Capture a frame
    ret, frame = cap.read()
    
    # Release the webcam
    cap.release()
    
    if not ret:
        print("Error: Could not read frame.")
        return
    
    # Get image dimensions and calculate the number of pixels
    height, width, channels = frame.shape
    num_pixels = height * width
    print(f"Image Dimensions: {width}x{height}, Number of Pixels: {num_pixels}")
    
    # Save the image in both JPG and PNG format
    cv2.imwrite("captured_image.jpg", frame)
    cv2.imwrite("captured_image.png", frame)
    
    print("Image saved as 'captured_image.jpg' and 'captured_image.png'")
    
    # Display the image
    cv2.imshow("Captured Image", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Run the function
capture_image()
