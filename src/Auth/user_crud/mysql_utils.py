import os, sys, time
import mysql.connector

class MySQL_Utils:
    myDB = mysql.connector.connect(
        host = "",
        user = "",
        password = "",
        database = ""
    )

    def SelectRow("SELECT * FROM users")

