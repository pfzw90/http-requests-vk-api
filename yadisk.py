import requests, os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""

        HEADERS = {"Authorization" : f'OAuth {self.token}'}

        response_url = requests.get(
        "https://cloud-api.yandex.net/v1/disk/resources/upload",
        params = {"path": file_path} ,
        headers = HEADERS)
       
        url = response_url.json()['href']
        response_upload = requests.put(url)
        return print(response_upload)


if __name__ == '__main__':
    uploader = YaUploader('AgAAAAAZDE4_AADLW8SH5kQzi0XkkSd4mUG10Eo')
    result = uploader.upload('\files-to-upload\art5.jpg')