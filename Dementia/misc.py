from PIL import Image
import base64
import io
import numpy as np
import tensorflow as tf

def decode(request):
    # Decode the base64 string
        image_data = base64.b64decode(request)
        image = Image.open(io.BytesIO(image_data))

        return image

def pil_to_tf_array(pil_image):
    """
    Convert a PIL Image object to a TensorFlow array using keras.utils.img_to_array.

    Parameters:
    pil_image (PIL.Image.Image): The input PIL Image object.

    Returns:
    np.ndarray: The converted TensorFlow array.
    """
    # Convert the PIL Image to a numpy array
    numpy_array = np.array(pil_image)
    
    # Convert the numpy array to a TensorFlow array using keras.utils.img_to_array
    tf_array = tf.keras.utils.img_to_array(numpy_array)

    tf_array = tf_array / 255.0
    tf_array = np.expand_dims(tf_array, axis=0)
    return tf_array
    
    return tf_array

def category(p):
      if p > 0.375: return "NO"
      return "YES"
