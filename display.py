import random
import sys


def image_average(x1, y1, x2, y2, img):
    average = lambda x: sum(x) / len(x) if len(x) > 0 else 0
    ret = []
    for x in range(x1, x2):
        for y in range(y1, y2):
            ret.append(average(img.getpixel((x, y))[:3]))
    return average(ret)

def convert_index(x):
    if x <  3: return x
    if x == 3: return 6
    if x == 4: return 3
    if x == 5: return 4
    if x == 6: return 5
    if x == 7: return 7

def draw(image):
    start = 0x2800
    char_width = 10
    char_height = char_width * 2
    dither, sensitivity = 5, 0.6
    char_width_divided, char_height_divided = round(char_width / 2), round(char_height / 4)
    match = lambda a, b: a < b if '--invert' in sys.argv else a > b
    for y in range(0, image.height - char_height - 1, char_height):
        for x in range(0, image.width - char_width - 1, char_width):
            byte, index = 0x0, 0
            for xn in range(2):
                for yn in range(4):
                    avg = image_average(x + (char_height_divided * xn), y + (char_width_divided * yn), x + (char_height_divided * (xn + 1)), y + (char_width_divided * (yn + 1)), image)
                    if match(avg + random.randint(-dither, dither), sensitivity * 0xff):
                        byte += 2 ** convert_index(index)
                    index += 1
            print(chr(start + byte), end='')
        print()
