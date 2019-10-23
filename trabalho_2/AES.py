

# word <- 4 bytes
# rouend_key <- 4 words
# key_list <- 11 round_keys
# Box <- matrix 16 X 16


S_BOX = None # TODO
L_TABLE = None # TODO
E_TABLE = None # TODO


mul_matrix = [2, 1, 1, 3, 3, 2, 1, 1, 1, 3, 2, 1, 1, 1, 3, 2]
# | 2 3 1 1 |
# | 1 2 3 1 |
# | 1 1 2 3 |
# | 3 1 1 2 |


def generate_round_keys(round_key_0): # recebe a primeira round key e retorna a lista com as 11
    """SPIESS"""
    key_list = [None for x in range(44)]
    key_list[0] = round_key_0[0]
    key_list[1] = round_key_0[1]
    key_list[2] = round_key_0[2]
    key_list[3] = round_key_0[3]
    for i in range(1, 10):
        fw = generate_first_word(i, key_list)
        key_list[i*4] = fw
        for j in range(1, 3):
            lw = key_list[i*4 + j - 1]
            ew = key_list[i*4 + j - 4]
            w = xor(lw, ew)
            key_list[i*4+j] = w
    return key_list


def apply_box(b1, box): # recebe uma byte e uma box, retorna uma word
    """ROVIGO"""
    p1 = b1 % 16 # parte menos significativa (4 bits a direita)
    p2 = b1 - p1 # parte mais significativa (4 bits a esquerda)
    return box[p1][p2]


def generate_first_word(i, key_list): # recebe a lista de words e a posição da round key e retorna word
    """ROVIGO"""
    lw = None # TODO copiar última word da rq i - 1
    fw = None # TODO copiar primeira word da rq i - 1
    rw = rot_word(lw)
    sw = sub_word(rw)
    rc = generate_round_constant(i)
    result = xor(sw, rc)
    result = xor(fw, result)
    return result


def cyfer(text, key_list):
    """ROVIGO"""
    a = xor(text, key_list[0:3])
    for i in range(1, 9): # add round key
        b = sub_bytes(a)
        c = shift_rows(b)
        d = mix_columns(c)
        a = xor(d, key_list[i*4:i*4+3]
    b = sub_bytes(a)
    c = shift_rows(b)
    e = xor(c, key_list[-4:])
    return e


def generate_round_constant(i): # retorna word
    """SPIESS"""
    return [0, 0, 0, i]


def xor(w1, w2): # recebe duas words retorna word
    """Xor operation for every pair w1i w2i"""
    return [p1 ^ p2 for p1, p2 in zip(w1, w2)]


def rot_word(lw): # recebe word retorna word
    """ROVIGO"""
    # TODO


def sub_word(rw): # recebe word retorna word
    """ROVIGO"""
    # TODO


def sub_bytes(a): # recebe word retorna word
    """SPIESS"""
    # TODO

def shift_rows(b): # recebe word retorna word
    """ROVIGO"""
    # TODO

def mix_columns(c): # recebe word retorna word
    """SPIESS"""
    # TODO

