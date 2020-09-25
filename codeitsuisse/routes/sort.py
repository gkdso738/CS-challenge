import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/sort', methods=['POST'])
def evaluate():
    data = request.get_json();
    return json.dumps(data["input"].sort());
