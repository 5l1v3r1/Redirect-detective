import requests
url =input("Enter URL You Want to Check : ")
r = requests.get(url)
for x in r.history:
    print(x.url, end="\n\n")
