class Instrument:
    def __init__(self, name, manufacturer, year_built, cost):
        self.name = name
        self.manufacturer = manufacturer
        self.year_built = year_built
        self.cost = cost
    def print_info(self):
        print('Instrument Information:')
        print(' Name:', self.name)
        print(' Manufacturer:', self.manufacturer)
        print(' Year built:', self.year_built)
        print(' Cost:', self.cost)

class StringInstrument(Instrument):
    def _init__(self, name, manufacturer, year_built, cost, num_strings, num_frets):
        Instrument. __init__(self, name, manufacturer, year_built, cost)
        self.num_strings = num_strings
        self. num_frets = num_frets

if __name__ == "__main__":
    instrument_name = input('instrument name:')
    manufacturer_name = input('manufacturer name:')
    year_built = int(input('year built: '))
    cost = int(input('cost: '))
    string_instrument_name = input('string instrument name: ')
    string_manufacturer = input('string instrument manufacturer: ')
    string_year_built = int(input('year the string instrument was built: '))
    string_cost = int(input('string instrument cost: '))
    num_strings = int(input('number of strings on the instrument: '))
    num_frets = int(input('number of frets on the instrument: '))

    myInstrument = Instrument(instrument_name, manufacturer_name, year_built, cost)
    myStringInstrument = StringInstrument(string_instrument_name, string_manufacturer, string_year_built, string_cost)

    myInstrument.print_info()
    myStringInstrument.print_info()

    print(' Number of strings: ', num_strings)
    print('Number of Frets: ', num_frets)
