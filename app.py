from flask import Flask, jsonify, request

app = Flask(__name__)

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


rules = {
    "minSize": minSize,
    "minUppercase": minUppercase,
    "minLowercase": minLowercase,
    "minDigit": minDigit,
    "minSpecialChars": minSpecialChars,
    "noRepeted": noRepeted
}


@app.route('/verify', methods=['POST'])
def VerifyPassword():    
    conditions = request.get_json()
    password = conditions["password"]
    rules_conditions = conditions["rules"]

    noMatch = []
    for rule in rules_conditions:
        rule_name = rule["rule"]
        value = int(rule["value"])
        if rule_name in rules:
            if not rules[rule_name](password, value):
                noMatch.append(rule_name)
            
    return jsonify(
        {
            "verify": "True" if len(noMatch) == 0 else "False", 
            "noMatch": noMatch
        }
    ), 200


app.run(port=8080,host='localhost',debug=True)