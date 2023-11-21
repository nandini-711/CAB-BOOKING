import mysql.connector
import sys


def Connect():

    conn = None
    try:
        conn = mysql.connector.connect(
            host='3306',
            username='root',
            password='Nandini@0808',
            database='cab_booking_system'
        )


    except:
        print("Error", sys.exc_info())

    finally:

        return conn



