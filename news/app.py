from flask import Flask,render_template
import os
app=Flask(__name__)
app.config('TEMPLATE_AUTO_RELOAD']=True
@app.route('/')
def index():
    os.

    return render_template('index.html',) 


@app.route('/files/<filename>')
def file(filename):
    os.

    return render_template()

