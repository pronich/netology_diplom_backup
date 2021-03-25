from backup import BackupVk
from pprint import pprint
import configparser


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("settings.ini")

    ya_token = config['YA']['token']

    user_id = input('Введите user_id или короткое имя пользователя VK: ')
    count = input('Введите количество фотографий для загрузки: ')

    if count == '':
        count = None

    backup = BackupVk(user_id, ya_token, count)
    upload_list = backup.get_photo_from_vk()
    backup.upload_to_ya(upload_list)
    pprint(upload_list[0])
