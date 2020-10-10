import requests, os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""

        file_path = os.path.normpath(file_path)
        HEADERS = {"Authorization" : f'OAuth {self.token}'}
        FILES = {"file" : open(file_path, 'rb')}

        response_url = requests.get(
        "https://cloud-api.yandex.net/v1/disk/resources/upload",
        params = {"path": file_path} ,
        headers = HEADERS)
        url = response_url.json().get('href')


        response_upload = requests.put(url, files = FILES, headers = {})
        return print(response_upload.status_code)


if __name__ == '__main__':
    uploader = YaUploader('XXX')
    result = uploader.upload("files-to-upload/test/art10.jpg")