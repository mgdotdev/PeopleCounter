# PeopleCounter

[![Website](https://img.shields.io/badge/Site-BeachWatch-blue)](https://1mikegrn.github.io/PeopleCounter/)

This is a multi-paradigm Hackathon project created by Michael Green and Shane May for the 2020 MLH Hackcation hackathon. There are several pieces which collectively form this project: The computing module, the uploader, the microservice, and the front-end.

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