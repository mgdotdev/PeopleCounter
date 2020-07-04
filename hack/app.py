'''
some important commands
project id : gcloud config get-value project
launch container : gcloud builds submit --tag gcr.io/hack-282223/hack or gcloud builds submit --tag gcr.io/PROJECT-ID/helloworld
launch app : gcloud run deploy --image gcr.io/hack-282223/hack --platform managed or gcloud run deploy --image gcr.io/PROJECT-ID/helloworld --platform managed

info{
    project-id : hack-282223
    project-name : hack
    url : https://hack-b6yvg7c7tq-uc.a.run.app
          https://hack-b6yvg7c7tq-uc.a.run.app
}
'''
import os

from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

beach_to_population = dict()

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    shane = os.environ.get('SHANE', 'shane')
    return 'You did it {}!\n'.format(shane)

@app.route('/update/', methods = ['GET', 'POST'])
def update():
    if request.method == 'GET':
        beach_name = request.args.get('beach', default='no_name', type=str)
        population = request.args.get('population', default=0, type=int)
        beach_to_population[beach_name] = population
        print(beach_to_population)
        return jsonify(isError= False,message= "Success",statusCode= 200,data= beach_to_population), 200

    if request.method == 'POST':
        beach_name = request.form.get('beach')
        population = request.form.get('population')
        beach_to_population[beach_name] = population
        print(beach_to_population)

@app.route('/get-beaches/', methods= ['GET'])
def get_beaches():
    return jsonify(isError= False,message= "Success",statusCode= 200,data= beach_to_population), 200

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))