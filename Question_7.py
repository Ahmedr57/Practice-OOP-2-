# Create a Currency class that can add and subtract different currency objects using operator overloading. 
# Implement a method that uses @staticmethod to convert between different currencies based on the exchange rate provided as input. 
# Ensure that adding or subtracting different currency types throws a custom exception.

class Currency:
    
    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code


    
    def __add__(self, other):
        if isinstance(other, Currency) and self.currency_code == other.currency_code:
            return Currency(self.amount + other.amount, self.currency_code)
        else:
            raise TypeError("Cannot add currencies of different types")
    
    def __sub__(self, other):
        if isinstance(other, Currency) and self.currency_code == other.currency_code:
            return Currency(self.amount - other.amount, self.currency_code)
        else:
            raise TypeError("Cannot subtract currencies of different types")
        
    @staticmethod
    def convert(amount, from_currency, to_currency, exchnge_rate):
        if from_currency == to_currency:
            return amount
        else:
            return amount * exchnge_rate

    


usd1 = Currency(100, "USD")
usd2 = Currency(500, "USD")
eur1 = Currency(80, "EUR")
eur2 = Currency(67, "EUR")


total_usd = usd1 + usd2  
print(f"Total USD: {total_usd.amount} {total_usd.currency_code}")

total_eur = eur1 - eur2  
print(f"Total EUR: {total_eur.amount} {total_eur.currency_code}")

converted_usd = Currency.convert(100, "USD", "EUR", 0.85)  
print(f"Converted USD to EUR: {converted_usd}")

invalid_addition = usd1 + eur1 
print(invalid_addition)

