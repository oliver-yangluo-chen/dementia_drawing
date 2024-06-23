import base64

file_path = "encoded.txt"

with open("test_img.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    with open(file_path, 'w') as file:
        file.write(encoded_string)