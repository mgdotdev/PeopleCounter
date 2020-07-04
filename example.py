import PeopleCounter
from os import path
import time

image_url = 'https://raw.githubusercontent.com/1mikegrn/PeopleCounter/master/images/my_screenshot.png'

input_image = path.join(r'D:\Programming\ZZ_Hackathon\Hackcation\PeopleCounter\images\my_screenshot_100.png')

results = PeopleCounter.src.Counter.Counter()

t1 = time.time()
results.new_query(input_image)
one = results.count_people(0.2)
t2 = time.time()
results.new_query(image_url)
two = results.count_people(0.2)
t3 = time.time()

print(one, t2-t1)
print(two, t3-t2)