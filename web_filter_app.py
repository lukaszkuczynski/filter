from flask import Flask, request
import json
from filter_processor import FilterProcessor
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, I am filter processor. Hit /filter endpoint to have your docs processed according to rules (/rules)'


@app.route('/filter', methods=['POST'])
def filter_endpoint():
    documents = request.get_json(force=True)
    rules = get_filter_rules_dict()
    print(rules)
    print(type(rules))
    processor = FilterProcessor(rules)
    try:
        left, removed = processor.process(docs=documents)
        print("There were %d docs removed according to %d rules defined. There are %d docs left" % (len(removed), len(rules), len(left)))
        return json.dumps({'success': True, 'left': left}), 200, {'ContentType': 'application/json'}
    except Exception as e:
        return json.dumps({'success': False, 'msg': e.__str__()}), 500, {'ContentType': 'application/json'}


@app.route("/rules")
def get_filter_rules():
    rules = get_filter_rules_dict()
    return json.dumps(rules)


def get_filter_rules_dict():
    rules_json = os.getenv("FILTER_RULES_JSON", "[]")
    rules = json.loads(rules_json)
    return rules
