#!/usr/bin/python3
"""
Write a script that takes in the name of
a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa

Your script should take 4 arguments: mysql username,
mysql password, database name and state name
(SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running
on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""
if __name__ == "__main__":
    # importing neccesary libraries
    import MySQLdb
    import sys

    # verify if right arguments have been supplied
    if len(sys.argv) < 5:
        print(
            "Usage:{:s} mysql username mysql password database name".format(
                sys.argv[0])
        )

    else:
        # setup database parameters
        db_username, db_password, db_name, state_name = sys.argv[1:]
        db_host = "localhost"
        db_port = 3306

        # establish database connection
        conn = MySQLdb.connect(
            host=db_host,
            port=db_port,
            user=db_username,
            passwd=db_password,
            db=db_name,
            charset="utf8",
        )
        # sanitize state_name against sql injection attack
        state_name = state_name.replace("'", "")
        state_name = state_name.replace(";", "")

        # build and execute query
        cur = conn.cursor()
        cur.execute(
            "SELECT cities.name \
            FROM cities  \
            INNER JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name = '{:s}' \
            ORDER BY cities.id ASC".format(state_name)
            )
        records = cur.fetchall()

        # print out query result
        for i, record in enumerate(records):
            if i == len(records) - 1:
                print(record[0])
            else:
                print(record[0], end=', ')

        # close all connections to db
        cur.close()
        conn.close()
