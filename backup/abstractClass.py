from abc import abstractmethod


class MediaUpLoader:
    def __init__(self, token):
        self.token = token

    @abstractmethod
    def check_folder(self, path):
        pass

    @abstractmethod
    def set_folder(self, path):
        pass

    @abstractmethod
    def upload(self, path, data):
        pass


class MediaLoader:
    def __init__(self):
        pass

    @abstractmethod
    def get_all_photo(self, user_id, count=5):
        pass

    @abstractmethod
    def get_user(self, user_id):
        pass
