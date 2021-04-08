def electricity_bill(time: float, power: float, price: float = 0.617) -> float:
    return time * power * price


print(f'Your electricity bill will be {electricity_bill(float(input("Enter time in hour: ")), float(input("Enter machine power in kW: "))):.2f} zl')
