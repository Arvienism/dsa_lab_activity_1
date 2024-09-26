class diamond_shape:
    def __init__(self) -> None:
        self.row = self.desired_rows()

    def desired_rows(self):
        while True:
            try:
                row = int(input("Enter the number of rows: "))
                if row % 2 == 0:
                    print("Please provide an odd integer.")
                else:
                    return row
            except ValueError:
                print('VALUE ERROR! Please enter INTEGERS ONLY!')

    def print_diamond(self):
        for i in range(self.row):
            print (" " * (self.row - i) + " *" * (i + 1))
        
        for j in range(self.row - 1):
            print(" " * (j + 2) + " *" * (self.row - 1 - j))

diamond = diamond_shape()
diamond.print_diamond()