class Matrix:
    def __init__(self, rows):
        self._rows = rows
        self._num_rows = len(rows)
        cols = []
        for i, _ in enumerate(rows[0]):
            cols.append([row[i] for row in rows])
        self._cols = cols
        self._num_cols = len(cols)
    
    def size(self) -> tuple:
        return (self._num_rows, self._num_cols)

    def __str__(self) -> str:
        for row in self._rows:
            temp = '\t'.join(str(elem) for elem in row)
        return '\n'.join('\t'.join(str(elem) for elem in row) for row in self._rows)
