import rsa

def main():
    keys = rsa.newkeys(512)
    public_Key = keys[0]
    private_Key = keys[1]
    
    private_Key_Exponent = private_Key.d
    public_Key_Exponent = public_Key.e 
    modulo = private_Key.n
    
    private_Key_File_Path = "privateKey.txt"
    public_Key_File_Path = "publicKey.txt"
    params_File_Path = "params.txt"
    
    private_Key_File = open(private_Key_File_Path, 'w')
    private_Key_File.write(str(private_Key))
    private_Key_File.close()

    public_Key_File = open(public_Key_File_Path, 'w')
    public_Key_File.write(str(public_Key))
    public_Key_File.close()

    params_File = open(params_File_Path,'w')
    params_File.write(str(private_Key_Exponent) + '\n')
    params_File.write(str(public_Key_Exponent) + '\n')
    params_File.write(str(modulo) + '\n')
    
if __name__ == "__main__":
    main()
