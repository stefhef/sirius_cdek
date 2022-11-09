import vk_api
import requests
import re
from constants import VK_PASSWORD, VK_LOGIN, VK_API_VERSION, LAST_MAX_ID, VK_TOKEN
from exeptions import MissingVariables, AuthorizationError, RequestFailed


class VkClient:
    vk: vk_api.vk_api.VkApiMethod = None
    token: str = None
    vk_api_version: str = None

    def __init__(self):

        if not any((VK_LOGIN, VK_PASSWORD)):
            return
        self.authorization_login_password(login=VK_LOGIN, password=VK_PASSWORD)  # Ну типа надо

    def authorization_login_password(self, login, password):
        """Авторизация с использованием логина или пароля"""
        vk_session = vk_api.VkApi(login=login,
                                  password=password,
                                  captcha_handler=self.captcha_handler,
                                  auth_handler=self.auth_handler)
        vk_session.auth()
        self.token = vk_session.token.get("access_token", None)  # Странный токен
        self.vk_api_version = vk_session.api_version
        self.vk = vk_session.get_api()  # Возможно уже не надо, но да ладно

    @staticmethod
    def captcha_handler(captcha):
        """ При возникновении капчи вызывается эта функция и ей передается объект
            капчи. Через метод get_url можно получить ссылку на изображение.
            Через метод try_again можно попытаться отправить запрос с кодом капчи
        """

        key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

        # Пробуем снова отправить запрос с капчей
        return captcha.try_again(key)

    def search_group(self, title, count=1000, market=False, sort=6):
        return self.vk.groups.search(q=title, count=count, market=market, sort=sort)

    def search_new_group(self):
        response = requests.get(
            "https://api.vk.com/method/execute.counts/",
            params={
                "gid": self.get_max_id(),
                "access_token": VK_TOKEN,
                "v": VK_API_VERSION,
            })

        if response.status_code != 200:
            raise RequestFailed

        json_response = response.json()
        return tuple(filter(lambda group: re.search(r"(маркет|магаз)", group["name"]), json_response["response"]))

    @staticmethod
    def auth_handler():
        """ При двухфакторной аутентификации вызывается эта функция."""

        # Код двухфакторной аутентификации
        key = input("Введите код двухфакторной аутентификации: ")
        # Если: True - сохранить, False - не сохранять.
        remember_device = True

        return key, remember_device

    @staticmethod
    def get_max_id():
        with open("vk.tmp", "r") as file:
            response = requests.get("https://api.vk.com/method/execute.getTip/",
                                    params={
                                        "oid": file.read(),
                                        "range": 100000,
                                        "access_token": VK_TOKEN,
                                        "v": VK_API_VERSION,
                                    })

        if response.status_code != 200:
            raise RequestFailed

        json_response = response.json()
        max_id = json_response["response"]["max"]
        with open("vk.tmp", "w") as file:
            file.write(str(max_id))
        return max_id


if __name__ == '__main__':
    v = VkClient()
    mx = v.get_max_id()
    print(mx)
