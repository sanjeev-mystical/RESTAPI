import os
import requests
import json

AUTH_ENDPOINT = "http://localhost:8000/api/auth/"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "/refresh"


image_path = os.path.join(os.getcwd(), "IMG_20170226_185004.jpg")

headers = {
    'content-type': 'application/json',
}
data = {
    "username": 'restapi',
    "password": 'admin@123'
}
r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()['token']
print(token)

BASE_ENDPOINT = "http://localhost:8000/api/status/"
ENDPOINT = BASE_ENDPOINT + "27/"

headers2 = {
    # "content-type": 'application/json',
    "Authorization": "JWT " + token
}
data2 = {
    'content': 'This new Content',
}
with open(image_path, 'rb') as image:
    file_data = {
        "image": image
    }
    response = requests.get(ENDPOINT, headers=headers2, files=file_data)
    print(response.text)
    # r = requests.post(BASE_ENDPOINT, data=data2, headers=headers2, files=file_data)
    # print(r.text)

# AUTH_ENDPOINT = "http://localhost:8000/api/auth/register"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "/refresh"
# ENDPOINT = "http://localhost:8000/api/status/"
#
# image_path = os.path.join(os.getcwd(), "IMG_20170226_185004.jpg")
#
# headers = {
#     'content-type': 'application/json',
#     "Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNCwidXNlcm5hbWUiOiJuZXd1c2VyMTUiLCJleHAiOjE1ODU2NzYyMzcsImVtYWlsIjoibmV3dXNlcjE1QGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTg1Njc1OTM3fQ.oOFHGPSKD26H39ZKky9uz2MOCt6g8HM1LAYkwmKlOlA',
# }
# data = {
#     "username": 'newuser15',
#     "email": 'newuser15@gmail.com',
#     "password": 'admin@123',
#     "password2": 'admin@123'
# }
# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# token = r.json() #['token']
# print(token)

# refresh_data = {
#     'token': token
# }
#
# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json() #['token']
# print(new_token)
# headers = {
#     #'content-type': 'application/json',
#     "Authorization": "JWT " + token,
# }
#
# with open(image_path, 'rb') as image:
#     file_data = {
#         "image": image
#     }
#     data={
#         'content': "updated description"
#     }
#
#     json_data = json.dumps(data)
#     posted_response = requests.put(ENDPOINT + str(23) + "/", data=data, headers=headers, files=file_data)
#     print(posted_response.text)
#
# headers = {
#     #'content-type': 'application/json',
#     "Authorization": "JWT " + token,
# }
#
# data={
#     'content': "updated description"
# }
#
# json_data = json.dumps(data)
# posted_response = requests.put(ENDPOINT + str(23) + "/", data=data, headers=headers)
# print(posted_response.text)


# get_endpoint = ENDPOINT + str(12)

# r = requests.get(get_endpoint)
# print(r.text)
# r2 = requests.get(ENDPOINT)
# print(r2.status_code)
# post_headers = {
#     'content-type': 'application/json'
# }
#
# post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
# print(post_response.text)
# def do_img(method='get', data={}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if image_path is not None:
#         with open(image_path, 'rb') as image:
#             file_data = {
#                 "image": image
#             }
#             r = requests.request(method, ENDPOINT, data=data, headers=headers, files=file_data)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r
#
#
# do_img(method='put', data={'id': 14, "user": 1, "content": "some wow content"}, is_json=False, img_path=image_path)
#
#
# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r

# do(data={'id': 50})
# do(method='delete', data={'id': 4})
# do(method='put', data={'id': 7, "content": "some cool new content", 'user': 1})
# do(method='post', data={"content": "some cool new content", 'user': 1})
