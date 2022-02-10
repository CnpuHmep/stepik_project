#   1040 ('А') по 1071 ('Я'), в нижнем регистре - с 1072 ('а') по 1103 ('я').
def shifr_cezar(text):
    text = list(text)
    new_text = []
    for i in range(len(text)):
        if 1040 <= ord(text[i]) <= 1071:
            if (ord(text[i]) + 10) <= 1071:
                new_text.append(chr(ord(text[i]) + 10))
