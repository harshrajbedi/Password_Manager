import psycopg2

def connection_to_db():
    try:
        connection = psycopg2.connect(user='harsh', password='harshdb', host='127.0.0.1', database='postgres')
        return connection
    except (Exception, psycopg2.Error) as error:
        print(error)

def get_master_passwd():
    try:
        connection = connection_to_db()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT masterpasswd FROM masterpassword """
        cursor.execute(postgres_select_query)
        connection.commit()
        result = cursor.fetchone()
        return result[0]

    except (Exception, psycopg2.Error) as error:
        print(error)
