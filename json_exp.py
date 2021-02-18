import json

dat =  {
    'type_trans'         : {
                'DS': 'Duvet',
                'BL': 'Blanket',
                'SS': 'Sheet Set'
    },
    'size_trans '        : {
                'TW': 'Twin',
                'FU': 'Full',
                'FQ': 'Full Queen',
                'QU': 'Queen',
                'KG': 'King',
                'CK': 'Cal King'
    },
    'color_trans'        : {
                '100': 'pink',
                '102': 'ivory',
                '019': 'grey',
                '410': 'navy',
                '090': 'fawn',
                '294': 'willow',
                '417': 'ltblue',
                '479': 'lilac',
                '638': 'blu'

    }
}

jas = json.dumps(dat)

with open('dict.json', 'w') as writer:
    # Alternatively you could use
    # writer.writelines(reversed(dog_breeds))

    # Write the dog breeds to the file in reversed order
    writer.write(jas)

with open('products.txt', 'r') as reader:
    # Note: readlines doesn't trim the line endings
    dog_breeds = reader.read().splitlines()
    print(dog_breeds)
    print(len(dog_breeds))


'''data = ''
jas = json.dumps(dat)
f = open("dict.json", "w")
print(jas)
f.write(jas)
f.close()

#print(js)
# Opening JSON file 
with open('dict.json') as json_file:
    data = json.load(json_file)
#   values = json.loads(js)
    print(data['color_trans'])

data['color_trans']['100'] = 'blue'
f = open("dict.json", "w")
js = json.dumps(data)
print(js)
f.write(js)
f.close()

with open('dict.json') as json_file:
    data = json.load(json_file)
#   values = json.loads(js)
    print(data['color_trans']['100'])'''