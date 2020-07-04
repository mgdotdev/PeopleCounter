def parse(results_dict, thrs):
    return_list = [
        [x[0].decode('utf-8'), x[1]] 
        for x in zip(
            results_dict['detection_class_entities'], 
            results_dict['detection_scores']
        ) if (x[0] in [b'Person', b'Man', b'Woman'] and x[1] > thrs)
    ]
    return return_list
