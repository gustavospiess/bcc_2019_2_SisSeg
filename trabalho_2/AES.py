

# word <- 4 bytes
# rouend_key <- 4 words
# key_list <- 11 round_keys
# Box <- matrix 16 X 16


S_BOX = [99, 202, 183, 4, 9, 83, 208, 81, 205, 96, 224, 231, 186, 112, 225,
        140, 124, 130, 253, 199, 131, 209, 239, 163, 12, 129, 50, 200, 120, 62,
        248, 161, 119, 201, 147, 35, 44, 0, 170, 64, 19, 79, 58, 55, 37, 181,
        152, 137, 123, 125, 38, 195, 26, 237, 251, 143, 236, 220, 10, 109, 46,
        102, 17, 13, 242, 250, 54, 24, 27, 32, 67, 146, 95, 34, 73, 141, 28,
        72, 105, 191, 107, 89, 63, 150, 110, 252, 77, 157, 151, 42, 6, 213,
        166, 3, 217, 230, 111, 71, 247, 5, 90, 177, 51, 56, 68, 144, 36, 78,
        180, 246, 142, 66, 197, 240, 204, 154, 160, 91, 133, 245, 23, 136, 92,
        169, 198, 14, 148, 104, 48, 173, 52, 7, 82, 106, 69, 188, 196, 70, 194,
        108, 232, 97, 155, 65, 1, 212, 165, 18, 59, 203, 249, 182, 167, 238,
        211, 86, 221, 53, 30, 153, 103, 162, 229, 128, 214, 190, 2, 218, 126,
        184, 172, 244, 116, 87, 135, 45, 43, 175, 241, 226, 179, 57, 127, 33,
        61, 20, 98, 234, 31, 185, 233, 15, 254, 156, 113, 235, 41, 74, 80, 16,
        100, 222, 145, 101, 75, 134, 206, 176, 215, 164, 216, 39, 227, 76, 60,
        255, 93, 94, 149, 122, 189, 193, 85, 84, 171, 114, 49, 178, 47, 88,
        159, 243, 25, 11, 228, 174, 139, 29, 40, 187, 118, 192, 21, 117, 132,
        207, 168, 210, 115, 219, 121, 8, 138, 158, 223, 22]

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

L_TABLE = [0, 100, 125, 101, 150, 102, 126, 43, 175, 44, 127, 204, 151, 83, 68,
        103, 0, 4, 194, 47, 143, 221, 110, 121, 88, 215, 12, 187, 178, 57, 17,
        74, 25, 224, 29, 138, 219, 253, 72, 10, 168, 117, 246, 62, 135, 132,
        146, 237, 1, 14, 181, 5, 189, 48, 195, 21, 80, 122, 111, 90, 144, 60,
        217, 222, 52, 52, 249, 33, 54, 191, 163, 155, 244, 235, 23, 251, 97,
        65, 35, 197, 2, 141, 185, 15, 208, 6, 182, 159, 234, 22, 196, 96, 190,
        162, 32, 49, 26, 129, 39, 225, 206, 139, 30, 94, 214, 11, 73, 177, 220,
        109, 46, 254, 198, 239, 106, 36, 148, 98, 66, 202, 116, 245, 236, 134,
        252, 71, 137, 24, 75, 76, 77, 18, 19, 179, 58, 78, 79, 89, 216, 59,
        188, 20, 180, 13, 199, 113, 78, 240, 92, 37, 107, 212, 174, 203, 67,
        82, 149, 42, 124, 99, 27, 8, 166, 130, 210, 226, 40, 172, 233, 95, 31,
        161, 207, 158, 184, 140, 104, 200, 114, 69, 241, 152, 84, 229, 213,
        176, 45, 108, 205, 93, 38, 128, 51, 248, 154, 53, 64, 34, 250, 243,
        231, 156, 164, 170, 55, 86, 119, 192, 238, 105, 201, 147, 70, 136, 133,
        115, 230, 169, 118, 85, 63, 242, 153, 247, 223, 28, 9, 218, 131, 145,
        61, 167, 173, 81, 123, 41, 91, 91, 227, 112, 3, 193, 120, 142, 56, 16,
        186, 87, 232, 160, 183, 157, 209, 171, 165, 7]

# | 00 00 19 01 34 02 1a c6 4b c7 1b 68 33 ee df 03 |
# | 64 04 e0 0e 34 8d 81 ef 4c 71 08 c8 f8 69 1c c1 |
# | 7d c2 1d b5 f9 b9 27 6a 4d 4e a6 72 9a c9 09 78 |
# | 65 2f 8a 05 21 0f e1 24 12 f0 82 45 35 93 da 8e |
# | 96 8f db bd 36 d0 ce 94 13 5c d2 f1 40 46 83 38 |
# | 66 dd fd 30 bf 06 8b 62 b3 25 e2 98 22 88 91 10 |
# | 7e 6e 48 c3 a3 b6 1e 42 3a 6b 28 54 fa 85 3d ba |
# | 2b 79 0a 15 9b 9f 5e ca 4e d4 ac e5 f3 73 a7 57 |
# | af 58 a8 50 f4 ea d6 74 4f ae e9 d5 e7 e6 ad e8 |
# | 2c d7 75 7a eb 16 0b f5 59 cb 5f b0 9c a9 51 a0 |
# | 7f 0c f6 6f 17 c4 49 ec d8 43 1f 2d a4 76 7b b7 |
# | cc bb 3e 5a fb 60 b1 86 3b 52 a1 6c aa 55 29 9d |
# | 97 b2 87 90 61 be dc fc bc 95 cf cd 37 3f 5b d1 |
# | 53 39 84 3c 41 a2 6d 47 14 2a 9e 5d 56 f2 5b ab |
# | 44 11 92 d9 23 20 2e 89 b4 7c b8 26 77 99 e3 a5 |
# | 67 4a ed de c5 31 fe 18 0d 63 8c 80 c0 f7 70 07 |

# TODO: validar se foi copiado direito

E_TABLE = [1, 95, 229, 83, 76, 131, 181, 254, 251, 195, 159, 155, 252, 69, 18,
        57, 3, 225, 52, 245, 212, 158, 196, 25, 22, 94, 186, 182, 31, 207, 54,
        77, 5, 56, 92, 4, 103, 185, 87, 43, 58, 226, 213, 193, 33, 74, 90, 221,
        15, 72, 228, 12, 169, 208, 249, 125, 78, 61, 100, 88, 99, 222, 238,
        124, 17, 216, 55, 20, 224, 107, 16, 135, 210, 71, 172, 232, 165, 121,
        41, 132, 51, 115, 89, 60, 59, 189, 48, 146, 109, 201, 239, 35, 244,
        139, 123, 151, 85, 149, 235, 68, 77, 220, 80, 173, 183, 64, 42, 101, 7,
        134, 141, 162, 255, 164, 38, 204, 215, 127, 240, 236, 194, 192, 126,
        175, 9, 145, 140, 253, 26, 247, 106, 79, 98, 129, 11, 47, 93, 91, 130,
        174, 27, 168, 143, 28, 46, 2, 190, 209, 166, 152, 29, 113, 231, 237,
        157, 37, 45, 227, 138, 36, 114, 6, 217, 104, 241, 179, 39, 147, 50, 44,
        188, 111, 119, 62, 133, 108, 150, 10, 112, 184, 8, 206, 105, 174, 86,
        116, 223, 177, 153, 66, 148, 180, 161, 30, 144, 211, 24, 73, 187, 233,
        250, 156, 122, 200, 176, 198, 167, 199, 248, 34, 171, 110, 40, 219,
        214, 32, 21, 191, 142, 67, 203, 81, 242, 82, 19, 102, 230, 178, 120,
        118, 97, 96, 63, 218, 137, 197, 70, 243, 13, 246, 53, 170, 49, 205,
        136, 154, 163, 160, 65, 117, 128, 84, 202, 14, 23, 1]

# | 01 03 05 0f 11 33 55 ff 1a 2e 72 96 a1 f8 13 35 |
# | 5f e1 38 48 d8 73 95 a4 f7 02 06 0a 1e 22 66 aa |
# | e5 34 5c e4 37 59 eb 26 6a be d9 70 90 ab e6 31 |
# | 53 f5 04 0c 14 3c 44 cc 4f d1 68 b8 d3 6e b2 cd |
# | 4c d4 67 a9 e0 3b 4d d7 62 a6 f1 08 18 28 78 88 |
# | 83 9e b9 d0 6b bd dc 7f 81 98 b3 ce 49 db 76 9a |
# | b5 c4 57 f9 10 30 50 f0 0b 1d 27 69 bb d6 61 a3 |
# | fe 19 2b 7d 87 92 ad ec 2f 71 93 ae e9 20 60 a0 |
# | fb 16 3a 4e d2 6d b7 c2 5d e7 32 56 fa 15 3f 41 |
# | c3 5e e2 3d 47 c9 40 c0 5b ed 2c 74 9c bf da 75 |
# | 9f ba d5 64 ac ef 2a 7e 82 9d bc df 7a 8e 89 80 |
# | 9b b6 c1 58 e8 23 65 af ae 25 6f b1 c8 43 c5 54 |
# | fc 1f 21 63 a5 f4 07 09 1b 2d 77 99 b0 cb 46 ca |
# | 45 cf 4a de 79 8b 86 91 a8 e3 3e 42 c6 51 f3 0e |
# | 12 36 5a ee 29 7b 8d 8c 8f 8a 85 94 a7 f2 0d 17 |
# | 39 4d dd 7c 84 97 a2 fd 1c 24 6c b4 c7 52 f6 01 |

# TODO: validar se foi copiado direito


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
    a = xor(text, key_list[0] + key_list[1] + key_list[2] + key_list[3])
    for i in range(1, 9): # add round key
        b = sub_bytes(a)
        c = shift_rows(b)
        d = mix_columns(c)
        a = xor(d, key_list[0+i*4] + key_list[1+i*4] + key_list[2+i*4] + key_list[3+i*4])
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
    d = list()
    for line in range(4):
        for column in range(4):
            value = 0
            # value = ''
            for i in range(4):
                text_input = c[line*4+i]
                mul_input = mul_matrix[column+i*4]
                # mul = "(" + str(text_input) + "*" + str(mul_input) + ")"
                # value += mul + " xor "
                mul = galois(text_input, mul_input)
                value = value ^ mul
            d.append(value)
    return d

def galois(b1, b2): # recebe 2 bytes retorna 1 byte
    """SPIESS"""

    if b1 == 0 or b2 == 1:  # TODO: validar se a excessão é referente à entrada
        return b1           #       ou ao que é obtido da tabela L
    if b2 == 0 or b1 == 1:
        return b2

    l1 = apply_box(b1, L_TABLE)
    l2 = apply_box(b2, L_TABLE)
    s = l1+l2 % 256

    e = apply_box(s, E_TABLE)
    return e
