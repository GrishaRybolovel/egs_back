import json
import requests

cnt = 0

with open("egservice_bd.json", "r") as f:
    data = json.load(f)

    for index, element in enumerate(data):
        if index != 0:
            if element["name"] == "users":
                for user in element["data"]:
                    print(user)
                    new_dict = {}
                    new_dict['email'] = user['email']
                    new_dict['name'] = user['name']
                    new_dict['surname'] = user['surname']
                    new_dict['last_name'] = user['patronymic']
                    new_dict['phone'] = user['phone']
                    new_dict['address'] = user['address']
                    new_dict['date_of_birth'] = user['birthDate'][0:10]
                    new_dict['date_of_start'] = user['startWorkDate'][0:10]
                    new_dict['inn'] = user['inn']
                    new_dict['snils'] = user['snils']
                    new_dict['passport'] = user['pasport']
                    new_dict['post'] = user['position']
                    new_dict['info_about_relocate'] = user['anotherDepartament']
                    new_dict['attestation'] = user['certification']
                    new_dict['qualification'] = user['trainingUp']
                    new_dict['retraining'] = user['trainingProf']
                    new_dict['status'] = user['status'] == '1'
                    new_dict['password'] = '1234'

                    print(json.dumps(new_dict))


                    res = requests.post('https://egs-back.ru/user/register/', data=new_dict)
                    print(res.status_code)