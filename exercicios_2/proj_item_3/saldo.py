import mysql.connector
from mysql.connector import Error

def main():
    login_str = input('Login: ')
    passwrd_str = input('Password: ')
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='mydb',
                                             user='root',
                                             password='root')

        if connection.is_connected():
            command = "select qt_saldo from saldos where ds_login = %s and ds_senha = %s;"
            params = (login_str, passwrd_str)
            cursor = connection.cursor()
            cursor.execute(command, params)
            record = cursor.fetchone()
            if not record:
                print("dados inválidos")
                return
            print("Seu saldo é: ", record[0])
        else:
            raise Exception()

    except Error as e:
        print("Erro, por favor contate o desenvolvedor", e)
    finally:
        if (connection and connection.is_connected()):
            if cursor and cursor.close:
                cursor.close()
            if connection.close:
                connection.close()

if __name__ == '__main__':
    main()
