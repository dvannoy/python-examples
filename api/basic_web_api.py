import sqlite3
from flask import Flask, jsonify, abort, g, make_response, request
# from config import FLASK_SECRET_KEY

DATABASE = 'vehicle_stops.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
PORT = 5000  # 5000 is default

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('WEB_API_SETTINGS', silent=True)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# def connect_db():
#     rv = sqlite3.connect(app.config['DATABASE'])
#     rv.row_factory = sqlite3.Row
#     return rv


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def query_db(query, args=()):
    cur = g.db.execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows


def make_stops_dictionary(rows):
    stops = [dict(stop_id=row[0], stop_cause=row[1], service_area=row[2], subject_race=row[3]) for row in rows]
    return stops


@app.route('/vehicle_stops/v0.1', methods=['GET'])
def get_list():
    pagesize = 50
    page = request.args.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    skip = (page - 1) * pagesize + 1
    rows = query_db('select * from vehicle_stops order by stop_id asc limit ?, ?', [skip, pagesize])
    if len(rows) == 0:
        abort(404)

    stop = make_stops_dictionary(rows)
    return jsonify(dict(stop=stop))

@app.route('/vehicle_stops/v0.1/<int:stop_id>', methods=['GET'])
def get_stop(stop_id):
    rows = query_db('select * from vehicle_stops where stop_id = ?',
                    [stop_id])
    if len(rows) == 0:
        abort(404)

    stop = make_stops_dictionary(rows)
    return jsonify(dict(stop=stop[0]))


if __name__ == '__main__':
    app.run(port=PORT)  # Used for development mode, do not use run() in production situation