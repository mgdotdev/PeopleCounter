'''
some important commands
project id : `gcloud config get-value project`
launch container : `gcloud builds submit --tag gcr.io/PROJECT-ID/helloworld`
launch app : `gcloud run deploy --image gcr.io/PROJECT-ID/helloworld --platform managed`

info{
    project-id : hack-282223
    project-name : hack
    url : https://hack-b6yvg7c7tq-uc.a.run.app
}
'''
import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    shane = os.environ.get('SHANE', 'shane')
    return 'You did it {}!\n'.format(shane)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))