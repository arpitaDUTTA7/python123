# Company will give bonus based on the following criteria.
# Time spent in company              Bonus
# More than 10 years                  10%
# More than 6 and less than 10         8%
# Less than 6 years                    5%
# Ask the salary and time spent from the user. Print the net bonus amount accordingly.

salary = int(input("Enter your current salary: "))
time = int(input("Enter the time spent in the company: "))

if time > 10 :
    print("Now your salary is: {:.2f} ".format(salary + salary*(10/100)))

elif time > 6 and time < 10 :
    print("Now your salary is: {:.2f}".format(salary + salary*(8/100)))

elif time <6 :
    print("Now your salary is: {:.2f}".format(salary + salary*(5/100)))

else :
    print("You did not receive any bonus")


