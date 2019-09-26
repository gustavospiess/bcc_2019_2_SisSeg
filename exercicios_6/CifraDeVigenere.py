import os
import sys
import click
import logging

ALPHABET_LOWER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
ALPHABET_UPPER = [letter.upper() for letter in ALPHABET_LOWER]
ALPHABET = [*ALPHABET_LOWER, *ALPHABET_UPPER]

def vigenere(text, mod, key):
    """Encryption algorithm of Vigenere
    
    Mod  > A modifier to be applied to each char change (i.e.: 1 to do nothing; -1 to decrypt)
    Text > The text to be encrypted
    Key  > The key to be used in de encryption

    The only characters that this function replace is from a to z and A to Z (i.e.: [a-zA-Z])
    """
    logging.debug('Initialize process to mix text')
    logging.debug('Using key \'%s\'' % (key))
    logging.debug('Encoding %s characters' % (len(text)))
    key_map = [ALPHABET.index(letter) for letter in key]
    new_text = list()
    for ind, letter in enumerate(text):
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
@click.option('--debug', '-D', 'debug', help='debugging info will be printed', default=False, is_flag=True)
@click.option('--key', '-k', 'key', help='Key to be used', prompt='key')
@click.option('--text', '-t', 'text', help='text to be decrypt or encrypt')
@click.option('--input', '-i', 'input_file', help='input file')
@click.option('--output', '-o', 'output_file', help='output file')
def main(decrypt, debug, key, text, input_file, output_file):

    if debug:
        logging.basicConfig(level=logging.DEBUG)

    if not text and not input_file:
        logging.error('No input available.')
        return

    if input_file:
        logging.debug('Checking input file \'%s\'' % (input_file))
        if not os.path.isfile(input_file):
            logging.error('Input file not exists.')
            return

    if input_file:
        logging.debug('opening input file \'%s\'' % (input_file))
        with open(input_file, 'r') as fb:
            logging.debug('reading input')
            text = "".join(fb)

    logging.debug('Initialize process')

    new_text = None

    if(decrypt):
        logging.debug('Decrypting')
        new_text = vigenere(text, -1, key)
    else:
        logging.debug('Encryption')
        new_text = vigenere(text, 1, key)

    logging.info('Ending process, outputting')

    if output_file:
        logging.debug('Opening output file \'%s\'' % (output_file))
        with open(output_file, 'w') as fb:
            logging.debug('Writing output file \'%s\'' % (output_file))
            fb.write(new_text)
    else:
        logging.debug('Printing output')
        print(new_text)
    
if __name__ == "__main__":
    try:
        main()
    except Exception:
        logging.error('Unexpected error, run with -D flag for debug info')
        logging.debug(sys.exc_info()[1])
