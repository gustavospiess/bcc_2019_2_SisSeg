

# word <- 4 bytes
# rouend_key <- 4 words
# key_list <- 11 round_keys
# Box <- matrix 16 X 16


S_BOX = [99, 202, 183, 4, 9, 83, 208, 81, 205, 96, 224, 231, 186, 112, 225, 140, 124,
        130, 253, 199, 131, 209, 239, 163, 12, 129, 50, 200, 120, 62, 248, 161, 119,
        201, 147, 35, 44, 0, 170, 64, 19, 79, 58, 55, 37, 181, 152, 137, 123, 125, 38,
        195, 26, 237, 251, 143, 236, 220, 10, 109, 46, 102, 17, 13, 242, 250, 54, 24,
        27, 32, 67, 146, 95, 34, 73, 141, 28, 72, 105, 191, 107, 89, 63, 150, 110, 252,
        77, 157, 151, 42, 6, 213, 166, 3, 217, 230, 111, 71, 247, 5, 90, 177, 51, 56,
        68, 144, 36, 78, 180, 246, 142, 66, 197, 240, 204, 154, 160, 91, 133, 245, 23,
        136, 92, 169, 198, 14, 148, 104, 48, 173, 52, 7, 82, 106, 69, 188, 196, 70,
        194, 108, 232, 97, 155, 65, 1, 212, 165, 18, 59, 203, 249, 182, 167, 238, 211,
        86, 221, 53, 30, 153, 103, 162, 229, 128, 214, 190, 2, 218, 126, 184, 172, 244,
        116, 87, 135, 45, 43, 175, 241, 226, 179, 57, 127, 33, 61, 20, 98, 234, 31,
        185, 233, 15, 254, 156, 113, 235, 41, 74, 80, 16, 100, 222, 145, 101, 75, 134,
        206, 176, 215, 164, 216, 39, 227, 76, 60, 255, 93, 94, 149, 122, 189, 193, 85,
        84, 171, 114, 49, 178, 47, 88, 159, 243, 25, 11, 228, 174, 139, 29, 40, 187,
        118, 192, 21, 117, 132, 207, 168, 210, 115, 219, 121, 8, 138, 158, 223, 22]

# | 63 7c 77 7b f2 6b 6f c5 30 01 67 2b fe d7 ab 76 |
# | ca 82 c9 7d fa 59 47 f0 ad d4 a2 af 9c a4 72 c0 |
# | b7 fd 93 26 36 3f f7 cc 34 a5 e5 f1 71 d8 31 15 |
# | 04 c7 23 c3 18 96 05 9a 07 12 80 e2 eb 27 b2 75 |
# | 09 83 2c 1a 1b 6e 5a a0 52 3b d6 b3 29 e3 2f 84 |
# | 53 d1 00 ed 20 fc b1 5b 6a cb be 39 4a 4c 58 cf |
# | d0 ef aa fb 43 4d 33 85 45 f9 02 7f 50 3c 9f a8 |
# | 51 a3 40 8f 92 9d 38 f5 bc b6 da 21 10 ff f3 d2 |
# | cd 0c 13 ec 5f 97 44 17 c4 a7 7e 3d 64 5d 19 73 |
# | 60 81 4f dc 22 2a 90 88 46 ee b8 14 de 5e 0b db |
# | e0 32 3a 0a 49 06 24 5c c2 d3 ac 62 91 95 e4 79 |
# | e7 c8 37 6d 8d d5 4e a9 6c 56 f4 ea 65 7a ae 08 |
# | ba 78 25 2e 1c a6 b4 c6 e8 dd 74 1f 4b bd 8b 8a |
# | 70 3e b5 66 48 03 f6 0e 61 35 57 b9 86 c1 1d 9e |
# | e1 f8 98 11 69 d9 8e 94 9b 1e 87 e9 ce 55 28 df |
# | 8c a1 89 0d bf e6 42 68 41 99 2d 0f b0 54 bb 16 |

L_TABLE = None # TODO
E_TABLE = None # TODO


mul_matrix = [2, 1, 1, 3, 3, 2, 1, 1, 1, 3, 2, 1, 1, 1, 3, 2]
# | 2 3 1 1 |
# | 1 2 3 1 |
# | 1 1 2 3 |
# | 3 1 1 2 |


# Exemplo de key_list:
# [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],
#  [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],
#  [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],
#  [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],
#  [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],
#  [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],
#  [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],
#  [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],
#  [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],
#  [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],
#  [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]


def generate_round_keys(round_key_0): # recebe a primeira round key e retorna a lista com as 11
    """generates the round_key list (44 words) from a initial 4 words"""
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
    print(b1)
    """ROVIGO"""
    p1 = b1 % 16 # parte menos significativa (4 bits a direita)
    p2 = int((b1 - p1) / 16) # parte mais significativa (4 bits a esquerda)
    return box[p2+p1*16]


def generate_first_word(i, key_list): # recebe a lista de words e a posição da round key e retorna word
    """ROVIGO"""
    lw = key_list[(i-1)*4 + 3]
    fw = key_list[(i-1)*4]
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
        a = xor(d, key_list[i*4:i*4+3])
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
    lw.append(lw.pop(0))
    return lw
        

def sub_word(rw): # recebe word retorna word
    """ROVIGO"""
    return [apply_box(b, S_BOX) for b in rw]


def sub_bytes(a): # recebe 4 words retorna 4 words
    """SPIESS"""
    return [sub_word(w) for w in a]

def shift_rows(b): # recebe 4 words retorna 4 words
    """ROVIGO"""
    # TODO

def mix_columns(c): # recebe 4 words retorna words
    """SPIESS"""
    # TODO
