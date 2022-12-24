import os
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

content_path = '../images/360.jpg'
style_path = '../images/vangogh_starry.jpg'

def load_img(path_to_img):
  max_dim = 512
  img = tf.io.read_file(path_to_img)
  img = tf.image.decode_image(img, channels=3)
  img = tf.image.convert_image_dtype(img, tf.float32)

  shape = tf.cast(tf.shape(img)[:-1], tf.float32)
  long_dim = max(shape)  #type: ignore
  scale = max_dim / long_dim

  new_shape = tf.cast(shape * scale, tf.int32)

  img = tf.image.resize(img, new_shape)
  img = img[tf.newaxis, :] # type: ignore
  return img

content_image = load_img(content_path)
style_image = load_img(style_path)

'''
plt.imshow(np.squeeze(content_image))
plt.show()

plt.imshow(np.squeeze(style_image))
plt.show()
'''

import tensorflow_hub as hub
model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0] # type: ignore


plt.imshow(np.squeeze(stylized_image))
plt.show()

import cv2

cv2.imwrite('../images/stylized.jpg', cv2.cvtColor(np.squeeze(stylized_image)*255, cv2.COLOR_BGR2RGB))