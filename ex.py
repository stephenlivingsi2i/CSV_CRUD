import json
import requests
import pandas as pd

# header = {
#     "content-Type":"application/json"
# }

payload = {

    "Firstname":"livings"

}


respon = requests.put("http://127.0.0.1:8000/updateEmployee/1002/Firstname/", data=payload)
print(respon)
