from typing import Protocol


class IDispatcher(Protocol):
    def upload_file(self, file_key, file_data):
        ...
