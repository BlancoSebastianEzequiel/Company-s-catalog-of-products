from flask import Blueprint, jsonify

EXAMPLE_BP = Blueprint('example', __name__, url_prefix='/')


@EXAMPLE_BP.route('/')
def root():
    return jsonify({"test": "Test successful"})
