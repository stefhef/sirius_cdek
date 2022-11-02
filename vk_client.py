import vk_api
from constants import VK_PASSWORD, VK_LOGIN
from exeptions import MissingVariables, AuthorizationError


class VkClient:
    vk = None

    def __init__(self):
        if not any((VK_LOGIN, VK_PASSWORD)):
            raise MissingVariables
        self.authorization_login_password(login=VK_LOGIN, password=VK_PASSWORD)

    def authorization_login_password(self, login, password):
        """Авторизация с использованием логина или пароля"""
        try:
            vk_session = vk_api.VkApi(login=login,
                                      password=password,
                                      captcha_handler=self.captcha_handler,
                                      auth_handler=self.auth_handler)
            vk_session.auth()
            self.vk = vk_session.get_api()
        except vk_api.AuthError as error_msg:
            raise AuthorizationError(error_msg)

    @staticmethod
    def captcha_handler(captcha):
        """ При возникновении капчи вызывается эта функция и ей передается объект
            капчи. Через метод get_url можно получить ссылку на изображение.
            Через метод try_again можно попытаться отправить запрос с кодом капчи
        """

        key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

        # Пробуем снова отправить запрос с капчей
        return captcha.try_again(key)

    @staticmethod
    def auth_handler():
        """ При двухфакторной аутентификации вызывается эта функция.
        """

        # Код двухфакторной аутентификации
        key = input("Enter authentication code: ")
        # Если: True - сохранить, False - не сохранять.
        remember_device = True

        return key, remember_device


if __name__ == '__main__':
    v = VkClient()
