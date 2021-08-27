import json
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
data_a = json.dumps(data)
data_b = json.loads(data_a)
#print("data_b的长度=============>",len(data_b.get('RECORDS')))
old_data = data_b.get('RECORDS');
new_json_header = {
    "clockSourceId": "0008DEFFFE0006BB",
    "comments": "",
    "defaultZ": 0.65,
    "properties":{

    }
}
new_json_header_b = json.loads(json.dumps(new_json_header))
print(new_json_header_b.get("properties"))
for index in range(len(old_data)):

    print (index, '--------------数据----------------- : %s' % old_data[index])