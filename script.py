import json
import requests

cnt = 0

with open("egservice_bd.json", "r") as f:
    data = json.load(f)

    for index, element in enumerate(data):
        if index != 0:
            if element["name"] == "users":
                for task in element["data"]:
                    if task['company1'] == '1':
                        user_model_fields = {
                            'id': task['id'],
                            'email': task['email'],
                            'name': task['name'],
                            'surname': task['surname'],
                            'last_name': task['patronymic'],
                            'phone': task['phone'],
                            'address': task['address'],
                            'date_of_birth': str(task['birthDate'])[:10],
                            'date_of_start': str(task['startWorkDate'])[:10],
                            'inn': task['inn'],
                            'snils': task['snils'],
                            'passport': task['pasport'],
                            'post': task['position'],
                            'info_about_relocate': task['anotherDepartament'],
                            'attestation':task['certification'],
                            'qualification': task['trainingUp'],
                            'retraining': task['trainingProf'],
                            'status': task['status'],
                            'is_dark': '1',
                            'password': '1234',
                        }

                        print(json.dumps(user_model_fields))
                        res = requests.post('https://egs-back.ru/user/user-create/', data=user_model_fields)
                        print(res.status_code)

for i in range(100):
    if i != 66:
        res = requests.delete(f'https://egs-back.ru/user/users/{i}')
        print(res.status_code)
