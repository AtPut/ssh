
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> int | str:
        value = self._cells.get(cell, '')
        if value.startswith('='):
            if value.count("'") == 1:
                return "#Error"
            if value.count("'") == 2:
                return value[1:]
            try:
                return int(float(value[1:]))
            except ValueError:
                return "#Error"
        if value.replace('.', '', 1).isdigit():
            if '.' in value:
                return "#Error"
            return int(value)
        if value.count("'") == 1:
            return "#Error"
        return value

