def spiralize(number):
    number = (number-1)/2
    return_value = 2*number*(8*number**2+15*number+13)/3+1
    return return_value
print(spiralize(501))
