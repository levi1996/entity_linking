import requests, json
# myjson = { "text": "Obama will visit Germany and have a meeting with Merkel tomorrow.", "spans": [{"start":0,"length":5}, {"start":17,"length":7}, {"start":49,"length":6}]  }
myjson = { "text": "Japan and China is two contries", "spans": []  }
requests.post("http://localhost:5555", json=myjson)

def create_training_data(json_data):
    with open(json_data, 'r', encoding='utf-8') as f:
        data= json.load(f)
        f.close()