Overview
The password verification API is a REST API that checks if a password meets a series of security rules. The rules include minimum size, special characters, numbers, uppercase and lowercase letters, and non-repeating characters.

Authentication
Authentication is not required to use this API.

Rate limits
There are no rate limits configured for this API.

Endpoints
Verify Password
Checks if a password meets the configured security rules.

URL: /verify
Method: POST
Input:
{
    "password": "TesteSenhaForte!123&",
    "rules": [
        {"rule": "minSize","value": "8"},
        {"rule": "minSpecialChars","value": "2"},
        {"rule": "noRepeted","value": "0"},
        {"rule": "minDigit","value": "4"}
    ]
}
Output:
{
    "verify": "True",
    "noMatch": []
}

or

{
    "verify": "False",
    "noMatch": ["minSize", "minSpecialChars"]
}

Return code:
200 OK: The password meets the configured security rules
400 Bad Request: The request is missing all the required parameters or the values are invalid

Security rules
minSize: The password size should be at least the specified value
minUppercase: The password should contain at least the specified number of uppercase characters
minLowercase: The password should contain at least the specified number of lowercase characters
minDigit: The password should contain at least the specified number of digits
minSpecialChars: The password should contain at least the specified number of special characters
noRepeted: The password should not contain consecutive repeating characters

Examples of use
Verify if the password "TesteSenhaForte!123&" meets the configured security rules

curl -d '{"password": "TesteSenhaForte!123&", "rules": [{"rule": "minSize","value": "8"},{"rule": "minSpecialChars","value": "2"},{"rule": "noRepeted","value": "0"},{"rule": "minDigit","value": "4"}]}' -H "Content-Type: application/json" -X POST http://localhost:8080/verify
Output:

{
    "verify": "True",
    "noMatch": []
}

Verify if the password "TesteSenhaFraca" meets the configured security rules

curl -d '{"password": "TesteSenhaFraca", "rules": [{"rule": "minSize","value": "8"},{"rule": "minSpecialChars","value": "2"},{"rule": "noRepeted","value": "0"},{"rule": "minDigit","value": "4"}]}' -H "Content-Type: application/json" -X POST http://localhost:8080/verify
Output:

{
    "verify": "False",
    "noMatch": ["minSize", "minSpecialChars", "minDigit"]
}