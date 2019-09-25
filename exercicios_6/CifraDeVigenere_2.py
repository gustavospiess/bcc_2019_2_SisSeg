import click

ALPHABET_LOWER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
ALPHABET_UPPER = [letter.upper() for letter in ALPHABET_LOWER]
ALPHABET = [*ALPHABET_LOWER, *ALPHABET_UPPER]

def cezar(texto, mod, key):
    key_map = [ALPHABET.index(letter) for letter in key]
    new_text = list()
    for ind, letter in enumerate(texto):
        if letter not in ALPHABET:
            new_text.append(letter)
        else:
            index = ALPHABET.index(letter)
            difference = mod * key_map[ind % len(key)]
            new_index = (ALPHABET.index(letter) + difference) % len(ALPHABET)
            new_text.append(ALPHABET[new_index])
    new_text = "".join(new_text)
    return new_text

@click.command()
@click.option('--decrypt', '-d', 'decrypt', help='set to decrypt (otherwise encrypt)', is_flag=True)
# @click.option('--debug', '-D', 'debug', help='debugging info will be printed', default=False, is_flag=True)
@click.option('--key', '-k', 'key', help='Key to be used', prompt='key')
@click.option('--text', '-t', 'text', help='text to be decrypt or encrypt', prompt='text')
def main(decrypt, debug, key, text):
    if(decrypt):
        new_text = cezar(text, -1, key)
        print(new_text)
    else:
        new_text = cezar(text, 1, key)
        print(new_text)
    
if __name__ == "__main__":
    main()
