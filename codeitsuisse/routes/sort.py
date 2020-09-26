import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/sort', methods=['POST'])
def evaluate_sort():
    data = request.get_json();
    cnt = []
    for _ in range(20001):
        cnt.append(0)
    for element in data:
        cnt[element+10000] += 1
    for i in range(20001):
        for j in range(cnt[i]):
            data[i] = i-10000
    return jsonify(ans);
