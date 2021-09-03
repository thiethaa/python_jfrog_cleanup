import requests
import json
import os
from dotenv import load_dotenv

# pip install -r requirements.txt
master = {'master' }

# request to get all the artifact inside particular repo path
url = "http://localhost:8082/artifactory/api/search/aql"
payload = "items.find(\n{\n  \"repo\": \"firmware-snapshot-local\",\n  \"path\": {\n    \"$match\": \"driverx/fwex\"\n  },\n  \"$and\":[\n  {\"name\": {\n    \"$nmatch\": \"107-02-001\"\n  }},\n   {\"name\": {\n    \"$nmatch\": \"107-02-002\"\n  }},\n    {\"name\": {\n    \"$nmatch\": \"107-02-003\"\n  }}\n  ],\n  \"type\": \"folder\"\n}).sort({\"$asc\" : [\"created\"]})\n\n"

load_dotenv()
token = os.environ.get('SECRET_TOKEN')
print("token:::", token)
headers = {
    'Authorization': f'{token}',
    'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)
response_dict = json.loads(response.text)

total = response_dict["range"]["total"] + 3
print('total artifact in the repository::', total)

remove = total - 5
print('total artifact to be removed::', remove)

if remove > 0:
    os.system('jfrog rt ping')
    cmd = f'jfrog rt del --spec=json-files/master.json --limit={remove} --dry-run --quiet=true'
    os.system(cmd)
else:
    print('nothing to delete!')
