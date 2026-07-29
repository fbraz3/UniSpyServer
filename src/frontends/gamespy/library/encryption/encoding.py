

class Encoding:
    @staticmethod
    def get_string(data: bytes) -> str:
        assert isinstance(data, bytes)
        return data.decode("ascii")

    @staticmethod
    def get_bytes(data) -> bytes:
        if isinstance(data, bytes):
            return data
        return str(data).encode()
