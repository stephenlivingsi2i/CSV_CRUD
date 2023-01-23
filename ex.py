import json
import requests
import pandas as pd

print("hello")

payload = {

    "Firstname":"livings"

}

'''update a particular employee'''

respon = requests.put("http://127.0.0.1:8000/updateEmployee/1002/Firstname/", data=payload)
print(respon)


'''add a new employee row into csv file'''

respon = requests.post("http://127.0.0.1:8000/addEmployee/", data=payload)
print(respon)


'''get all employee rows from csv file'''

respon = requests.get("http://127.0.0.1:8000/getEmployees/")
print(respon)
