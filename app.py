from flask import Flask, jsonify, request   #Type 'pip install Flask' if you don't have Flask on your PC.
import constants


app = Flask(__name__)

#Endpoint 
@app.route('/verify', methods=['POST'])
def VerifyPassword():    
    conditions = request.get_json()
    password = conditions["password"]
    rules_conditions = conditions["rules"]

    noMatch = []
    for rule in rules_conditions:
        rule_name = rule["rule"]
        value = int(rule["value"])
        if rule_name in constants.rules:
            if not constants.rules[rule_name](password, value):
                noMatch.append(rule_name)
            
    return jsonify(
        {
            "verify": "True" if len(noMatch) == 0 else "False", 
            "noMatch": noMatch
        }
    ), 200

#running Flask server
app.run(port=8080,host='localhost',debug=True)