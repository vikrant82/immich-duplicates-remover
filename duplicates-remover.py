import requests
import json as json

#1 - Define your base URL
BASE_URL = "https://baseurl"
API_DUPLICATE_URL = "{}/api/duplicates".format(BASE_URL)
ASSETS_URL = "{}/api/assets".format(BASE_URL)
SKIP_VIDOES = True

#2 - Copy the token from cookies in the browser
TOKEN = ""

def getHeaders():
    headers = {
    'Cookie': 'immich_access_token='+TOKEN,
    'accept': '*/*',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }
    return headers


def getDuplicates():
    x = requests.request("GET", API_DUPLICATE_URL, headers=getHeaders())
    countDeleted = 0
    if x.status_code == 200:
        duplicates = x.json()
        print ("Total duplicates : " + str(len(duplicates)))
        countDone = 0
        for duplicate in duplicates:
            countDone += 1
            if (countDone % 100 == 0):
                print ("Done: " +str(countDone))
            assets = duplicate['assets']
            max_size = 0
            selected_asset = None
            for asset in assets:
                if SKIP_VIDOES and asset['type'] != 'IMAGE':
                    break
                if asset["exifInfo"]["fileSizeInByte"] > max_size:
                    selected_asset = asset
                    max_size = asset["exifInfo"]["fileSizeInByte"]
            ids_delete = []
            ids_duplicate = []
            for asset in assets:
                if SKIP_VIDOES and asset['type'] != 'IMAGE':
                    break
                ids_duplicate.append(asset["id"])
                if asset != selected_asset:
                    ids_delete.append(asset["id"])

            if len(ids_duplicate) > 0:
                payloa_put = json.dumps({
                    "ids": ids_duplicate,
                    "duplicateId": None
                })

                resolve_duplicate = requests.request("PUT", ASSETS_URL, headers=getHeaders(), data=payloa_put)
                print ("\nDuplicates resolve:" + str(resolve_duplicate.status_code) + ":" + ','.join(ids_duplicate))

            if len(ids_delete) > 0:
                payload =  json.dumps({
                    "ids": ids_delete,
                    "force": False
                })
                countDeleted = countDeleted + len(ids_delete)
                delete = requests.request("DELETE", ASSETS_URL, headers=getHeaders(), data=payload)
                print ("Delete:" + str(delete.status_code) + ":" + ','.join(ids_delete))
        
        print ("Total deleted : " + str(countDeleted))
    else:
        print (str(x.status_code) + ": Check your token.")

if __name__ == '__main__':
    getDuplicates()