class RequestFailed(Exception):
    """Вызывается, когда происходит ошибка запроса"""

    def __init__(self, message="\nОшибка запроса"):
        super().__init__(message)
