from typing import Union, Literal


class Detection:
    @staticmethod
    def detect(value: Union[str, tuple[int, int, int], tuple[int, int, int, int]]) -> Literal['hex', 'hexa', 'rgb', 'rgba', 'direct']:  # noqa
        if isinstance(value, str) and len(value.removeprefix('#')) == 6:
            return 'hex'
        elif isinstance(value, str) and len(value.removeprefix('#')) == 8:
            return 'hexa'
        elif isinstance(value, tuple) and len(value) == 3:
            return 'rgb'
        elif isinstance(value, tuple) and len(value) == 4:
            return 'rgba'
        elif isinstance(value, str) and value.replace(' ', '').lower().isidentifier():
            return 'direct'

        raise ValueError(f'Invalid value with unknown format: {value}. Possible formats: {['hex', 'hexa', 'rgb', 'rgba', 'direct']}')  # noqa
