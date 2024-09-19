def convert_usd_to_inr(amount):
    exchange_rate = 83.0  # Example exchange rate
    return amount * exchange_rate

def convert_inr_to_usd(amount):
    exchange_rate = 1 / 83.0  # Example exchange rate
    return amount * exchange_rate

# Example usage
print("Currency Converter:")
print("1. USD to INR")
print("2. INR to USD")
choice = input("Choose conversion type (1 or 2): ")

amount = float(input("Enter the amount: "))

if choice == '1':
    result = convert_usd_to_inr(amount)
    print(f"{amount} USD is equal to {result:.2f} INR.")
elif choice == '2':
    result = convert_inr_to_usd(amount)
    print(f"{amount} INR is equal to {result:.2f} USD.")
else:
    print("Invalid choice. Please select 1 or 2.")
