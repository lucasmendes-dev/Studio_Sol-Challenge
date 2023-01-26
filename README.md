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

![input1](https://user-images.githubusercontent.com/106750716/214899333-0fb8228a-a30c-4290-8e9e-222827f9e8a1.png)

Output:

![output1](https://user-images.githubusercontent.com/106750716/214899366-c1399c88-bfa0-4393-94d2-5660e3880361.png)

or

![output12](https://user-images.githubusercontent.com/106750716/214899409-bb4d53c4-5c5f-4b4a-b6d4-86e26d7443d8.png)

<b>Obs:</b> You can choose the rules you want, there's no need to choose all of them, but at least 1 rule and the 'password' is mandatory.

Input:

![input2](https://user-images.githubusercontent.com/106750716/214899448-51184720-6c20-41d5-90a5-71690280ee5c.png)

Output:

![output2](https://user-images.githubusercontent.com/106750716/214899495-a5ad8cdc-c9a9-4947-b430-e02e45c990dc.png)

or

![out3](https://user-images.githubusercontent.com/106750716/214899525-ab7dc560-2b88-40b8-b820-0975bee7238f.png)

<p><b>Return code:</b></p>
<p>200 OK: The password meets the configured security rules</p>
<p>400 Bad Request: The request is missing all the required parameters or the values are invalid</p>


<h1>Security rules / Methods</h1>
<ul>
    <li><b>minSize:</b> The password size should be at least the specified value</li>
    <li><b>minUppercase:</b> The password should contain at least the specified number of uppercase characters</li>
    <li><b>minLowercase:</b> The password should contain at least the specified number of lowercase characters</li>
    <li><b>minDigit:</b> The password should contain at least the specified number of digits</li>
    <li><b>minSpecialChars:</b> The password should contain at least the specified number of special characters</li>
    <li><b>noRepeted:</b> The password should not contain consecutive repeating characters</li>
</ul>

<h1>Examples of use</h1>
<p>Verify if the password "TesteSenhaForte!123&" meets the configured security rules:</p>

curl -d '{"password": "TesteSenhaForte!123&", "rules": [{"rule": "minSize","value": "8"},{"rule": "minSpecialChars","value": "2"},{"rule": "noRepeted","value": "0"},{"rule": "minDigit","value": "4"}]}' -H "Content-Type: application/json" -X POST http://localhost:8080/verify

<p>Output:</p>

![output1](https://user-images.githubusercontent.com/106750716/214899366-c1399c88-bfa0-4393-94d2-5660e3880361.png)

<p>Verify if the password "Senha1" meets the configured security rules:</p>

curl -d '{"password": "Senha1", "rules": [{"rule": "minSize","value": "8"},{"rule": "minSpecialChars","value": "2"},{"rule": "noRepeted","value": "0"},{"rule": "minDigit","value": "1"}]}' -H "Content-Type: application/json" -X POST http://localhost:8080/verify
Output:

![output12](https://user-images.githubusercontent.com/106750716/214899409-bb4d53c4-5c5f-4b4a-b6d4-86e26d7443d8.png)
