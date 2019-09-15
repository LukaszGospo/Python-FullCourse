import json

data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

data = '''[
    {
        "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    }, 
    {
        "id" : "002",
        "x" : "7",
        "name" : "Chuck"
    }
]'''

info = json.loads(data)
for item in info:
    print(item['id'])

lista=list()

dir = dict()

dir["id"] = 5
dir["name"]="Gospo"
lista.append(dir)

fhand = open('jexample.json')

lista=json.load(fhand)

print(lista)