"""Messanges module."""


class Message:
    """Class for messages to user."""
    unauthorized = (
        'Только авторизованные пользователи могут использовать сервис.'
        ' Пожалуйста, зарегистрируйтесь или авторизуйтесь.'
    )
    success_register = 'Вы успешно зарегистрировались'
    error_register = 'Ошибка регистрации'
    no_translates = 'У вас пока нет ни одного перевода...'
