class AuthorizationError(Exception):
    """Вызывается когда произошла ошибка авторизации в ВК"""

    def __init__(self, message):
        super().__init__(self,
                         "\nОшибка авторизации в ВК. Введете верные данные в файл .env\nБолее подробно:" + message)
