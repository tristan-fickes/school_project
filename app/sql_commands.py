# TODO: Method to retrieve total time a student spent in the hawksnest per day
# TODO: Method to retrieve the total number of times a student logged in/out of the hawksnest perday
# TODO: Method to retrieve average time a student spends in the hawksnest

import sqlite3
from sqlite3 import Error
import pathlib


def create_connection(path):
    """
    Open a connection to the SQLite DB.

    If there is no existing Database at the entered path one will be created.

    :param path: Absolute path to the location of the Database, or where the Database will be created.
    :return connection: Returns the connection Database object.
    """

    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


app_directory = pathlib.Path(__file__).parent.absolute()
db_connection = create_connection(f"{app_directory}\\students.sqlite")


def execute_query(connection, query):
    """ Use to execute SQLite queries.

    :param connection: Accepts a connection object to the database.
    :param query: SQLite query string that is passed to cursor.execute().
    """

    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred.")


def execute_read_query(connection, query):
    """ Selects records to return from the database.

    :param connection: Accepts a connection object to the database.
    :param query: SQLite query string that is passed to cursor.execute().
    :return: result: Results of the SQLite query.
    """

    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred.")


def student_login(student_id):
    """ Log a student into the database system.

    :param student_id: Student's unique student ID.
    """

    login_query = f"""
        INSERT INTO 
            powerpass(login_time, student_id)
        VALUES 
            (datetime('now', 'localtime'), {student_id})
        """
    execute_query(db_connection, login_query)


def student_logout(student_id):
    """ Log a student out of the database system.

    :param student_id: Student's unique student ID.
    """

    logout_query = f"""
        UPDATE
            powerpass
        SET
            logout_time = (datetime('now', 'localtime'))
        WHERE
            student_id = {student_id} AND logout_time IS NULL
        """
    execute_query(db_connection, logout_query)


def add_student_record(first_name, last_name, student_id):
    """ Add a student into the student database table.

    :param first_name: First name of the student.
    :param last_name: Last name of the student.
    :param student_id: Student's student ID number.
    """

    add_student_query = f"""
        INSERT INTO
            students (first_name, last_name, student_id)
        VALUES
            ({first_name}, {last_name}, {student_id});
        """
    execute_read_query(db_connection, add_student_query)
