from typing import List


class TableCreator:
    def __init__(self, column_names: list, data: List[list], extra_gap: int=2, with_border: bool=False):
        self.column_names = column_names
        self.data = data
        self.extra_gap = extra_gap
        self.with_border = with_border
        self.table = self.create_table()

    def create_table(self) -> str:
        """
        Creates table
        :return: Table as a string ready to print or output to file
        """
        max_len = [
            max(x) if max(x) > len(self.column_names[pos]) else len(self.column_names[pos])
            for pos, x in enumerate(zip(*[[len(j) for j in i] for i in self.data]))
        ]
        rows = [
            "".join([cell + (" " * ((max_len[pos] - len(cell)) + self.extra_gap)) for pos, cell in enumerate(row)])
            for row in self.data
        ]
        col_row = "".join(
            [i + (" " * ((max_len[pos] - len(i)) + self.extra_gap)) for pos, i in enumerate(self.column_names)]
        )
        rows.insert(0, col_row)
        if self.with_border:
            top = "".join(["+" + ("-" * ((i + self.extra_gap) - 1)) for pos, i in enumerate(max_len)]) + "+"
            rows.insert(0, top)
            rows.insert(len(rows), top)
        return "\n".join(rows)


if __name__ == '__main__':
    t = TableCreator(["a", "b", "c"], [["1", "22", "333"], ["4444", "55555", "666666"], ["7777777", "88888888", "999999999"]], with_border=True)
    print(t.table)
