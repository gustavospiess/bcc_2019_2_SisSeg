import mysql.connector
from mysql.connector import Error
import re

_login_regex = re.compile(r'[A-Za-z]{4,55}')
_pswrd_regex = re.compile(r'[A-Za-z0-9!@#$%*()]{4,55}')

def validate_login(login_str):
    match = _login_regex.fullmatch(login_str)
    if not match:
        return 'Login inválido, apenas letras (4-55)'

def validate_pswrd(pswrd_str):
    match = _pswrd_regex.fullmatch(pswrd_str)
    if not match:
        return 'Senha inválido, apenas letras e caracteres especiais (!@#$%*()) (4-55)'

def main():
    login_str = input('Login: ')
    err = validate_login(login_str)
    if err:
        print(err)
        return

    pswrd_str = input('Password: ')
    err = validate_pswrd(pswrd_str)
    if err:
        print(err)
        return

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='mydb',
                                             user='root',
                                             password='root')

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("select qt_saldo from saldos where ds_login = '" + login_str + "' and ds_senha = '" + pswrd_str + "';")
            record = cursor.fetchone()
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
