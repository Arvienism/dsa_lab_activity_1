# create a method for converting celsius to fahrenheit and fahrenheit to celsius.
class temperature_converter:
    def __init__(self, temperature) -> None:
        self.temperature = temperature

    def celsius_to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
    def fahrenheit_to_celsius(self):
        return (self.temperature - 32) * 1/1.8
# ask user to input the a temperature. 
class main:
    while True:
        temp = float(input("Enter the temperature: "))
        conversion_type = str(input('\n' +
                            'Select conversion type: \n' +
                            'if Celsius to Fahrenheit, type: "1" \n' +
                            'if Fahrenheit to Celsius, type: "2" \n' + '\n'
                            'Type your conversion type number: ')).strip()

        temp_converter = temperature_converter(temp) 
# print the results.
        if conversion_type == "1":
            result = temp_converter.celsius_to_fahrenheit()
            print(f"{temp}°C is {result:.2f}°F")
            break
        elif conversion_type == "2":
            result = temp_converter.fahrenheit_to_celsius()
            print(f"{temp}°F is {result:.2f}°C")
            break
        else:
            print('"INVALID! Please, select the correct conversion type number." \n' + '\n')
main()