import requests

res=requests.get("http://localhost:1234/test_api",params={"num1":"2","num2":"7"})
json=res.json()

print(json["sum"])
