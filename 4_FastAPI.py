# from fastapi import FastAPI
# app = FastAPI()
#
# @app.get("/sample")
# def hello():
#     return {
#         "name":"Bhagwant",
#         "Address":"Pune"
#     }
# @app.post("/sample")
# def hello():
#     return "hello bro!"

#
# from fastapi import FastAPI
# import random
# app = FastAPI()
# @app.get("/")
# def hello():
#     random_number_list = []
#     for i in range(10):
#         num = random.randrange(0, 10)
#         random_number_list.append(num)
#         return random_number_list


from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def get_hello():
    list1 = [3, 5, 6, 7, 9, 2]
    return list1


