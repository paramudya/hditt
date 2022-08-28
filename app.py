from flask import Flask, render_template, request, jsonify
from calc import hard_code

app = Flask (__name__)

@app.route('/')
def hello():
    return render_template("home.html")

@app.route("/result", methods=['POST','GET'])
def namafungsiirelevankah():
    data_input = (request.form)
    input_string=data_input.get('string_name') 
    output_string=hard_code(input_string)

    return render_template("result.html",input=input_string,result=output_string)

if __name__ == '__main__':
    app.run()