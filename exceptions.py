"""Exceptions."""


class LimitReportException(LookupError):
    """Невозможно создать отчет ввиду отсутствия необходимых данных."""


class NameErrorException(TypeError):
    """Невозможно создать имя для переода."""


class TranslateErrorException(ValueError):
    """Невозможно перевести текст."""
