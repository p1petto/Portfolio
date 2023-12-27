import json
import requests

lang_url = "https://translate.api.cloud.yandex.net/translate/v2/translate"
FOLDER_ID = "b1gtf3dqupicap0o7l1v"

token = "t1.9euelZrPnZmbjcyRz46Vl5TIxozNnu3rnpWais-QkJ7OlZOcic6Llpaenprl9PdgUQBj-e8cSSPj3fT3IAB-YvnvHEkj4w.3aKdh7Kx8ZQvyQl8NGwM1FmEAYorfJ7RzemlEf1stxu89EY3F0lacBMAgdes46KTiH1UAhl5n2mOdPYxa_9WDg"
lang_headers= {"Authorization": "Bearer " + token}

post_data = {"folderId": FOLDER_ID, "lang": "en-US"}
file = json.load(open("body.json", "r"))

input = open("text.txt", "r", encoding="UTF-8")
for_translation = [line[:-1] for line in input]

for i in for_translation:
    file['texts'] = i
    response = requests.post(lang_url, headers=lang_headers,  json=file)
    print(response.text)


