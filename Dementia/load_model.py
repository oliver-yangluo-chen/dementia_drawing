import numpy as np
import tensorflow as tf
import keras

from PIL import Image
import base64
import io

import os

class CustomScaleLayer(keras.layers.Layer):
    def __init__(self, scale, **kwargs):
        super().__init__(**kwargs)
        self.scale = scale

    def get_config(self):
        config = super().get_config()
        config.update({"scale": self.scale})
        return config

    def call(self, inputs):
        return inputs[0] + inputs[1] * self.scale
    
    @classmethod
    def from_config(cls, config):
        sublayer_config = config.pop("sublayer")
        sublayer = keras.saving.deserialize_keras_object(sublayer_config)
        return cls(sublayer, **config)

model_path = "my_model_full.keras"

#model = keras.models.load_model(model_path, custom_objects={'Custom>CustomScaleLayer': CustomScaleLayer})

model = keras.models.load_model(model_path)

#model.summary()

def prepare_image(image_path, target_size=(299, 299)):
    image = keras.utils.load_img(image_path, target_size=target_size)
    image = keras.utils.img_to_array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image




dementia_folder = 'AD/'  # Replace with your folder path
dementia_imgs = os.listdir(dementia_folder)
dementia_imgs = [f for f in dementia_imgs if os.path.isfile(os.path.join(dementia_folder, f))]
                 

normal_folder = 'HC/'
normal_imgs = os.listdir(normal_folder)
normal_imgs = [f for f in normal_imgs if os.path.isfile(os.path.join(normal_folder, f))]

print("DEMENTIA!")
for i in dementia_imgs:
    img = dementia_folder + i
    prepared_img = prepare_image(img)
    print(model.predict([prepared_img]))

print()

print("NORMAL!")
for i in normal_imgs:
    img = normal_folder + '/' + i
    prepared_img = prepare_image(img)
    print(model.predict([prepared_img]))