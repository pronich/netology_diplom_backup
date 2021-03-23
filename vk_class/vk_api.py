import requests
from pprint import pprint
import time
from progress.bar import ChargingBar

class Vk_api:
    def __init__(self, token, version = None):
        self.token = token
        self.version = version
        if self.version is None:
            self.version = '5.130'
        self.params = {
            'access_token': self.token,
            'v': self.version
        }
        self.url = 'https://api.vk.com/method/'
        resp = requests.get(self.url+'users.get', self.params)
        if resp.status_code == 200:
            self.owner_id = resp.json()['response'][0]['id']
        else:
            pprint('Ошибка получения Owner_id, проверьте токен')

    def _get_all_photos(self, user_id, count):
        photos_params = {
            'album_id': 'profile',
            'owner_id': user_id,
            'photo_sizes': 1,
            'extended': 1,
            'count': count
        }
        resp = requests.get(self.url+'photos.get', params={**self.params, **photos_params})
        if 'response' in resp.json().keys():
            return resp.json()
        else:
            print('Ошибка получения фото')

    def get_max_size_photos(self, user_id = None, count=5):
        if user_id is None:
            user_id = self.owner_id
        all_photos = self._get_all_photos(user_id, count)
        # pprint(all_photos)
        json_file = []
        photo_list = []
        print('\nПолучаем фотографии максимального размера из VK')
        bar = ChargingBar('Countdown', max=len(all_photos['response']['items']))
        for photo in all_photos['response']['items']:
            photo_name = str(photo['likes']['count'])+'.jpg'
            photo_size = photo['sizes'][len(photo['sizes'])-1]['type']
            json_file.append({'file_name': photo_name, 'size': photo_size})
            photo_list.append({'file_name': photo_name, 'url': photo['sizes'][len(photo['sizes'])-1]['url']})
            bar.next()
            time.sleep(0.1)
        bar.finish()

        return [json_file, photo_list]