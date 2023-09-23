
import sys
import pytesseract
from PIL import Image, ImageDraw
import argparse

# Define the function to highlight the given text in the given image
def highlight_text(image_file, text):
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
    left = data['left'][index]
    top = data['top'][index]
    width = data['width'][index]
    height = data['height'][index]

    # Create a Draw object
    draw = ImageDraw.Draw(img)

    # Draw a rectangle on the image
    rectangle_position = [left, top, left + width, top + height]
    draw.rectangle(rectangle_position, outline='red')

    # Save the modified image
    img.save('highlighted_' + image_file)

# Use the argparse module to handle command line parameters
parser = argparse.ArgumentParser(description='Highlight the given text in the given image.')
parser.add_argument('image_file', type=str, help='The image file.')
parser.add_argument('text', type=str, help='The text to be highlighted.')
args = parser.parse_args()

# Call the function with the command line parameters
highlight_text(args.image_file, args.text)
