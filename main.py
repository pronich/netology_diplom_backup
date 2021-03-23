from rezerv_copy_vk.rezerv_class import Rezerv_vk


if __name__ == '__main__':

    user_id = input('Введите user_id или короткое имя пользователя VK: ')
    ya_token = input('Введите токен от яндекс.диск: ')
    count = input('Введите количество фотографий для загрузки: ')

    rezerv = Rezerv_vk(user_id, ya_token, count)
    rezerv.rezerv_to_ya()