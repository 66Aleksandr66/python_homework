#Task 1
import logging                                          # встроенный модуль для логов
logger = logging.getLogger(__name__ + "_parameter_log") # создать логгер с именем
logger.setLevel(logging.INFO)                           # записывать сообщения уровня INFO и выше
logger.addHandler(logging.FileHandler("./decorator.log", "a"))  # куда писать: в файл, режим "a"

def logger_decorator(func):              # декоратор получает исходную функцию
    def wrapper(*args, **kwargs):      # обёртка собирает ЛЮБЫЕ аргументы
        value = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {args if args else 'none'}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.log(logging.INFO, f"return: {value}")
        return value                   # отдаём результат наружу
    return wrapper


@logger_decorator
def greeting():
    print("Hello, World!")

@logger_decorator
def args_func(*args):
    return True

@logger_decorator
def kwargs_func(**kwargs):
    return logger_decorator

greeting()
args_func(1,2,3)
kwargs_func(book = 'War and Peace')
