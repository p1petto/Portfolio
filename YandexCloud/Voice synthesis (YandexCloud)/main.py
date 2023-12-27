import argparse
import requests


def synthesize(folder_id, iam_token, text):
   url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
   headers = {
       'Authorization': 'Bearer ' + iam_token,
   }

   data = {
       'text': text,
       'lang': 'ru-RU',
       'voice': 'filipp',
       'folderId': folder_id
   }

   with requests.post(url, headers=headers, data=data, stream=True) as resp:
       if resp.status_code != 200:
           raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))

       for chunk in resp.iter_content(chunk_size=None):
           yield chunk

if __name__ == "__main__":
    FOLDER_ID = "b1gtf3dqupicap0o7l1v"
    token = "t1.9euelZqSjp7NzJucyp6QjcuUm82Kle3rnpWais-QkJ7OlZOcic6Llpaenprl8_cYQFti-e98aikk_N3z91huWGL573xqKST8.tV0Ncjnvyy3_5IRm0WwpkA3lDvSAkS7b6XVzjmPeaN80boQ_JujQZU_Qq2usPvboTFzct92hl6Eu2LQtgSsDBA"
    text = open("text.txt", "r", encoding="UTF-8").readline()

with open("output.ogg", "wb") as f:
    for audio_content in synthesize(FOLDER_ID, token, text):
        f.write(audio_content)



