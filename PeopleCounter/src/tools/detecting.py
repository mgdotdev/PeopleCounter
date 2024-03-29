import PeopleCounter

import tensorflow as tf
import numpy as np
import time

def load_img(path):
    img = tf.io.read_file(path)
    img = tf.image.decode_jpeg(img, channels=3)
    return img

def run_detector(detector, path):

    img = load_img(path)

    converted_img  = tf.image.convert_image_dtype(
        img, tf.float32
    )[tf.newaxis, ...]
    
    result = detector(converted_img)

    return_dict = {key: value.numpy() for key, value in result.items()}

    return return_dict