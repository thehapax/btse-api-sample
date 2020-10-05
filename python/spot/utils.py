import ujson
'''
def is_json(myjson):
    try:
        json_object = ujson.loads(myjson)
    except ValueError as e:
        return False
    return True
'''

# check if the string  is a json
def is_json(myjson):
    try:
        json_object = ujson.loads(myjson)
        if json_object:
            return True
    except ValueError:
        return False

