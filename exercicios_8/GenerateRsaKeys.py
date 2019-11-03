import rsa

def main():
    #create 2 random keys public and private
    keys = rsa.newkeys(512)
    public_key = keys[0]
    private_key = keys[1]

    #get the keys info
    private_key_Exponent = private_key.d
    public_key_Exponent = public_key.e 
    modulo = private_key.n

    #set the file path to save the info
    private_key_File_Path = "privateKey.txt"
    public_key_File_Path = "publicKey.txt"
    params_File_Path = "params.txt"

    #save private key to file
    private_key_content = private_key.save_pkcs1()
    private_key_File = open(private_key_File_Path, 'wb')
    private_key_File.write(private_key_content)
    private_key_File.close()

    #save public key to file
    public_key_content = public_key.save_pkcs1()
    public_key_File = open(public_key_File_Path, 'wb')
    public_key_File.write(public_key_content)
    public_key_File.close()

    #save aditional info
    params_File = open(params_File_Path,'w')
    params_File.write("Expoente da chave Privada:"+str(private_key_Exponent) + '\n')
    params_File.write("Expoente da chave Publica:"+str(public_key_Exponent) + '\n')
    params_File.write("Módulo:"+str(modulo) + '\n')
    params_File.close()
    
if __name__ == "__main__":
    main()
