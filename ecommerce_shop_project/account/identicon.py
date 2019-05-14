import sys
import hashlib
from PIL import Image

IMAGE_SIZE = (128, 128)
IMAGE_MODE = "RGB"


def get_identicon(string):

    hash_string = get_hash_string(string)
    color = get_color(hash_string)


def get_hash_string(string):

    hash_string = hashlib.md5(str.encode(string.lower()))
    return hash_string.hexdigest()


def get_color(hash):
    return hash[:6]


def create_image(image_mode, image_size, color):

    image = Image.new(image_mode, image_size, color)
