import functions_framework
import random
from flask import jsonify


@functions_framework.http
def is_valid_input(request):
    #request_json = request.get_json()
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
            #return HTTPException(status_code=status.HTTP_200_OK,
                                #detail=f'message: success')
            #return status_code #HTTPException(status_code=status.HTTP_200_OK,
                                #detail=f'message: success')
        else:
            output = {"input_type" :"given alphabet", "status" : 405}
            return jsonify(output)
            #return HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                                #detail=f'message: {type(x)} is not allowed')
            #return status_code

    elif flag1 == 1:
        output = {"input_type" :"float", "status" : 400}
        return jsonify(output)
        #return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            #detail=f'message: error')
        #return status_code
    elif flag1 == 2:
        output = {"input_type" :"boolean", "status" : 501}
        return jsonify(output)
        #return HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED,
                            #detail=f'message: input is a boolean  ')
