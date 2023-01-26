<h1>Overview</h1>
The password verification API is a REST API that checks if a password meets a series of security rules. The rules include minimum size, special characters, numbers, uppercase and lowercase letters, and non-repeating characters.

<h1>Authentication</h1>
Authentication is not required to use this API.

<h1>Rate Limits</h1>
There are no rate limits configured for this API.

<h1>EndPoints</h1>
<h3>Verify Password</h3>
<p>Checks if a password meets the configured security rules.</p>

<p><b>URL:</b> http://localhost:8080/verify</p>
<p><b>Method:</b> POST </p>
<p><b>Input:</b></p>
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

<b>Obs:</b> You can choose only the rules you want, there's no need to choose all of them, but at least 1 rule and the 'password' is mandatory.

Input:
{
    "password": "TesteSenhaForte!123&",
    "rules": [
        {"rule": "minUppercase","value": "1"}
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
    "noMatch": ["minUppercase"]
}

Return code:
200 OK: The password meets the configured security rules
400 Bad Request: The request is missing all the required parameters or the values are invalid


<h1>Security rules</h1>
minSize: The password size should be at least the specified value
minUppercase: The password should contain at least the specified number of uppercase characters
minLowercase: The password should contain at least the specified number of lowercase characters
minDigit: The password should contain at least the specified number of digits
minSpecialChars: The password should contain at least the specified number of special characters
noRepeted: The password should not contain consecutive repeating characters

<h1>Examples of use</h1>
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
