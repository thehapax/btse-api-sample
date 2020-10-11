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


def get_base(symbol):
    pairs = symbol.split('-')
    return pairs[0]

def get_quote(symbol):
    pairs = symbol.split('-')
    return pairs[1]


# 'symbol': 'BTC-USD', 
if __name__ == "__main__":
    symbol = 'BTC-USD'    
    print(symbol)
    base = get_base(symbol)
    print(base)
    quote = get_quote(symbol)
    print(quote)
    
    
    
    