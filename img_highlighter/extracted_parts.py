
import argparse

def create_parser():
    parser = argparse.ArgumentParser(description='Highlight the given text in the given image.')
    parser.add_argument('image_file', type=str, help='The image file.')
    parser.add_argument('text', type=str, nargs='?', default=None, help='The text to be highlighted. If not provided, all found phrases or single words will be highlighted.')
    parser.add_argument('--padding', type=int, default=100, help='The padding around the text.')
    parser.add_argument('--thickness', type=int, default=50, help='The thickness of the line.')
    parser.add_argument('--color', type=str, default='red', help='The color of the line.')
    parser.add_argument('--opacity', type=float, default=0.3, help='The opacity of the line.')
    parser.add_argument('--corners_radius', type=int, default=50, help='The radius of the corners of the rectangle.')
    args = parser.parse_args()
    return parser, args

def color_name_to_rgb(color_name):
    colors = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255), 'black': (0, 0, 0), 'white': (255, 255, 255)}
    return colors.get(color_name.lower(), (255, 0, 0))
