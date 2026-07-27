print("=" * 40)
print("💱 Offline Currency Converter")
print("=" * 40)

# Example exchange rates (can be updated manually)
rates = {
    "USD": 1.00,
    "EUR": 0.85,
    "TRY": 40.50,
    "PLN": 3.65,
    "GBP": 0.73
}

print("Available currencies:")
print(", ".join(rates.keys()))

from_currency = input("\nFrom: ").upper()
to_currency = input("To: ").upper()

if from_currency not in rates or to_currency not in rates:
    print("Unsupported currency.")
    exit()

amount = float(input(f"Amount ({from_currency}): "))

# Convert through USD
usd = amount / rates[from_currency]
converted = usd * rates[to_currency]

print(f"\n{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")