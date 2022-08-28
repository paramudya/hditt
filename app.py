from flask import Flask
app = Flask (__name__)

@app.route('/')
def hello():
    return 'Hello this is the dummy for us dummies to deply our dumb dumb depressing project!'

if __name__ == '__main__':
    app.run()