import PeopleCounter
import tensorflow_hub as hub
from os import path

class Counter:
    def __init__(self, file_path=None):

        self.detector = hub.load(
        "https://tfhub.dev/google/faster_rcnn/openimages_v4/inception_resnet_v2/1"
        ).signatures['default']

        if file_path == None:
            self.results = None

        else:
            self.new_query(file_path)

    def new_query(self, file_path):

        if ('http://' in file_path or 'https://' in file_path):
            file_path = PeopleCounter.src.tools.img_from_url.download_and_resize_image(
                file_path
            )

        else:
            file_path = path.join(file_path)

        self.results = PeopleCounter.src.tools.detecting.run_detector(
            self.detector, file_path
        )   

    def get_raw_results(self):

        self.check_init()

        return self.results

    def count_people(self, thrs):

        self.check_init()

        check_list = [b'Person', b'Man', b'Woman']
        people = PeopleCounter.src.tools.parse_bytes.parse(
            self.results, check_list, thrs 
        )
        return len(people)

    def custom_count(self, check_list, thrs):

        self.check_init()

        check_list = [bytes(x, 'utf-8') for x in check_list]

        counts = PeopleCounter.src.tools.parse_bytes.parse(
            self.results, check_list, thrs 
        )

        return len(counts)

    def check_init(self):
        assert self.results != None, (
            'You must first run a query before acquiring results! Use' 
            '.new_query(path) to start your query'
        )
