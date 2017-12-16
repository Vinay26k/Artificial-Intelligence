import json

f = open("tweetjson.txt",'r').read()
data = json.loads(f)
print(json.dumps(data, indent=4, sort_keys=True))
print(data['user']['screen_name'])
