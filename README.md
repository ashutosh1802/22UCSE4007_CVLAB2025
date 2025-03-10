# Laboratory Experiments

## Overview
This repository contains a collection of image processing experiments implemented using OpenCV/Scikit-Image in Python. These experiments cover fundamental image processing techniques, including capturing images, performing transformations, applying filters, and working on real-world tasks like object recognition.

## Experiments

### 1. Capture Image from Webcam
- Open the webcam and capture an image.
- Print the number of pixels in the image.
- Save the image in both JPG and PNG formats.

### 2. Image Transformations (Without Library Functions)
- Open a JPG image and manually perform:
  - Scaling
  - Rotation
  - Flipping

### 3. GUI for Image Adjustments
- Build a GUI to adjust the following webcam image parameters using library functions:
  - Contrast
  - Brightness
  - Sharpness
  - Hue
  - Saturation

### 4. High Pass & Low Pass Filtering
- Perform High Pass & Low Pass Filtering operations in the Fourier Domain on a JPG image and save the results.

### 5. Histogram Equalization
- Draw a histogram of an input image before and after performing histogram equalization.

### 6. Edge Detection on Medical Images
- Open a medical image file (MRI/CT/PET scan) and perform edge detection.

### 7. Shape Detection
- Identify basic shapes (e.g., circle, line, square, rectangle) in an input image.

### 8. Image Watermarking and Inpainting
- Add a watermark to an image.
- Remove the watermark using inpainting.

### 9. **Mini Project 1**: Text Image Segmentation
- Take an image of printed text (e.g., from a book).
- Extract individual characters as separate images.
- Save each row of the input text image in separately numbered folders.

### 10. **Mini Project 2**: Object Recognition
- Use an inbuilt feature extractor for a real-world object recognition task (e.g., face recognition).
- Implement an ML classifier for the task.

## Requirements
- Python 3.x / C++
- OpenCV
- Scikit-Image
- NumPy

## Installation
```bash
pip install opencv-python numpy scikit-image
```

## How to Run
Each experiment is implemented as a separate script. To run an experiment, execute:
For example, to run the first experiment:
```bash
python exp1.py
```

## Contributors
Feel free to contribute by adding improvements, fixes, or new experiments!
