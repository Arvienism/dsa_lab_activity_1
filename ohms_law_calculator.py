# create a method for calculating voltage, current, and resistance
class ohms_law_calculator:
    def __init__(self) -> None:
        self.voltage = None
        self.current = None
        self.resistance = None
    
    def menu(self):
        print("Ohms's law Calculator MENU: \n" +
              '(1) Voltage \n' +
              '(2) Current \n' +
              '(3) Resistance \n' +
              '(4) Exit')

    def calculate_voltage(self):
        try:
            self.current = float(input("Enter the value of the current(I): "))
            self.resistance = float(input("Enter the value of the resistance(R): "))

            self.voltage = self.current * self.resistance
            print(f"The voltage(V) is {self.voltage:.2f}")
        except ValueError:
            print(' "VALUE ERROR!" Please put INTEGERS ONLY!') 
    
    def calculate_current(self):
        try:
            self.voltage = float(input("Enter the value of the voltage(V): "))
            self.resistance = float(input("Enter the value of the resistance(R): "))

            self.current = self.voltage / self.resistance
            print(f"The current(I) is {self.current:.2f}")
        except ValueError:
            print(' "VALUE ERROR!" Please put INTEGERS ONLY!')
        except ZeroDivisionError:
            print('"UNDEFINED!" Please, do not divide it to zero')
    
    def calculate_resistance(self):
        try:
            self.voltage = float(input("Enter the value of the voltage(V): "))
            self.current = float(input("Enter the value of the current(I): "))

            self.resistance = self.voltage / self.current
            print(f"The resistance(R) is {self.resistance:.2f}")
        except ValueError:
            print(' "VALUE ERROR!" Please put INTEGERS ONLY!')
        except ZeroDivisionError:
            print('"UNDEFINED!" Please, do not divide it to zero')
# ask user to choose what they want to calculate
class main(ohms_law_calculator):
     while True:
        try:
            ohms_law_calculator().menu()

            chosen_menu_number = int(input("Enter Chosen Menu Number: "))

            if chosen_menu_number == 1:
                ohms_law_calculator().calculate_voltage()

            elif chosen_menu_number == 2:
                ohms_law_calculator().calculate_current()
                
            elif chosen_menu_number == 3:
                ohms_law_calculator().calculate_resistance()
                
            elif chosen_menu_number == 4:
                print("Thank you for using this Calculator!")
                break

            else:
                print("Please, choose only the given number in the MENU!" + "\n")

            try_again = input("Do you want to try again? (y/n): ").lower()
            if try_again != "y":
                print("Thank you for using this Calculator!")
                break
        except ValueError:
            print(' "VALUE ERROR!" Please put INTEGERS ONLY!')
main()