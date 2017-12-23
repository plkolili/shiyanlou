from flask import Flask,render_template
import os,json
app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True
@app.route('/')
def index():
    path='/home/shiyanlou/files'
    files=os.listdir(path=path)
    files1=os.path.join(path,files[0])
    with open( files1,'r') as f:
        shiyanlou=json.loads(f.read())
    return render_template('index.html',shiyanlou=shiyanlou) 


#@app.route('/files/<filename>')
#def file(filename):
#    os.
#
#    return render_template()

