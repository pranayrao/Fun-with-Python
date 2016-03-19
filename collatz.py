def collatz(number):
    if number%2==0:
        return number//2
    else:
        return number*3+1
print "Enter a number: "
try:

    number = int(input())
    while number!= 1:
        number = collatz(number)
        print number
except Exception as e:
    print "Must enter an integer"
