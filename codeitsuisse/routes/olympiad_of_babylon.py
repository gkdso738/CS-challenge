import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

import numpy as np
def solve(books, days):
    books.sort()
    days.sort()
    cur = 0
    sum = 0
    while cur < len(books):
        if days == []: return cur
        if sum + books[cur] > days[len(days)-1]:
            for j in range(len(days)):
                if days[j] >= sum:
                    days = days[:j] + days[j+1:]
                    break
            sum = 0
        sum += books[cur]
        if days == [] or sum > days[len(days)-1]: return cur
        cur += 1
    

@app.route('/olympiad-of-babylon', methods=['POST'])
def evaluate_salad_spree():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    
    books = data["books"]
    days = data["days"]
    result = solve(books,days)
    
    logging.info("My result :{}".format(result))
    return jsonify({"result": result});
