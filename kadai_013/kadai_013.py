#関数の定義
def calc_consumption_tax(value, tax):
    total = value * (1 + tax/100)
    # print(total)
    return total

value = 100
tax = 10 #[%]

print(calc_consumption_tax(value, tax))