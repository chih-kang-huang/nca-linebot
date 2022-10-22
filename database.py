"""
Helper funtions for read and edit data.
"""
import os
import pymysql
import pymysql.cursors
import pandas as pd

def connectToDatabase():
    """ Connects to the database """
    conn = pymysql.connect(host=os.environ.get('SQL_HOST'),
                             user=os.environ.get('SQL_USER'),
                             password=os.environ.get('SQL_PASSWD'),
                             db=os.environ.get('DB_NAME'),
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    return conn

def executeQuery(query):
    """ Executes a random sql query and returns the results if there is one 
    :param query <string>: sql query
    """
    conn = connectToDatabase()
    cursor = conn.cursor()
    answer = 'executeQuery start'
    try:
        cursor.execute(query)
        try:
            answer = cursor.fetchall() # will return () is nothing is expected
        except:
            answer = "Not valid"
    except:
        answer = 'ERR: executeQuery not working'
    conn.commit()
    conn.close() 
    return answer 

def createTableQuery(table_name, df):
    """ Returns a query that creates table from dataframe using only its colums name
    :param table_name <string>: the name of the table
    :param df <pd.DataFrame>: an example table
    """
    cols = df.columns
    query = "CREATE TABLE IF NOT EXISTS "+table_name+"("+table_name+"_id int auto_increment, " 
    for element in cols:
       query += str(element) +" varchar(255), "
    query += "primary key("+table_name+"_id));"
    print(query)
    return(query)


def addRowQuery(table_name, df):
    """ Returns a query that adds a row into a table that depends on the structure of df
    :param table_name <string>: the name of the table
    :param df <pd.DataFrame>: an example table
    """
    cols = df.columns
    query = "INSERT INTO "+table_name+"("+table_name+"_id" 
    inputs = "(%s"
    for element in cols:
       query += ", "+ str(element)
       inputs +=  ", %s"
    query += ") VALUES "+inputs+");"
    print(query)
    return(query)
    

def addTableFromDF(table_name, df):
    """ Adds the table in the database with the data in dataframe
    :param table_name <string>: the name of the table
    :param df <pd.DataFrame>: the data that we want to store
    """
    conn = connectToDatabase()
    cursor = conn.cursor()
    cursor.execute(createTableQuery(table_name, df)) # create if not exists
    values_to_be_insert = list(df.itertuples(index=False, name=None))
    cursor.execute('SELECT COUNT(*) FROM '+table_name)

    element_id = cursor.fetchall()[0]['COUNT(*)'] # number of existing rows
    for row in range(len(values_to_be_insert)):  # or len(df.index)
        element_id += 1
        cursor.execute(addRowQuery(table_name, df),(element_id,)+values_to_be_insert[row])
        
    conn.commit()
    conn.close() 


def fetchTable2Dataframe(table_name):
    """ Fetches a table and turn it to dataframe
    : param table_name <string>: name of the table in the database
    return type : pandas dataframe 
    """
    conn = connectToDatabase()
    query = "SELECT * FROM " + str(table_name)
    df = pd.read_sql(query, conn) # Transform SQL to Pandas DF
    conn.close() 
    print(df)
    return df

def resetTableQuery(table_name,format_df): 
    """ Reset the table in the database that follows a new format
    :param table_name <string>: name of the table 
    :param format_df <pd.DataFrame>: the format
    """
    conn = connectToDatabase()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS "+ table_name+";")
    cursor.execute(createTableQuery(table_name, format_df))
    conn.commit()
    conn.close() 