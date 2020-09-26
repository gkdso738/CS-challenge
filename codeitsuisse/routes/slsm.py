import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


def solve(n, mp, extra_roll, rnd):
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
            if extra_roll[cur] != 0:
                ans.append(extra_roll[cur])
    tcur = cur
    for i in range(1,7):
        if mp[cur+i] != n:
            cur = mp[cur+i]
            for _ in range(rnd-1):
                ans.append(i)
                if extra_roll[cur] != 0:
                    ans.append(extra_roll[cur])
            break
    for i in range(1,7):
        if mp[tcur+i] == n:
            ans.append(i)
            if extra_roll[tcur+i] != 0:
                ans.append(extra_roll[tcur+i])
            break
    return ans
def build(n, jumps):
    kw = []
    mp = {}
    extra_roll = {}
    for i in range(n+6):
        extra_roll[i] = 0
    for element in jumps:
        x,y = element.split(':')
        x = int(x)
        y = int(y)
        if x == 0:
            kw.append(y)
            mp[y] = y+6
            extra_roll[y] = 6
        else:
            kw.append(x)
            if y == 0:
                if x-1 in kw:
                    mp[x] = mp[x-1]
                else:
                    mp[x] = x-1
                extra_roll[x] = 1
            else:
                mp[x] = y
    for i in range(n+1):
        if i not in kw:
            mp[i] = i

    for i in range(n+1,n+6):
        mp[i] = mp[n+n-i]
        extra_roll[i] = extra_roll[n+n-i]
    for i in range(n+6):
        if mp[i] != i and mp[mp[i]] != mp[i]:
            mp[i] = mp[mp[i]]
    return mp, extra_roll

@app.route('/slsm', methods=['POST'])
def evaluate_slsm():

    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))

    n = data["boardSize"]
    rnd = data["players"]
    mp,extra_roll = build(n,data["jumps"])
    result = solve(n,mp,extra_roll,rnd)

    # logging.info("My result :{}".format(result))
    return jsonify(result);
