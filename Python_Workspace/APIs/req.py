import requests

res=requests.get("https://api.exchangeratesapi.io/latest",params={"base":"INR"})
json=res.json()

print(json['rates']['USD'])
