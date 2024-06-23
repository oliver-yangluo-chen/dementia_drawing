import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from PIL import Image
import base64
import io

from misc import decode, pil_to_tf_array, category

import numpy as np
import tensorflow as tf

app = FastAPI()

class ImageRequest(BaseModel):
    image_data: str  # Base64-encoded string of the image

model_path = "best_model.keras"

#model = keras.models.load_model(model_path, custom_objects={'Custom>CustomScaleLayer': CustomScaleLayer})

model = tf.keras.models.load_model(model_path)

@app.post("/process-image/")
async def process_image(request: ImageRequest):
    try:
        img = decode(request.image_data)
        tf_img = pil_to_tf_array(img)
        ans = model.predict(tf_img)[0][0]
        return (category(ans), ans)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
