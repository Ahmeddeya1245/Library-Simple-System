class Book:
    def __init__(self, name, id, total_quantity):
        self.name = name
        self.id = id
        self.total_quantity = total_quantity
        self.total_borrowed = 0

    def borrow(self):
        if self.total_quantity - self.total_borrowed == 0:
            return False
        return True

    def return_copy(self):
        assert self.total_borrowed > 0
        self.total_borrowed -= 1

    def __repr__(self):
        return f'Book name : {self.name} - id: {self.id} - Total Quantity: {self.total_quantity} - ' \
               f'total Borrowed : {self.total_borrowed}'