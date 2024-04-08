#変数を代入
# var = 3
# var = 5
# var = 15
var = 7

#条件分岐
if var % 3 == 0:
    if var % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
elif var % 5 == 0:
    print("Buzz")
else:
    print(var)
