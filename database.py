import psycopg2

def connection_to_db():
    try:
        connection = psycopg2.connect(user='harsh', password='harshdb', host='127.0.0.1', database='postgres')
        return connection
    except (Exception, psycopg2.Error) as error:
        print(error)

def send_passwd_to_db(app_site_name, user_name, email_add, web_site, enc_passwd):
    try:
        connection = connection_to_db()
        cursor = connection.cursor()
        insert_statement = """ INSERT INTO accounts (Name, Username, Email, URL, Password) VALUES (%s, %s, %s, %s, %s)"""
        insertion_record = (app_site_name, user_name, email_add, web_site, enc_passwd)
        cursor.execute(insert_statement, insertion_record)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)

def find_passw_from_db(app_name):
    try:
        connection = connection_to_db()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT password FROM accounts WHERE name = '""" + app_name + "'"
        cursor.execute(postgres_select_query, app_name)
        connection.commit()
        result = cursor.fetchone()
        str = ''
        for item in result:
            str = str + item
        alphabets = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '123456789' + '(,._-*~"<>/|!@#$%^&)+='
        key = 20
        dec_passwd = ''
        for letter in str:
            new_position=(alphabets.find(letter)-key)%len(alphabets)
            dec_passwd+=alphabets[new_position]
        print('Here is your password')
        print(dec_passwd)

    except (Exception, psycopg2.Error) as error:
        print(error)


def search_email_from_db(user_email):
    data = ('App Name: ', 'Username: ', 'E-mail: ', 'url: ')
    try:
        connection = connection_to_db()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM accounts WHERE email = '""" + user_email + "'"
        cursor.execute(postgres_select_query, user_email)
        connection.commit()
        result = cursor.fetchall()
        print('')
        print('Searching in Database...')
        print('')
        j = 1
        for row in result:
            print(j, '---------')
            j += 1
            for i in range(0, len(row) - 1):
                print(data[i] + row[i])

        print('')
    except (Exception, psycopg2.Error) as error:
        print(error)



def delete_from_db(del_pass):
    try:
        connection = connection_to_db()
        cursor = connection.cursor()
        delete_statement = """ DELETE FROM accounts WHERE name = '""" + del_pass + "'"
        delete_record = del_pass
        cursor.execute(delete_statement, delete_record)
        connection.commit()
        print('Password Deleted Successfully!')
    except (Exception, psycopg2.Error) as error:
        print(error)


