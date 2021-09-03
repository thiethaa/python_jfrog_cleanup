import requests
import json
import os

url = "https://thiethaa.jfrog.io/artifactory/api/search/aql"

payload = '''
items.find(
      {
        "repo": "default-docker-local",
        "path": {
          "$match": "thiethaa/demo1"
        },
        "name": {
          "$match": "SNAPSHOT.*"
        },
        "type": "folder"
      }).include("name", "repo","path")
'''
print (payload)
# headers = {
#     'Content-Type': 'text/plain',
#     'Authorization': 'Bearer eyJ2ZXIiOiIyIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYiLCJraWQiOiJ1RmdMYkV6RlhVQUZXYkhMcUcxNmJmVE9SSmhBdHJuSEM1V3RueUdYc1drIn0.eyJzdWIiOiJqZmZlQDAwMFwvdXNlcnNcL3RyaXl1bGlhbmEudGhpZUBnbWFpbC5jb20iLCJzY3AiOiJhcHBsaWVkLXBlcm1pc3Npb25zXC9hZG1pbiBhcGk6KiIsImF1ZCI6ImpmcnRAKiIsImlzcyI6ImpmZmVAMDAwIiwiaWF0IjoxNjIyMzkyODI2LCJqdGkiOiJmZGM4NTJmNi1hNzg5LTRhZDUtYTBmMi0yYmYzNjEwYmJkMzQifQ.lU1YB-mLJrISvQbcvmxqG3GWFoOMer3INkP6c44Eb--kOBKk6j43vk0ob_Lg0BDlaGW-N86OuqtxjW_ujqMdXE6Vr2c2qry8yPQWTMN7Dz01cNEeenKcvqh7hj0rWVZegkRuHRW6RFsIyZ-AEmuAoBE0jief-36JtlO616WFDC8LyZJeLYsaPb_Hzirova_k8iXGQ4bqHxUXQXIOOQuNPVMDQf-4MxCLrkbUPJ9PwJ6FF6YOVxvJb2ZQ2g15LdP0a4IjHXTEvQ79E7XFtRSDulfxyMnO8Oe1MthVNtcwfHNIZqV1Q2vtravBuVAJPAHa5o_UzsLcm9HtGodyBEsu8w'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload)
#
# response_dict = json.loads(response.text)
# print(response_dict)
#
# total = response_dict["range"]["total"]
# print('total artifact in the repository::', total)
#
# remove = total - 3
# print('total artifact to be removed::', remove)
#
# if remove > 0:
#     os.system('jfrog rt ping')
#     cmd = f'jfrog rt del --spec=thiethaaDemo1.json --limit={remove} --dry-run --quiet=true'
#     os.system(cmd)
# else:
#     print('nothing to delete!')
