from flask import Flask, render_template
import os

template_dir = os.path.abspath('./')
app = Flask(__name__, template_folder=template_dir)
 
 
@app.route('/')
def hello_world():
    return render_template("static/index.html")
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')