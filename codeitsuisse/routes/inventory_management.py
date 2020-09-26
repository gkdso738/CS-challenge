import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def cmp(s,t):
    s = "#" + s
    t = "#" + t
    dp = []
    for i in range(len(s)+1):
        foo = []
        for i in range(len(t)+1):
            foo.append(100000000)
        dp.append(foo)
    for i in range(len(s)):
        dp[i][0] = i
    for i in range(len(t)):
        dp[0][i] = i
    for i in range(1,len(s)):
        for j in range(1,len(t)):
            dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
            dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
            if s[i] == t[j]: dp[i][j] = min(dp[i][j], dp[i-1][j-1])
            else: dp[i][j] = min(dp[i][j], dp[i-1][j-1] + 1)
    distance = dp[len(s)-1][len(t)-1]
    ans = ""
    x = len(s)-1
    y = len(t)-1
    while x>0 or y>0:
        if x == 0 or dp[x][y] == dp[x][y-1]+1:
            ans = "+" + t[y] + ans
            y -= 1
        elif y == 0 or dp[x][y] == dp[x-1][y]+1:
            ans = "-" + s[x] + ans
            x -= 1
        else:
            ans = t[y] + ans
            x -= 1
            y -= 1
    return distance, ans

def solve(target, a):
    ans = []
    for str in a:
        ans.append(cmp(target,str.lower()))
    ans.sort()
    if len(ans) < 10: return ans
    return ans[:10]
    

@app.route('/inventory-management', methods=['POST'])
def evaluate_inventory_management():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    
    target = data["searchItemName"]
    a = data["items"]
    result = {"searchItemName": target, "searchResult": []}
    temp = solve(target.lower(), a)
    for i in range(len(ans)):
      result["searchResult"].append(ans[i][1])
    logging.info("My result :{}".format(result))
    return jsonify(result);
