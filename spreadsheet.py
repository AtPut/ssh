
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluation_stack = set()  # To track cells during evaluation to detect cycles

    def set(self, cell: str, value: str) -> None:
        if value.startswith('='):
            if value.count("'") == 1:
                value = "#Error"
            elif value.count("'") == 2:
                value = value[2:-1]
            elif value[1:].isnumeric():
                value = int(value[1:])
        elif value.replace('.', '', 1).isdigit():
            if '.' in value:
                value = "#Error"
            else:
                value = int(value)
        elif value.count("'") == 1:
            value = "#Error"
        self._cells[cell] = value

    def get(self, cell: str) -> int | str:
        if cell in self._evaluation_stack:
            return "#Error"  # Detect cycle and return error
        self._evaluation_stack.add(cell)  # Add cell to stack to track evaluation

        value = self._cells.get(cell, '')
        if isinstance(value, str) and value.startswith('='):
            ref_cell = value[1:]
            if ref_cell in self._cells:
                value = self.get(ref_cell)
            else:
                value = "#Error"
        if isinstance(value, str) and value.isnumeric():
            value = int(value)

        self._evaluation_stack.remove(cell)  # Remove cell from stack after evaluation
        return value

