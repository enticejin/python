# import json
# data = [{'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' :  5}]
# json = json.dumps(data)
# print(json)

# import json
# print(json.dumps({"a": "Rumboo", "b" : 7}, sort_keys=True, indent=4, separators=(",", ": ")))

import json
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
text = json.loads(jsonData)
print(text)
