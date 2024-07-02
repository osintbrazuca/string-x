from core.format import Format


class Funcs:

    @staticmethod
    def clear(value_str: str) -> str:
        if value_str:
            return Format.clear_value(value_str)
        return None

    @staticmethod
    def debase64(value_str: str) -> str:
        if value_str:
            return Format.decode64(value_str)
        return None

    @staticmethod
    def base64(value_str: str) -> str:
        if value_str:
            return Format.encode64(value_str)
        return None

    @staticmethod
    def sha1(value_str: str) -> str:
        if value_str:
            return Format.sha1(value_str)
        return None

    @staticmethod
    def sha256(value_str: str) -> str:
        if value_str:
            return Format.sha256(value_str)
        return None

    @staticmethod
    def hex(value_str: str) -> str:
        if value_str:
            return Format.encodehex(value_str)
        return None

    @staticmethod
    def dehex(value_str: str) -> str:
        if value_str:
            return Format.decodehex(value_str)
        return None

    @staticmethod
    def md5(value_str: str):
        if value_str:
            return Format.md5(value_str)
        return None
