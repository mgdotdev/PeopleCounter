import tempfile
from six.moves.urllib.request import urlopen
from six import BytesIO
from PIL import Image
from PIL import ImageOps

def download_and_resize_image(
    url, new_width=256, new_height=256
    ):
    
    filename = tempfile.mkstemp(suffix=".jpg")[1]
    response = urlopen(url)
    image_data = response.read()
    image_data = BytesIO(image_data)
    pil_image = Image.open(image_data)
    pil_image = ImageOps.fit(pil_image, (new_width, new_height), Image.ANTIALIAS)
    pil_image_rgb = pil_image.convert("RGB")
    pil_image_rgb.save(filename, format="JPEG", quality=90)

    return filename