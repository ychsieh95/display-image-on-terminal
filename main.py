import argparse
import os
from display import draw
from PIL import Image


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A CLI tool for displaying image on terminal.')
    parser.add_argument('-p', '--image-path', required=True, help='the file path of image')
    args = parser.parse_args()

    if not os.path.isfile(args.image_path):
        print('[FAILED] \'{}\' is not a exists file'.format(args.image_path))
    else:
        print()
        draw(Image.open(args.image_path))
