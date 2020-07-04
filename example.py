import PeopleCounter
from os import path

# image_url = 'https://raw.githubusercontent.com/1mikegrn/PeopleCounter/master/images/my_screenshot.png'

# image = PeopleCounter.src.tools.helpers.download_and_resize_image(
#         image_url, 640, 480
#     )

# image is a python-generic file path to a .jpg file
input_image = path.join(r'D:\Programming\ZZ_Hackathon\Hackcation\PeopleCounter\images\Untitled.jpg')

# can be url string refactored by 'img_from_url.py'
image_url = 'https://raw.githubusercontent.com/1mikegrn/PeopleCounter/master/images/my_screenshot.png'
input_image = PeopleCounter.src.tools.img_from_url.download_and_resize_image(
    image_url
)

results = PeopleCounter.src.tools.detecting.detect_img(input_image)
