import numpy as np
import cv2
import matplotlib.pyplot as plt

def apply_filter(image_path, cutoff, filter_type="low"):
    # Load image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Get image dimensions
    rows, cols = img.shape
    crow, ccol = rows // 2 , cols // 2  # Center of the image

    # Perform Fourier Transform
    dft = np.fft.fft2(img)
    dft_shift = np.fft.fftshift(dft)

    # Create a mask
    mask = np.zeros((rows, cols), np.uint8)

    if filter_type == "low":
        # Low Pass Filter: Set center circle to 1
        mask[crow-cutoff:crow+cutoff, ccol-cutoff:ccol+cutoff] = 1
    elif filter_type == "high":
        # High Pass Filter: Set center circle to 0, rest to 1
        mask = np.ones((rows, cols), np.uint8)
        mask[crow-cutoff:crow+cutoff, ccol-cutoff:ccol+cutoff] = 0

    # Apply mask and inverse transform
    dft_filtered = dft_shift * mask
    dft_inverse = np.fft.ifftshift(dft_filtered)
    img_filtered = np.fft.ifft2(dft_inverse)
    img_filtered = np.abs(img_filtered)

    # Save output images
    output_filename = f"filtered_{filter_type}.jpg"
    cv2.imwrite(output_filename, img_filtered)
    
    return img, mask * 255, img_filtered

# Apply Low Pass Filter
original, mask_lpf, result_lpf = apply_filter("input.jpg", cutoff=30, filter_type="low")

# Apply High Pass Filter
original, mask_hpf, result_hpf = apply_filter("input.jpg", cutoff=30, filter_type="high")

# Display Results
fig, axs = plt.subplots(3, 3, figsize=(12, 10))

# Low Pass Filtering
axs[0, 0].imshow(original, cmap="gray")
axs[0, 0].set_title("Original Image")
axs[0, 1].imshow(mask_lpf, cmap="gray")
axs[0, 1].set_title("Low Pass Filter Mask")
axs[0, 2].imshow(result_lpf, cmap="gray")
axs[0, 2].set_title("Low Pass Filtered Image")

# High Pass Filtering
axs[1, 0].imshow(original, cmap="gray")
axs[1, 0].set_title("Original Image")
axs[1, 1].imshow(mask_hpf, cmap="gray")
axs[1, 1].set_title("High Pass Filter Mask")
axs[1, 2].imshow(result_hpf, cmap="gray")
axs[1, 2].set_title("High Pass Filtered Image")

for ax in axs.flat:
    ax.axis("off")

plt.tight_layout()
plt.show()
