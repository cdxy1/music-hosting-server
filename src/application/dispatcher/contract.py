from typing import Protocol


class IDispatcher(Protocol):
    def upload_file(self, prefix, file_key, file_data):
        ...
