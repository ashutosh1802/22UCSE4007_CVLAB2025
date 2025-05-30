from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np

# Step 1: Add a watermark to the image
def add_watermark(input_image_path, output_image_path, watermark_text):
    # Load the image
    image = Image.open(input_image_path)

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Define the watermark text and font
    font = ImageFont.truetype("arial.ttf", 50)  # Use a system font or provide a path to a .ttf file

    # Add the watermark
    draw.text((10, 10), watermark_text, fill=(255, 255, 255, 128), font=font)  # (x, y) position, RGBA color

    # Save the watermarked image
    image.save(output_image_path)
    print(f"Watermarked image saved to {output_image_path}")

# Step 2: Remove the watermark using inpainting
def remove_watermark(input_image_path, output_image_path):
    # Load the watermarked image
    image = cv2.imread(input_image_path)

    # Create a mask where the watermark is located
    mask = np.zeros(image.shape[:2], dtype=np.uint8)  # Create a black mask
    cv2.rectangle(mask, (10, 10), (300, 100), 255, -1)  # White rectangle where the watermark is

    # Apply inpainting
    inpainted_image = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

    # Save the inpainted image
    cv2.imwrite(output_image_path, inpainted_image)
    print(f"Inpainted image saved to {output_image_path}")

# Main script
if __name__ == "__main__":
    input_image_path = "input.jpg"  # Path to the original image
    watermarked_image_path = "watermarked_image.jpg"  # Path to save the watermarked image
    inpainted_image_path = "inpainted_image.jpg"  # Path to save the inpainted image
    watermark_text = "Sample Watermark"  # Watermark text

    # Add watermark
    add_watermark(input_image_path, watermarked_image_path, watermark_text)

    # Remove watermark
    remove_watermark(watermarked_image_path, inpainted_image_path)