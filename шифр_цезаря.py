#   1040 ('А') по 1071 ('Я'), в нижнем регистре - с 1072 ('а') по 1103 ('я').
def shifr_cezar(text, n):
    text = list(text)
    new_text = []
    for i in range(len(text)):
        if 1040 <= ord(text[i]) <= 1071:
            if (ord(text[i]) + n) <= 1071:
                new_text.append(chr(ord(text[i]) + n))
            else:
                new_text.append(chr(((ord(text[i]) + n) - 1071) + 1039))
        if 1072 <= ord(text[i]) <= 1103:
            if (ord(text[i]) + n) <= 1103:
                new_text.append(chr(ord(text[i]) + n))
            else:
                new_text.append(chr(((ord(text[i]) + n) - 1103) + 1072))
        if not 1040 <= ord(text[i]) <= 1071 and not 1072 <= ord(text[i]) <= 1103:
            new_text.append(text[i])
    return new_text


print(*(shifr_cezar('Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг', -7)), sep='')
