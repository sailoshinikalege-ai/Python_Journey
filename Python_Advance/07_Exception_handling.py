'''
WAP to simulate an IPL match between RCB and Mumbai Indians.

Generate a random score for both teams between 100 and 180. Use try-except-else-finally to handle a ZeroDivisionError.
In the try block, perform a division by zero operation. If an exception occurs, display an appropriate error message.
Otherwise, display the scores of both teams.
Finally, display the total score of both teams. 
'''
import random

target = 100

mi_score = random.randint(100, 180)
rcb_score = random.randint(100, 180)
print(mi_score)
print(rcb_score)

try:
    a = target / 0

except ZeroDivisionError:
    print('Cannot divide by zero')

else:
    print('MI SCORE IS:', mi_score)
    print('RCB SCORE IS:', rcb_score)

finally:
    print('TOTAL SCORE IS:', mi_score + rcb_score)

#CUSTOM EXCEPTION:

nopro = int(input('Enter your product quantity:'))
'''
1. Custom Exception

WAP to take the number of seats available in a theatre.
If the number of seats is less than or equal to 0, raise ValueError with the message "No seats available".
Otherwise, print "Seats are available".
'''

'''
2. User-defined Exception

WAP to create a user-defined exception named SalaryError.
Take salary as input.
If salary is less than or equal to 0, raise SalaryError with the message "Invalid Salary".
Otherwise, print "Valid Salary".
'''


'''

3. Assertion

WAP to take the percentage of a student.
Use assertion to check that the percentage is between 0 and 100.
If the condition is satisfied, print "Valid Percentage". 
'''
