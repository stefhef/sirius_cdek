class MissingVariables(Exception):
    """Вызывается когда не введены данные для входа в .env файле"""

    def __init__(self, message="\nВведите данные для входа в ВК"):
        super().__init__(message)
