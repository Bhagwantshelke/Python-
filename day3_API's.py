# import requests
#
# req_url = "https://jsonplaceholder.typicode.com/posts"
#
# responce = requests.get(url= req_url)
# json_data = responce.json()
# lst = []
# for x in responce.json():
#
#     if len(x.get("title").split()) <= 8:
#
#         print(x)
#
# request_url = "https://jsonplaceholder.typicode.com/comments"
# response = requests.get(url=request_url)
# json_resp = response.json()
# email_list = []
# for emails in json_resp:
#     email_list.append(emails['email'])
#     print(email_list)
#
# # import requests
# # req_url="https://jsonplaceholder.typicode.com/comments"
# # responce =requests.get(url=req_url,params={"postId":"5"})
# # data = responce.json()
# # for i in data:
# #     if i["name"].lower().count("e") >= 2:
# #
# #         print(i)
#
# # Post Request
#
# import requests
# import json
# request_url = "https://jsonplaceholder.typicode.com/posts"
# sample = {'title':"dau","body":"bar","usrId":1}
# string = json.dumps(sample)
# responce = requests.post(request_url,data=string,
#                          headers={'Content-type': 'application/json; charset=UTF-8'})
# print(responce.json())
#
#
# # dict1 = {    "name":"A",    "company": "B"}
# # tinyData = json.dumps(dict1)
# # # print(type(tinyData))
# # # print(tinyData)
# # response = requests.post('https://jsonplaceholder.typicode.com/posts',data=tinyData,
# #                          headers={'Content-type': 'application/json; charset=UTF-8'})
# # # print(response)
#
#
#
# import json
#
# import requests
# request_url = "https://jsonplaceholder.typicode.com/posts"
# sample = {'title':"dau","body":"bar","usrId":1}
# string = json.dumps(sample)
# responce = requests.post(request_url,data=string,
#                          headers={'Content-type': 'application/json; charset=UTF-8'})
# print(responce.json())
#
#
#
# # import requests
# # import json
# # api_url = "https://api.publicapis.org/random"
# # response = requests.get(api_url)
# # data = []
# # for i in range(0,5):
# #     response = requests.get(api_url).json()
# #     data.append(response)
# #     print(data)
#
#
# import requests
# base = "https://api.publicapis.org/"
# endpoint = "random"
# req_url = base+endpoint
# responce = requests.get(url=req_url)
# print(responce.json




