import requests
import json

BASE_URL = " http://127.0.0.1:8000/"
End_Point = "api/updates/"


def get_list(id=None):
    data = json.dumps({})
    if id is not None:
        data = json.dumps({'id': id})
    r = requests.get(BASE_URL + End_Point, data=data)
    print(r.status_code)
    status_code = r.status_code
    if status_code != 200:
        print('probably not a good sign')
    data = r.json()
    return data


def create_update():
    new_data = {
        "user": 1,
        "content": "Another New Update"
    }
    r = requests.post(BASE_URL + End_Point, data=json.dumps(new_data))
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


print(get_list())


# print(create_update())

def do_obj_update():
    new_data = {
        "id": 1,
        "content": "Some New data updated"
    }
    r = requests.put(BASE_URL + End_Point, data=json.dumps(new_data))
    # new_data = {
    #     "id": 1,
    #     "content": "Another New Update"
    # }
    # r = requests.put(BASE_URL + End_Point, data=new_data)
    # print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


def do_obj_delete():
    new_data = {
        "id": 1
    }
    r = requests.delete(BASE_URL + End_Point, data=json.dumps(new_data))
    # new_data = {
    #     "id": 1,
    #     "content": "Another New Update"
    # }
    # r = requests.put(BASE_URL + End_Point, data=new_data)
    # print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

# print(do_obj_update())
# print(do_obj_delete())
