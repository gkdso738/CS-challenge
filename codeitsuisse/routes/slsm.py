import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


def solve(n, mp, rnd):
    ans = []
    cur = 1
    while cur+6 < n:
        mx = -1
        cand = 0
        for i in range(1,7):
            if mp[cur+i] > mx:
                mx = mp[cur+i]
                cand = i
        if mx == n: break
        cur = mx
        for _ in range(rnd):
            ans.append(cand)
    for i in range(1,7):
        if mp[cur+i] != n:
            cur = mp[cur+i]
            for _ in range(rnd-1):
                ans.append(i)
            break
    for i in range(1,7):
        if mp[cur+i] == n:
            ans.append(i)
            break
    while cur < n:
        mx = -1
        cand = 0
        for i in range(1,7):
            if mp[cur+i] > mx:
                mx = mp[cur+i]
                cand = i
        cur = mx
        for _ in range(rnd-1):
            ans.append(cand)
    return ans
def build(n, jumps):
    kw = []
    mp = {}
    for element in jumps:
        x,y = element.split(':')
        x = int(x)
        y = int(y)
        if x == 0:
            kw.append(y)
            mp[y] = y+6
        else:
            kw.append(x)
            if y == 0:
                mp[x] = x+6
            else:
                mp[x] = y
    for i in range(n):
        if i not in kw:
            mp[i] = i
    for i in range(n+1,n+6):
        mp[i] = mp[n+n-i]
    return mp

@app.route('/slsm', methods=['POST'])
def evaluate_slsm():
    
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    
    n = data["boardSize"]
    rnd = data["players"]
    mp = build(n,data["jumps"])
    result = solve(n,mp,rnd)
    
    # logging.info("My result :{}".format(result))
    return jsonify(result);

