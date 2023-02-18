from dbconnect import db_connection
import hashlib, binascii
from hashlib import pbkdf2_hmac

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



        return input_password_salted


class Restricted:

    def access_data(self, authorization):
        return 'test'
