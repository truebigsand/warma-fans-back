import flask
import flask_cors
from Sqlite3Helper import Sqlite3Helper
from videomaker import *
import updater
import json

app = flask.Flask(__name__)
flask_cors.CORS(app, supports_credentials=True)
db = Sqlite3Helper('warma.db')

@app.route('/')
def api():
    return '{"msg":"Welcome to api!"}';

@app.route('/all')
def all():
    videos = db.query('SELECT * FROM videos')
    if videos == []:
        return '{"data":[]}'
    result = {'data':makevideos(videos)}
    return json.dumps(result)#.encode('utf-8').decode('unicode_escape')

@app.route('/update')
def update():
    return updater.update()

@app.route('/search/<string:TYPE>/<string:CONTENT>')
def search(TYPE,CONTENT):
    if ['title','description','author','aid','bvid'].count(TYPE) == 0:
        return '{"msg":"Undefined type ' + TYPE + '"}';
    videos = db.query('SELECT * FROM videos WHERE ' + TYPE + ' like \'%' + '%'.join(CONTENT) + '%\'')
    if videos == []:
        return '{"data":[],"msg":"success"}'
    result = {'data':makevideos(videos)}
    return json.dumps(result)#.encode('utf-8').decode('unicode_escape')

@app.route('/query/<string:command>/<string:password>')
def query(command,password):
    if password == '123456':
        return json.dumps(db.query(command))
    else:
        return "You have no limits of authority to use this api";

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")