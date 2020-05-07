import flask
from flask import Flask, render_template
from numpy import block
from pyxb.bundles.wssplat.raw.soapbind11 import body

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', body=body, block=block)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')