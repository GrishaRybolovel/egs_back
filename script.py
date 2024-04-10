import json
import requests

cnt = 0

with open("egservice_bd.json", "r") as f:
    data = json.load(f)

    for index, element in enumerate(data):
        if index != 0:
            if element["name"] == "tasks":
                for task in element["data"]:

                    new_dict = {
                        "name": task["name"],
                        "description": "-",
                        "author": task["ownerId"],
                        "completion": task["date"][0:10],
                        "done": task["closedDate"],
                        "project": task["objectId"],
                    }

                    print(json.dumps(new_dict))
                    res = requests.post('https://egs-back.ru/task/tasks/', data=new_dict)
                    print(res.status_code)
