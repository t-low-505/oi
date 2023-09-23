import sys
import pytesseract
from PIL import Image, ImageDraw
import argparse


# Define a function to convert color names to RGB values
from extracted_parts import color_name_to_rgb

# Define the function to highlight the given text in the given image
def highlight_text(image_file, text, padding, thickness, color, opacity, corners_radius):
    # Convert the color argument to a tuple of integers
    color = color_name_to_rgb(color)
    # Open the image
    img = Image.open(image_file)
    # Use pytesseract to get the data from the image
    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
    # Try to find the index of the given text in the 'text' list
    try:
        index = data['text'].index(text)
    except ValueError:
        print(f'"{text}" not found in the image.')
        sys.exit(1)
    # Get the bounding box coordinates for the given text
    left = data['left'][index] - padding
    top = data['top'][index] - padding
    width = data['width'][index] + 2 * padding
    height = data['height'][index] + 2 * padding
    # Create a Draw object
    draw = ImageDraw.Draw(img, 'RGBA')
    # Draw a rectangle on the image
    rectangle_position = [left, top, left + width, top + height]
    draw.rounded_rectangle(rectangle_position, outline=(color[0], color[1], color[2], int(opacity * 255)), width=thickness, radius=corners_radius)
    # Save the modified image
    img.save('highlighted_' + image_file)
# Use the argparse module to handle command line parameters
from extracted_parts import create_parser
parser, args = create_parser()
# Call the function with the command line parameters
highlight_text(args.image_file, args.text, args.padding, args.thickness, args.color, args.opacity, args.corners_radius)
