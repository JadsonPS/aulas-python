import requests 
url = 'https://api.covid19api.com/dayone/country/brazil'

resp = requests.get(url)
raw_data = resp.json()
print(resp)


print()
