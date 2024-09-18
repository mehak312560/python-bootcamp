def get_exchange_rate(from_currency, to_currency):
    # Define exchange rates (example rates, use real-time rates in a real application)
    rates = {
        'USD': {'EUR': 0.85, 'JPY': 110.53, 'GBP': 0.75},
        'EUR': {'USD': 1.18, 'JPY': 129.53, 'GBP': 0.88},
        'JPY': {'USD': 0.0090, 'EUR': 0.0077, 'GBP': 0.0068},
        'GBP': {'USD': 1.33, 'EUR': 1.14, 'JPY': 147.10}
    }
    
    # Return the exchange rate from 'from_currency' to 'to_currency'
    return rates.get(from_currency, {}).get(to_currency)

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate is None:
        return None
    return amount * rate

def main():
    print("Welcome to the Currency Converter!")
    
    # Get user input
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the source currency (USD, EUR, JPY, GBP): ").upper()
    to_currency = input("Enter the target currency (USD, EUR, JPY, GBP): ").upper()
    
    # Convert the currency
    converted_amount = convert_currency(amount, from_currency, to_currency)
    
    if converted_amount is None:
        print("Invalid currency code or conversion rate not available.")
    else:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()