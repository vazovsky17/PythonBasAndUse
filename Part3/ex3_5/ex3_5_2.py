import requests
import json

client_id = 'my_secret_id'
client_secret = 'my_secret_code'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

json_file = json.loads(r.text)
token = json_file['token']
headers = {"X-Xapp-Token": token}

with open('file1.txt', 'r') as f:
    pairs = {}
    for line in f:
        r = requests.get(f'https://api.artsy.net/api/artists/{line.strip()}', headers=headers)
        j = json.loads(r.text)
        pairs[j['sortable_name']] = j['birthday']
print(*sorted(pairs, key=lambda x: pairs[x]), sep='\n')
