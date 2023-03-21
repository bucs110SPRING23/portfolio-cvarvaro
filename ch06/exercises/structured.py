# Protocols
# - http
# - xml
# - json: javascript object notation
#   - string formats, not file formats
#   - int, float, string, bool, list, dictionary, None
#   - {}: dictionary, []: list
# 
# 

import json

data = {
    "num": 1,
    "msg": "Hello World",
}

json_string = json.dumps(data)
print(json_string, type(json_string))

json_data = json.loads(json_string)
for k, v in json_data.items():
    print(k, v)

fptr = open("data.json","w") # json is a convention not a file type
fptr.write(json_string)
fptr.close()

data_str = open("data.json", "r").read()
data = json.loads(data_str)
print(data, type(data))

