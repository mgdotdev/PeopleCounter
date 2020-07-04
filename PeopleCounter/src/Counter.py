import PeopleCounter
from os import path

def Counter(file_path, thrs):

    if ('http://' in file_path or 'https://' in file_path):
        file_path = PeopleCounter.src.tools.img_from_url.download_and_resize_image(
            file_path
        )

    else:
        file_path = path.join(file_path)

    results = PeopleCounter.src.tools.detecting.detect_img(file_path)   

    results = PeopleCounter.src.tools.parse_bytes.parse(results, thrs)

    return results
