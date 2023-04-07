value = 1000
rate = 3
period = 5
future = value * ((1 + (rate / 100)) ** period)
print(f"The future value of the investment: {round(future, 2)} USD")
print(f"The future value of the investment: {future:.2f} USD")