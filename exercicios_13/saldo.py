import mysql.connector
from mysql.connector import Error
import hashlib

CONSTANTE = 'aaaaaaasdflkajsçdlkfjaçsldkjfçalskdjfçlaksdjfçlkasjdçflkajdsf'

def main():
    operation =""
    while(operation != '1' and operation != '2'):
        operation = input('Digite 1 para criar um usuário ou 2 para logar')
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='mydb',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        if(operation == '2'):
            login_str = input('Login: ')
            passwrd_str = input('Password: ')
        
            if connection.is_connected():
                command = "select qt_saldo from saldos where ds_login = %s and ds_senha = %s;"
                
                hash_function = hashlib.new('md5')
                hash_function.update(passwrd_str.encode('UTF-8'))
                hash_function.update(str([x for i, x in enumerate(login_str) if i % 2]).encode('UTF-8'))
                hash_function.update(CONSTANTE.encode('UTF-8'))
                hashed = hash_function.hexdigest()


                params = (login_str, hashed)
                
                cursor.execute(command, params)
                record = cursor.fetchone()
                if not record:
                    print("Dados inválidos!")
                    return
                print("Login feito com sucesso!")
            else:
                raise Exception()
        if(operation == '1'):
            login_str = input('Digite um Login para salvar: ')
            passwrd_str = input('Digite um Password para salvar: ')

            if connection.is_connected():
                command = "INSERT INTO saldos(ds_login, ds_senha) VALUES(%s,%s);"
                
                hash_function = hashlib.new('md5')
                hash_function.update(passwrd_str.encode('UTF-8'))
                hash_function.update(str([x for i, x in enumerate(login_str) if i % 2]).encode('UTF-8'))
                hash_function.update(CONSTANTE.encode('UTF-8'))
                hashed = hash_function.hexdigest()
                params = (login_str,hashed)
                cursor.execute(command, params)
                connection.commit()
                print("O usuário foi salvo com o hash: " + hashed)
                
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
