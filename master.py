import requests
import json
import os

master = {'master' }

# request to get all the artifact inside particular repo path
url = "http://localhost:8082/artifactory/api/search/aql"


payload = "items.find(\n{\n  \"repo\": \"firmware-snapshot-local\",\n  \"path\": {\n    \"$match\": \"driverx/fwex\"\n  },\n  \"$and\":[\n  {\"name\": {\n    \"$nmatch\": \"107-02-001\"\n  }},\n   {\"name\": {\n    \"$nmatch\": \"107-02-002\"\n  }},\n    {\"name\": {\n    \"$nmatch\": \"107-02-003\"\n  }}\n  ],\n  \"type\": \"folder\"\n}).sort({\"$asc\" : [\"created\"]})\n\n"


print (payload)

headers = {
    'Authorization': 'Bearer eyJ2ZXIiOiIyIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYiLCJraWQiOiI1bjZUQmVhd2xXT2ZCV3NMeFhuUzJJOGI2Ui0wVC01TUswRVhSajFKdW84In0.eyJzdWIiOiJqZmZlQDAwMFwvdXNlcnNcL2FkbWluIiwic2NwIjoiYXBwbGllZC1wZXJtaXNzaW9uc1wvYWRtaW4gYXBpOioiLCJhdWQiOiIqQCoiLCJpc3MiOiJqZmZlQDAwMCIsImlhdCI6MTYyOTA1MzkwMCwianRpIjoiOGU1ZjFhYTQtZjMwMS00NDcyLWE0MjItMDU4Mjc2NWJkMWIxIn0.AXR0_owoIRgpZ6yBy8q6TElH9JyqPW4fvHEqZL4qeG_dVIsPV7Ii3CUxWuzn5Aa3LoenFjqC4ojBhb_dJyCWpXVxP24wxKtaKNo-huB9en2qPE0CtU4ZZ2QUwj7DThVQph0V0Sx_zl-AVIXK28jebJlZZ_UOiiGGNSk_QpePpueFHo0kJl7kxjgW2NAx4lEPD5Urf-bmt9Er6jX_aiEMvASY3QsOQLE0E-Ho1JSQ-Xtdh4iAW-oRyvqkt3FAMoxhGzEdie4rdD88cLri9Oh8nNzLHXlQJXAK90JMxMRxcTWHpscgkYSFdj7_PbF0JDWOApPoXtVmKu_5Lo63r3-gKQ',
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
