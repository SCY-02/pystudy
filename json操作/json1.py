import json

def jsons():
    with open('json.json', 'r', encoding='UTF-8') as jsonfile:
        json_string = json.load(jsonfile)
        table = json_string['table']['field']
        fo = open('json1.txt', 'w', encoding='UTF-8')
        ls = list()
        for i in table:
            fo.write(i['tableId']+',')
            ls.append(i['tableId'])
        fo.close()
        return ls
def wf(json):
    fo = open('json.txt','w',encoding='UTF-8')
    print(json)
    fo.write(str(json))
    fo.close()


if __name__ == '__main__':
    wf(jsons())


















