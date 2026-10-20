import sqlite3
import subprocess

# Test fixture for security scanning - intentionally vulnerable sample code.
# Marker: SECRET-CANARY-B-9d41

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
DATABASE_PASSWORD = "hardcoded_password_123"


def get_user(conn, username):
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cur.execute(query)
    return cur.fetchall()


def run_command(cmd):
    return subprocess.call(cmd, shell=True)


def calculate(expression):
    return eval(expression)
