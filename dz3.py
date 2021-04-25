class Cell:
    def __init__(self, cells_amount):
        self.cells_amount = int(cells_amount)

    def __add__(self, other):
        return Cell(self.cells_amount + other.cells_amount)

    def __sub__(self, other):
        return Cell(self.cells_amount - other.cells_amount)

    def __mul__(self, other):
        return Cell(self.cells_amount * other.cells_amount)

    def __floordiv__(self, other):
        return Cell(self.cells_amount // other.cells_amount)

    def __str__(self):
        return f'{self.cells_amount} cells long'

    def make_order(self, amount_of_cells_in_row):
        rows_amount, add_to_last_row = \
            divmod(self.cells_amount, amount_of_cells_in_row)

        cell_as_string = ''
        for _ in range(rows_amount):
            cell_as_string += f'{"*" * amount_of_cells_in_row}\n'

        return cell_as_string.rstrip() + '*' * add_to_last_row


if __name__ == '__main__':
    c1 = Cell(46)
    c2 = Cell(20)

    c_add = c1 + c2
    c_sub = c1 - c2
    c_mul = c1 * c2
    c_div = c1 // c2

    print(c_add, c_sub, c_mul, c_div)
    print(c_add.make_order(10))
    print(c_sub.make_order(3))
    print(c_mul.make_order(5))
    print(c_div.make_order(2))
