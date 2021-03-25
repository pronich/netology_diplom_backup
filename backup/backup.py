from yaLoader import YaUpLoader
from vk_api import VkApi
import requests
from progress.bar import ChargingBar


class BackupVk:
    def __init__(self, user_id, ya_token, count=None):
        self.ya_token = ya_token
        self.user_id = user_id
        self.count = count

    def get_photo_from_vk(self):
        vk_obj = VkApi()
        if self.count is None:
            upload_list = vk_obj.get_max_size_photos(self.user_id)
        else:
            upload_list = vk_obj.get_max_size_photos(self.user_id, self.count)
        return upload_list

    def upload_to_ya(self, upload_list):
        ya_obj = YaUpLoader(self.ya_token)
        ya_load_to = input('\nВведите путь до папки на ya_disk: ')
        print(ya_obj.check_folder(ya_load_to))

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
            ya_obj.upload(ya_file_to, res)
            bar.next()
        bar.finish()
