
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from flask import Blueprint
from server import app

from endpoints.utils import login_required, view
from model.dummies import *

import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
     "CREATE TABLE IF NOT EXISTS TEST(address_id serial PRIMARY KEY) ",
    "INSERT INTO TEST  VALUES (43)",

]
showDB = "SELECT * FROM TEST"

def execute(url, query):
    res = None
    if url is None:
        return None
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(query)

            res = cursor.fetchall()
            print(res)
            cursor.close()
        except dbapi2.Error as e:
            print(f"Query was \n {query} \n error{str(e)}")
            cursor.close()
    return None if res is not None and len(res) == 0 else res


def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)

        cursor.close()


if __name__ == "__main__":
    url = "postgres://postgres:docker@localhost:5432/postgres"
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file= sys.stderr)
        sys.exit(1)
    initialize(url)
    execute(url, showDB)






