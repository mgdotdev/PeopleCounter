import PeopleCounter
from selenium import webdriver
import requests
import time
from os import path

here = path.dirname(path.abspath(__file__))
url = 'https://www.youtube.com/embed/'

places = [
    'Southampton, NY',
    'Ehukai Beach, HI',
    'Waimea Bay, HI',
    'Cayucos Beach, CA',
    'Mori Point, CA',
    'Pacifica Pier, CA',
    'Santa Monica Pier, CA',
    'Clearwater Beach, FL',
    'Miramar Beach, FL',
    'Santa Rosa Beach, FL',
    'Panama City Beach, FL'
]

vids = [
    'WNeVYGasWMc',
    'DY5RYp4sxYc',
    'wnNrd-VjLsQ',
    'XKu1-q7Q2YE',
    'y0iKpoQbcbg',
    'ypcwqwRe8Ww',
    'OWbI6WtlI-k',
    'fa7wCF6JL1w',
    'QgAFWjRXpqI',
    'ftGfQqCA184',
    'NEli-J4WB24'
]

tag = '?rel=0&amp;autoplay=1;vq=hd720;mute=true'

DRIVER = r'D:\Downloads\Google\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(DRIVER)

for _ in range(len(vids)-1):
    driver.execute_script("window.open('');")

for cnt, vid in enumerate(vids):
    driver.switch_to.window(driver.window_handles[cnt])
    driver.get(url+vid+tag)
    time.sleep(5)

def grab_stills():
    for cnt, vid in enumerate(vids):
        driver.switch_to.window(driver.window_handles[cnt])
        driver.save_screenshot(
            path.join(here, 'images', 'bulk', '{}.png'.format(vid))
        )

counter = PeopleCounter.src.Counter.Counter()

while True:

    grab_stills()

    for cnt, vid in enumerate(vids):

        counter.new_query(
            path.join(here, 'images', 'bulk', '{}.png'.format(vid))
        )

        ppl = counter.count_people(thrs=0.05)

        place = '%20'.join(places[cnt].split(' '))

        requests.get(
            'https://hack-b6yvg7c7tq-uc.a.run.app/update/?beach={}&population={}&video_id={}'.format(
                place, ppl, vid
            )
        )

        print('sent get req for {}'.format(places[cnt]))

driver.quit()