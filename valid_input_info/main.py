import functions_framework
import random
from flask import jsonify


@functions_framework.http
def is_valid_input(request):
    y = request.args
    x = y['input'] #value in x
    
    flag1 = 0
    if x == "0" or x == "1":
        flag1 = 2
    try:
        if float(x) and flag1 == 0:
            flag1 = 1
    except:
        pass

    if x.isalpha():
        if x.islower():
            output = {"input_type" :"lower case", "status" : 200}
            return jsonify(output)
        else:
            output = {"input_type" :"given alphabet", "status" : 405}
            return jsonify(output)

    elif flag1 == 1:
        output = {"input_type" :"float", "status" : 400}
        return jsonify(output)
    elif flag1 == 2:
        output = {"input_type" :"boolean", "status" : 501}
        return jsonify(output)
