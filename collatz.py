def collatz(number):
        if number % 2 == 0:
            print(number // 2)
        else:
            print(3 * number + 1)
            

try:
    number = input("type a whole number: ")
except KeyboardInterrupt:
    print("Must be a whole number")
		


collatz(int(number))
