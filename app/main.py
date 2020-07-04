from flask import Flask, render_template
from os import path
# import PeopleCounter

app = Flask(__name__)
here = path.dirname(path.abspath(__file__))

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='localhost', port=5500, debug=True)