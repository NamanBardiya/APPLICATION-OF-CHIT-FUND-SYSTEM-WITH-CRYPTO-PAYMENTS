import hashlib
import json

def crypto_hash(*args):
    """
    for generating sha 256 hash value of a given arguments...
    """
    stringified_args= sorted(map(lambda data: json.dumps(data), args))
    '''
    print(f"intial arguments: {stringified_args}")
    '''
    joined_data=''.join(stringified_args)
    '''
    print(f"joined_data: {joined_data}")
    '''
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(crypto_hash('one',2,[3]))
    print(crypto_hash(2,'one',[3]))

if __name__ == '__main__':
    main()

