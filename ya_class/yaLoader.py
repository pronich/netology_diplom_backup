import requests
import os


class YaUpLoader:
    def __init__(self, token):
        self.token = token
        self.url = 'https://cloud-api.yandex.net:443/v1/disk/'

    def headers(self):
        return {'Content-Type': 'Application/json', 'Authorization': 'OAuth ' + self.token}

    def _get_path_by_file(self, path):
        url = self.url + 'resources/upload'
        headers = self.headers()
        params = {'path': path, 'overwrite': 'true'}
        resp = requests.get(url, params=params, headers=headers)
        return resp.json()

    def upload(self, file_to, data):
        href = self._get_path_by_file(file_to).get('href')
        response = requests.put(href, data=data)
        response.raise_for_status()
        # if response.status_code == 201:
        pass

    def check_folder(self, path):
        url = self.url + 'resources/'
        headers = self.headers()
        params = {'path': path}
        resp = requests.get(url, params=params, headers=headers)
        return resp.status_code

    def set_folder(self, path):
        url = self.url + 'resources/'
        headers = self.headers()
        params = {'path': path}
        resp = requests.put(url, params=params, headers=headers)
        return resp.status_code
