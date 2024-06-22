import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from PIL import Image
import base64
import io

from testfunction import f

app = FastAPI()

class ImageRequest(BaseModel):
    image_data: str  # Base64-encoded string of the image

@app.post("/process-image/")
async def process_image(request: ImageRequest):
    try:
        return f(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
