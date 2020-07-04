import PeopleCounter
from os import path

class Counter:
    def __init__(self, file_path):

        if ('http://' in file_path or 'https://' in file_path):
            file_path = PeopleCounter.src.tools.img_from_url.download_and_resize_image(
                file_path
            )

        else:
            file_path = path.join(file_path)

        self.results = PeopleCounter.src.tools.detecting.detect_img(file_path)   

    def get_raw_results(self):
        return self.results

    def count_people(self, thrs):
        check_list = [b'Person', b'Man', b'Woman']
        people = PeopleCounter.src.tools.parse_bytes.parse(
            self.results, check_list, thrs 
        )
        return len(people)

    def custom_count(self, check_list, thrs):

        check_list = [bytes(x, 'utf-8') for x in check_list]

        counts = PeopleCounter.src.tools.parse_bytes.parse(
            self.results, check_list, thrs 
        )

        return len(counts)
