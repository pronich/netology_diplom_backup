import requests
from abstractClass import MediaUpLoader


class YaUpLoader(MediaUpLoader):
    def __init__(self, token):
        super().__init__(token)
        self.url = 'https://cloud-api.yandex.net:443/v1/disk/'
        self.headers = {'Content-Type': 'Application/json', 'Authorization': 'OAuth ' + self.token}

    def check_folder(self, path):
        url = self.url + 'resources/'
        params = {'path': path}
        resp = requests.get(url, params=params, headers=self.headers)
        if resp.status_code != 200:
            self.set_folder(path)
            return 'Set new folder'
        return '\nCheck folder complete'

    def set_folder(self, path):
        url = self.url + 'resources/'
        params = {'path': path}
        resp = requests.put(url, params=params, headers=self.headers)
        return resp.status_code

    def _get_path_by_file(self, path):
        url = self.url + 'resources/upload'
        params = {'path': path, 'overwrite': 'true'}
        resp = requests.get(url, params=params, headers=self.headers)
        return resp.json().get('href')

    def upload(self, path, data):
        href = self._get_path_by_file(path)
        response = requests.put(href, data=data)
        response.raise_for_status()
        pass
