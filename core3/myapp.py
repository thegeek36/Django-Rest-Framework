import  requests
import json
URL = "http://127.0.0.1:8000/stuapi/"

# data = {
#     'name': "Mohit",
#     'roll': 108,
#     'city':'Kolkata'
# }
#Convert the python data into json data to send to the server.
# json_data = json.dumps(data)
# req = requests.post(url = URL,data = json_data)
# data = req.json()
# print(data)

def get_data(id = None):
    data ={}
    if id is not None:
        data = {'id':id}
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(data)
    req = requests.get(url = URL,headers = headers,data = json_data)
    data = req.json()
    print(data)

#get_data()

def post_data():
    data = {
    'name': 'Ridhiman',
    'roll': 161,
    'city':'Rourkela'
    }
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(data)  
    r = requests.post(url = URL,headers = headers ,data = json_data)
    data = r.json()
    print(data)

#post_data()

def update_data():
    data = {
    'id':8,
    'name': "Priyanka Mishra",
    'roll':129,
    'city':'Sambalpur'
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL,data = json_data)
    data = r.json()
    print(data)

#update_data()

def delete_data():
    data = {
    'id':10
    }
    json_data = json.dumps(data)
    r = requests.delete(url = URL,data = json_data)
    data = r.json()
    print(data)

delete_data()