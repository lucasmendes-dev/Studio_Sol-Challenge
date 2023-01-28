#Functions to validade the password
def minSize(password, rule):
    return len(password) >= rule        

def minUppercase(password, rule):    
    return sum(char.isupper() for char in password) >= rule

def minLowercase(password, rule):
    return sum(char.islower() for char in password) >= rule

def minDigit(password, rule):
    return sum(char.isdigit() for char in password) >= rule

def minSpecialChars(password, rule):
    special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "\\", "/" "{", "}", "[", "]"]
    return sum(password.count(char) for char in special_chars) >= rule

def noRepeted(password, rule):
    for i in range(1, len(password)):
        if password[i] == password[i-1]:
            return False
    return True