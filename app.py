from flask import Flask, render_template, request, jsonify
from secret import hard_code

app = Flask (__name__)

@app.route('/')
def hello():
    return render_template("home.html")
@app.route("/result", methods=['POST','GET'])
def namafungsiirelevankah():
    data_input = (request.form)
    # input_string=data_input.get('text')

    output_string=hard_code(input_string)

    return render_template("result.html",input='asd',result=output_string)

if __name__ == '__main__':
    app.run()