import json

import mysql.connector
from flask import jsonify


class db_connection():

    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="sre-bootcamp-selection-challenge.cabf3yhjqvmq.us-east-1.rds.amazonaws.com",
                                username="secret", password="jOdznoyH6swQB9sTGdLUeeSrtejWkcw",
                                database="bootcamp_tht", port="3306")
            self.cur = self.con.cursor()
            print("DB connection success!")
        except:
            print("DB connection error!")


    def db_query(self,sql_query):

        self.cur.execute(sql_query)
        records = self.cur.fetchone()
        result = records[0]
        return result


    def db_query_test(self):

        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        return jsonify(result)