import requests
import json
import os

url = "http://localhost:8082/artifactory/api/search/aql"

headers = {
    'Authorization': 'Bearer eyJ2ZXIiOiIyIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYiLCJraWQiOiI1bjZUQmVhd2xXT2ZCV3NMeFhuUzJJOGI2Ui0wVC01TUswRVhSajFKdW84In0.eyJzdWIiOiJqZmZlQDAwMFwvdXNlcnNcL2FkbWluIiwic2NwIjoiYXBwbGllZC1wZXJtaXNzaW9uc1wvYWRtaW4gYXBpOioiLCJhdWQiOiIqQCoiLCJpc3MiOiJqZmZlQDAwMCIsImlhdCI6MTYyOTA1MzkwMCwianRpIjoiOGU1ZjFhYTQtZjMwMS00NDcyLWE0MjItMDU4Mjc2NWJkMWIxIn0.AXR0_owoIRgpZ6yBy8q6TElH9JyqPW4fvHEqZL4qeG_dVIsPV7Ii3CUxWuzn5Aa3LoenFjqC4ojBhb_dJyCWpXVxP24wxKtaKNo-huB9en2qPE0CtU4ZZ2QUwj7DThVQph0V0Sx_zl-AVIXK28jebJlZZ_UOiiGGNSk_QpePpueFHo0kJl7kxjgW2NAx4lEPD5Urf-bmt9Er6jX_aiEMvASY3QsOQLE0E-Ho1JSQ-Xtdh4iAW-oRyvqkt3FAMoxhGzEdie4rdD88cLri9Oh8nNzLHXlQJXAK90JMxMRxcTWHpscgkYSFdj7_PbF0JDWOApPoXtVmKu_5Lo63r3-gKQ',
    'Content-Type': 'text/plain'
}

# pathThreeImages = {'master','thiethaa/hello-world','thiethaa/my-company'}

pathFiveImages = {'master'}


def mainFunction (paths, totalRemove):
    for path in paths:
        payload = f"items.find(\n{{\n  \"repo\": \"example-local-docker\",\n  \"path\": {{\n    \"$match\": \"{path}\"\n  }},\n  \"name\": {{\n    \"$match\": \"SNAPSHOT_*\"\n  }},\n  \"type\": \"folder\"\n}}).sort({{\"$asc\" : [\"created\"]}})\n"
        print("\n------------------",path,"---------------------\n")

        response = requests.request("POST", url, headers=headers, data=payload)
        response_dict = json.loads(response.text)

        prettyJson = json.dumps(response_dict, indent=1)
        print(prettyJson)

        total = response_dict["range"]["total"]
        print('Total Artifact in the Repository::', total)

        remove = total - totalRemove
        print('Total Artifact to be Removed::', remove)

        if remove > 0:
            os.system('jfrog rt ping')
            cmd_search = f'jfrog rt s --spec=json-files/{path}.json --limit={remove}'
            cmd_delete = f'jfrog rt del --spec=json-files/{path}.json --limit={remove} --quiet=true'
            print("--------list of old images to be deleted::----------")
            os.system(cmd_search)
            os.system(cmd_delete)
        else:
            print('Nothing to Delete!')

# mainFunction(pathThreeImages,3)
mainFunction(pathFiveImages,5)