import PeopleCounter
from os import path

# image_url = 'https://raw.githubusercontent.com/1mikegrn/PeopleCounter/master/images/my_screenshot.png'

input_image = path.join(r'D:\Programming\ZZ_Hackathon\Hackcation\PeopleCounter\images\my_screenshot.png')

results = PeopleCounter.src.Counter.Counter(input_image)

results.count_people(0.2)
