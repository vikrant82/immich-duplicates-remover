import json

file = '../orphans.json'

def getDuplicates():
    with open(file) as f:
        d = json.load(f)
        print ("'")
        for element in d:
            id = element['entityId']
            print (id, end ="','")

if __name__ == '__main__':
    getDuplicates()