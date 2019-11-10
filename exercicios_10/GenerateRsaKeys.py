import rsa

def main():
    #create 2 random keysPairs public and private
    keysA = rsa.newkeys(1024)
    public_keyA = keysA[0]
    private_keyA = keysA[1]

    keysB = rsa.newkeys(1024)
    public_keyB = keysB[0]
    private_keyB = keysB[1]

    private_keyA_File_Path = "privateKeyA.txt"
    public_keyA_File_Path = "publicKeyA.txt"

    private_keyB_File_Path = "privateKeyB.txt"
    public_keyB_File_Path = "publicKeyB.txt"

    #save private key to file
    private_keyA_content = private_keyA.save_pkcs1()
    private_key_File = open(private_keyA_File_Path, 'wb')
    private_key_File.write(private_keyA_content)
    private_key_File.close()

    private_keyB_content = private_keyB.save_pkcs1()
    private_key_File = open(private_keyB_File_Path, 'wb')
    private_key_File.write(private_keyB_content)
    private_key_File.close()

    #save public key to file
    public_keyA_content = public_keyA.save_pkcs1()
    public_key_File = open(public_keyA_File_Path, 'wb')
    public_key_File.write(public_keyA_content)
    public_key_File.close()

    public_keyB_content = public_keyB.save_pkcs1()
    public_key_File = open(public_keyB_File_Path, 'wb')
    public_key_File.write(public_keyB_content)
    public_key_File.close()
    
if __name__ == "__main__":
    main()
