# PeopleCounter

[![Website](https://img.shields.io/badge/Site-BeachWatch-blue)](https://1mikegrn.github.io/PeopleCounter/)

This is a multi-paradigm Hackathon project created by Michael Green and Shane May for the 2020 MLH Hackcation hackathon. There are several pieces which collectively form this project: The computing module, the uploader, the microservice, and the front-end.

## What it does

The suite accomplishes multiple tasks:

1) It collects live video data from youtube.
2) It executes object detection on still images so to count the number of people at the beach.
3) It sends the object count to a google cloud microservice which hosts the data.
4) It provides the user of the website relative populations of the beaches, with the option to see the live feed directly.

## How we built it

Michael developed the computing module and web scraper, Shane built the front-end and we collectively worked on the microservice.

## Challenges we ran into

We originally wanted to have the computing and data collection engine runnning on the google cloud service as well, but we were unable to come up with a means for rendering the youtube image data non-locally. We settled to run the collection and detection locally and simply push the results to the microservice.

## Accomplishments we're proud of

Overall we were able to generate a functional website that accomplished the task we set out to achieve. We learned how to use google cloud to host our Flask instance, which was a first for both of us.

## What we learned

Michael: I learned about tensorflow-hub and how to implement their pre-built models, and how to host web services in the google cloud.

Shane: I learned how to use Flask and Docker for developing back-end services in google cloud.  

# Additional information

## Computing Module

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/1mikegrn/PeopleCounter/blob/master/colab/PeopleCounter.ipynb)

The computing module is a pip-installable Python library which integrates the pre-trained Inception Resnet model from tensorflow-hub into a class object which allows for image object detection. For beach watch, images of beaches are fed to the class object which counts the number of people objects within the image and returns the count.

## Uploader

The uploader is a python script which automates a local instance of google chrome. This automated webbrowser queries a set of youtube links which route to live webcam streams of a set of beaches. Once queried and buffered, the uploader takes a screenshot. Each screenshot is them passed to the computing module, which returns the number count. This and other ancillary information is finally passed to the microservice hosted in the google cloud.

## Microservice

The microservice is a docker/flask instance hosted in the google compute engine. The instance receives get requests at a designated URL from the uploader, and updates the internal hashmap pertaining to the specified beach. This hashmap is subsequently queried by the front-end when the website is loaded.

## Frontend

The frontend is the static webpage hosted at https://1mikegrn.github.io/PeopleCounter
with the associated HTML file located in the `docs/` folder of this repository. The webpage pings the microservice for the available data and parses it out to a user interface. The front-end also displays the original live youtube feeds when requrested by the user.

