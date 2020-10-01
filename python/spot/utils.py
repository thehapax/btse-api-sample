import ujson

def is_json(myjson):
    try:
        json_object = ujson.loads(myjson)
    except ValueError as e:
        return False
    return True


