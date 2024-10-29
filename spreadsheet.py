
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> int | str:
        value = self._cells.get(cell, '')
        if value.replace('.', '', 1).isdigit():
            if '.' in value:
                return "#Error"
            return int(value)
        if value.count("'") == 1:
            return "#Error"
        return value

