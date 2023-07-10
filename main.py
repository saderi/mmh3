import mmh3
import requests
import codecs
import sys
import urllib3


if len(sys.argv) < 2:
    print("URL is empty")
    exit(1)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
response = requests.get(sys.argv[1], verify=False)
favicon = codecs.encode(response.content,"base64")
mmh_hash = mmh3.hash(favicon, signed=False)
mmh_hash2 = mmh3.hash(favicon)


print(mmh_hash)
print(mmh_hash2)

