"""
Policy Provider Service

is used to link privacy preferences or generalized usage policies to external datasets
"""
from flask import Flask, request, Response, jsonify, render_template, current_app
from bson import json_util
from pymongo import MongoClient
import os
import json
import jsonschema

app = Flask(__name__)

client = MongoClient('mongodb://' + os.environ['mongodb_user'] + ':' + os.environ['mongodb_pw'] + os.environ['mongodb_url'])
db = client.CoMaPo
my_pref = db.usage_prefs


def validate(policy):
    try:
        yappl_schema = open('YaPPL_schema.json', 'r')
        yappl_load = True
    except IOError:
        yappl_load = False

    if yappl_load:
        yappl_schema = yappl_schema.read()
        yappl_schema = json.loads(yappl_schema)
        #  policy = json.loads(policy)
    else:
        return 'SchemaLoadError'

    try:
        val_result = jsonschema.validate(policy, yappl_schema)
        return 'valid'
    except jsonschema.SchemaError:
        return 'SchemaError'
    except jsonschema.ValidationError:
        return 'ValidationError'

    val_result = val_result  # ???


@app.route('/', methods=['GET'])
def index():
    urls = dict([(r.rule, current_app.view_functions.get(r.endpoint).__doc__) for r in current_app.url_map.iter_rules() if not r.rule.startswith('/static')])
    return render_template('index.html', urls=urls)


@app.route('/schema', methods=['GET'])
def get_yappl_schema():
    """ GET the YaPPL-policy json-schema"""

    yappl_schema = open('YaPPL_schema.json', 'r')
    yappl_schema = yappl_schema.read()
    yappl_schema = json.loads(yappl_schema)

    return Response(json_util.dumps(yappl_schema), mimetype='application/json')


@app.route("/<id>", methods=['GET'])
def get_policy(id):
    """ GET a YaPPL-policy with the passed <id>"""
    policy = my_pref.find_one({"_id": int(id)})
    if policy is None:
        return jsonify({"policy": "not found"})
    else:
        return Response(json_util.dumps(policy), mimetype='application/json')


@app.route("/", methods=['POST'])
def create_policy():
    """ POST a YaPPL-policy to create a corresponding database entry"""
    policy = request.get_json()

    if my_pref.find_one({'_id': policy['_id']}) is not None:
        return "409 - Conflict (there already exits an entry with this id)"
    else:
        validation = validate(policy)
        if validation == 'valid':
            my_pref.insert_one(policy)
            return "200 - Policy created & saved."
        elif validation == 'ValidationError':
            return "ValidationError"
        else:
            return "An Error occurred"


if __name__ == '__main__':
    app.run()