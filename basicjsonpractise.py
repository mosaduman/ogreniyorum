#test amacli yorumdur

import json

while True:
    fname = input("Enter file name: ")
    fh = open(fname)
    data = fh.read()
    print('Retrieved', len(data), 'characters')

    info = json.loads(data)
    item = info["comments"]
    print('Count:', len(item))
    y = 0
    for newitem in item:
        x = newitem["count"]
        y = x + y
    print('Sum:', y)
