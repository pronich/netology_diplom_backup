from ya_class.yaLoader import yaUpLoader
from vk_class.vk_api import vk_api
import requests
from progress.bar import ChargingBar
import os
from pprint import pprint

class rezerv_vk:
    def __init__(self, user_id, ya_token, count):
        self.ya_token = ya_token
        self.user_id = user_id
        self.count = count
        self.ya_loader = yaUpLoader(self.ya_token)
        self.vkapi = vk_api(self._get_vk_token())

    def _get_vk_token(self):
        os_path = os.getcwd()
        vk_file = 'vk_token.txt'
        vk_from = os.path.join(os_path, vk_file)
        with open(vk_from, 'r') as vk_f:
            vk_token = vk_f.readline().strip()
        return vk_token

    def check_folder(self, path):
        status_code = self.ya_loader.check_folder(path)
        if status_code != 200:
            self.ya_loader.set_folder(path)
        return path

    def get_photo_from_vk(self, count):
        if count == '':
            upload_list = self.vkapi.get_max_size_photos(self.user_id)
        else:
            upload_list = self.vkapi.get_max_size_photos(self.user_id, count)
        return upload_list

    def upload_to_ya(self, upload_list):
        ya_load_to = input('\nВведите путь до папки на ya_disk: ')
        ya_load_to = self.check_folder(ya_load_to)

        print(f'\nЗагружаем файлы на YaDisk')
        bar = ChargingBar('Countdown', max=len(upload_list[1]))
        hash_map = {}
        for photo in upload_list[1]:
            bar.start()
            file_name = photo['file_name']
            if file_name in hash_map.keys():
                last_name = file_name
                value = hash_map[last_name] + 1
                file_name = file_name.split('.')[0] + '_' + str(value) + '.jpg'
                hash_map[last_name] = value
            else:
                hash_map[file_name] = 1

            ya_file_to = ya_load_to + '/' + file_name
            url = photo['url']

            res = requests.get(url).content
            self.ya_loader.upload(ya_file_to, res)
            bar.next()
        bar.finish()

    def rezerv_to_ya(self):
        upload_list = self.get_photo_from_vk(self.count)
        self.upload_to_ya(upload_list)
        pprint(upload_list[0])

