from random import randrange
from json import dumps

SAVE_LOC="data.json"

def randID(data):
    id = '%030x' % randrange(16**30)
    if id not in data:
        return id
    randID(data)

if __name__ == "__main__":
    data = {}
    for i in range(100000):
        data[randID(data)] = '%030x' % randrange(16**30)

    print("saving...")
    with open(SAVE_LOC, 'w') as writer:
        writer.write(dumps(data))
        writer.close()
    
    print("finished")