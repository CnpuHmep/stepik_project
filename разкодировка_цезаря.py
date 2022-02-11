def shifr_cezar(text, n):
    text = list(text)
    new_text = []
    for i in range(len(text)):
        if 65 <= ord(text[i]) <= 90:
            if (ord(text[i]) - n) >= 65:
                new_text.append(chr(ord(text[i]) - n))
            else:
                new_text.append(chr(91 - (65 - (ord(text[i]) - n))))
        if 97 <= ord(text[i]) <= 122:
            if (ord(text[i]) - n) >= 97:
                new_text.append(chr(ord(text[i]) - n))
            else:
                new_text.append(chr(123 - (97 - (ord(text[i]) - n))))
        if not 65 <= ord(text[i]) <= 90 and not 97 <= ord(text[i]) <= 122:
            new_text.append(text[i])
    return new_text


for i in range(1, 26):
    print(*(shifr_cezar("Hawnj pk swhg xabkna ukq nqj.", i)), sep='')
