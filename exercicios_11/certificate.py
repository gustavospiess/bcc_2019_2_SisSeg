import jks

keystore = jks.KeyStore.load('keystore.jks', 'passphrase')

print(ks.private_keys)
print(ks.certs)
print(ks.secret_keys)
