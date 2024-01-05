from colorama import Fore


class Logger:

    def __init__(self, is_debug_enable: bool = True):
        self.is_debug_enable = is_debug_enable

    def __logger(self, function: ()):
        if self.is_debug_enable:
            function()

    def debug(self, message: str):
        self.__logger(print(Fore.BLUE + message))

    def info(self, message: str):
        self.__logger(print(Fore.YELLOW + message))

    def bug(self, message: str):
        self.__logger(print(Fore.RED + message))

    def success(self, message: str):
        self.__logger(print(Fore.GREEN + message))
