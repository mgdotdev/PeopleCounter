# Hack microservice info! 
## Your one-stop shop for sketchy data!

## Base url: ``` https://hack-b6yvg7c7tq-uc.a.run.app ```

## Routs
### get-beaches
* get or post
* example 
```
https://hack-b6yvg7c7tq-uc.a.run.app/get-beaches/
```
* returns json object like 
```json
{"data":{"DY5RYp4sxYc":{"beach_name":"awesome1 beach","population":1010}},"isError":false,"message":"Success","statusCode":200}
```
### update
* get or post
* parameters
    * beach : name of the beach
    * populatin : number of people on beach (according to some know-it-all *robot*)
    * video_id : the video id from youtube (giberish at the end)
* example 
```
https://hack-b6yvg7c7tq-uc.a.run.app/update/?beach=awesome1%20beach&population=1010&video_id=DY5RYp4sxYc
```
* returns json object
```json
{"data":{"DY5RYp4sxYc":{"beach_name":"awesome1 beach","population":1010}},"isError":false,"message":"Success","statusCode":200}
```

## Resources
### Google Cloud Platform (gcp)
* [Cloud Run](https://cloud.google.com/run/docs/quickstarts/build-and-deploy#python)
* [App Engine](https://console.cloud.google.com/appengine/start?project=hack-282223&folder&organizationId)
* [Dashboard to see your projects](https://console.cloud.google.com/)