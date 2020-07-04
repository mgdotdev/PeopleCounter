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
{"data":{"cook inlet":1},"isError":false,"message":"Success","statusCode":200}
```
### update
* get or post
* parameters
    * beach : name of the beach
    * populatin : number of people on beach (according to some know-it-all *robot*)
* example 
```
https://hack-b6yvg7c7tq-uc.a.run.app/update/?beach=awesome%20beach&population=1234
```
* returns json object
```json
{"data":{"awesome beach":1234,"cook inlet":1},"isError":false,"message":"Success","statusCode":200}
```