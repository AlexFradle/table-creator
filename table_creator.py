from typing import List, Union


class TableCreator:
    def __init__(self, column_names: Union[list, tuple], data: List[list], extra_gap: int=2, with_border: bool=False):
        self.__column_names = column_names
        self.__data = [[str(j) for j in i] for i in data]
        self.__data = [row + ([""] * (len(self.__column_names) - len(row))) for row in self.__data]
        self.__extra_gap = extra_gap
        self.__with_border = with_border
        self.__table = self.__create_table()

    @property
    def table(self):
        return self.__table

    def __create_table(self) -> str:
        """
        Creates table
        :return: Table as a string ready to print or output to file
        """
        max_len = [
            max(x) if max(x) > len(self.__column_names[pos]) else len(self.__column_names[pos])
            for pos, x in enumerate(zip(*[[len(j) for j in i] for i in self.__data]))
        ]
        rows = [
            "".join([cell + (" " * ((max_len[pos] - len(cell)) + self.__extra_gap)) for pos, cell in enumerate(row)])
            for row in self.__data
        ]
        col_row = "".join(
            [i + (" " * ((max_len[pos] - len(i)) + self.__extra_gap)) for pos, i in enumerate(self.__column_names)]
        )
        rows.insert(0, col_row)
        if self.__with_border:
            top = "".join(["+" + ("-" * (i + self.__extra_gap)) for pos, i in enumerate(max_len)]) + "+"
            rows = [list(i) for i in rows]
            for row in rows:
                for pos, c in enumerate(row):
                    if top[pos] == "+":
                        row.insert(pos, "|")
                row.insert(len(row), "|")
            rows = ["".join(i) for i in rows]
            rows.insert(0, top)
            rows.insert(2, top)
            rows.insert(len(rows), top)
        return "\n".join(rows)


if __name__ == '__main__':
    t = TableCreator(
        ["id", "name", "address", "phone"], [
            ["1", "James Smith", "1 generic road"],
            ["2", "New Name", "43355 house land"],
            ["3", "John Doe", "", "01235 678910"]
        ], with_border=True)
    print(t.table)
