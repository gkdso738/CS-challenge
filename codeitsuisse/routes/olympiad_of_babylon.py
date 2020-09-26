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
    return cur

def solve2(books, days):
    books.sort()
    sum = 0
    ans = -1
    for i in range(len(days)):
        sum += days[i]
    for i in range(len(books)):
        if books[i] > sum:
            ans = i
            break
        sum -= books[i]
    if ans == -1: ans = len(books)
    return ans
    for cand in range(ans, -1, -1):
        subset = books[:cand]
        subset.reverse()
        for i in range(len(days)):
            x = days[i]
            if subset == []: break
            while subset != [] and x >= subset[len(subset)-1]:
                for j in range(len(subset)):
                    if x >= subset[j]:
                        x -= subset[j]
                        subset = subset[:j] + subset[j+1:]
                        break
        if subset == []:
            return cand

@app.route('/olympiad-of-babylon', methods=['POST'])
def evaluate_salad_spree():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    
    books = data["books"]
    days = data["days"]
    result = solve2(books,days)
    
    logging.info("My result :{}".format(result))
    return jsonify({"optimalNumberOfBooks": result});
