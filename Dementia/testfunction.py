from PIL import Image
import base64
import io

def f(request):
    # Decode the base64 string
        image_data = base64.b64decode(request.image_data)
        image = Image.open(io.BytesIO(image_data))

        # Here you can add your image processing logic
        # For this example, we'll just return the size of the image
        width, height = image.size

        return {"width": width, "height": height}