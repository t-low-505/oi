
import sys
import pytesseract
from PIL import Image, ImageDraw
import argparse
from extracted_parts import color_name_to_rgb

def highlight_text(image_file, text, padding, thickness, color, opacity, corners_radius):
    color = color_name_to_rgb(color)
    original_img = Image.open(image_file)
    data = pytesseract.image_to_data(original_img, output_type=pytesseract.Output.DICT)
    try:
        indexes = [i for i, t in enumerate(data['text']) if t == text or text == ""]
    except ValueError:
        print(f'"{text}" not found in the image.')
        sys.exit(1)
    for i, index in enumerate(indexes):
        img = original_img.copy()
        left = data['left'][index] - padding
        top = data['top'][index] - padding
        width = data['width'][index] + 2 * padding
        height = data['height'][index] + 2 * padding
        draw = ImageDraw.Draw(img, 'RGBA')
        rectangle_position = [left, top, left + width, top + height]
        draw.rounded_rectangle(rectangle_position, outline=(color[0], color[1], color[2], int(opacity * 255)), width=thickness, radius=corners_radius)
        img.save(f'highlighted_{i}_{image_file}' if text != "" else f'highlighted_all_{i}_{image_file}')

from extracted_parts import create_parser
parser, args = create_parser()
highlight_text(args.image_file, args.text if args.text is not None else '', args.padding, args.thickness, args.color, args.opacity, args.corners_radius)
