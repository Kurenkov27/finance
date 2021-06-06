import json

from flask import Flask

import data_scrapper
from sql import write_data, delete_data, get_json_data, get_json_elems_by_name

app = Flask(__name__)

elems = ['PD', 'ZUO', 'PINS', 'ZM', 'PVTL', 'DOCU', 'CLDR', 'RUN']


@app.route('/')
def hello_world():
    response = app.response_class(
        response=json.dumps(get_json_data()),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/refresh/')
def refresh_data():
    data_scrapper.run_load_data(elems)
    delete_data()
    write_data(elems)
    return 'Data is updated'


@app.route('/<string:elem>/')
def get_elem_data(elem):
    response = app.response_class(
        response=json.dumps(get_json_elems_by_name(elem.upper())),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run()
