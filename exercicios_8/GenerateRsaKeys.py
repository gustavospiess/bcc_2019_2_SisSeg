import rsa

def main():
    keys = rsa.newkeys(512)
    public_key = keys[0]
    private_key = keys[1]
    
    private_key_Exponent = private_key.d
    public_key_Exponent = public_key.e 
    modulo = private_key.n
    
    private_key_File_Path = "privateKey.txt"
    public_key_File_Path = "publicKey.txt"
    params_File_Path = "params.txt"

    private_key_content = private_key.save_pkcs1()
    private_key_File = open(private_key_File_Path, 'wb')
    private_key_File.write(private_key_content)
    private_key_File.close()

    public_key_content = public_key.save_pkcs1()
    public_key_File = open(public_key_File_Path, 'wb')
    public_key_File.write(public_key_content)
    public_key_File.close()

    params_File = open(params_File_Path,'w')
    params_File.write("Expoente da chave Privada:"+str(private_key_Exponent) + '\n')
    params_File.write("Expoente da chave Publica:"+str(public_key_Exponent) + '\n')
    params_File.write("Módulo:"+str(modulo) + '\n')
    
if __name__ == "__main__":
    main()
