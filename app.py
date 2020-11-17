from flask import Flask, render_template, request
from lights import *

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('ON') == 'ON':
            print("Lights ON")
            setup()
            turn_on()
        elif  request.form.get('OFF') == 'OFF':
            print("Lights OFF")
            setup()
            turn_off()
            destroy()
        else:
            return render_template("index.html")
    elif request.method == 'GET':
        print("No Post Back Call")
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=int("5001"))