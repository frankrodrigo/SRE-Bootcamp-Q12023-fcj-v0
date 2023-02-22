from dbconnect import db_connection
import hashlib
import jwt

query = db_connection()

# These functions need to be implemented
class Token:

    def generate_token(self, username, password):
        sentence1 = "SELECT password FROM users WHERE username="+'"'+username+'"'
        salted_password = query.db_query(sentence1)
        sentence2 = "SELECT salt FROM users WHERE username=" + '"' + username + '"'
        salt_value = query.db_query(sentence2)
        password2 = password + salt_value
        input_password_salted = hashlib.sha512(password2.encode()).hexdigest()

        if input_password_salted == salted_password:
            print("Password correcto")
            role_query = "SELECT role FROM users WHERE username=" + '"' + username + '"'
            role = query.db_query(role_query)
            encoded_jwt = jwt.encode({"role": role}, "my2w7wjd7yXF64FIADfJxNs1oupTGAuW", algorithm='HS256')
            return encoded_jwt

        else:
            return "password incorrecto"




class Restricted:

    def access_data(self, authorization):



        return 'You are under protected data'
