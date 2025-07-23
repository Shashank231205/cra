# data/utils/image_receiver.py
import base64
import os

SAVE_PATH = "received.jpg"

def save_base64_image(base64_str):
    image_data = base64.b64decode(base64_str)
    with open(SAVE_PATH, "wb") as f:
        f.write(image_data)
    return SAVE_PATH
