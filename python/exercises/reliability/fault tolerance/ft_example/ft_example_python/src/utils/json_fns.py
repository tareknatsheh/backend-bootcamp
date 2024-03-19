import json
from utils.random_err import gen_rand_err

def write_to_json(msg):
    with open('./data/journal.json','r+') as f:
        f.seek(0)
        content = f.read()
        content = json.loads(content)
        content.append(msg)
        f.seek(0)        
        json.dump(content,f)
        f.truncate()
        
def read_from_json(database_filename):
    # read from json, but fail 50% of the time
    with open(f'./data/{database_filename}') as f:
        gen_rand_err()
        print(f.read())
        return 