from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello everyone,this is my first flask app'

if __name__ == '__main__':
    app.run()