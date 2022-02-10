def shifr_cezar(text, n):
    text = list(text)
    new_text = []
    for i in range(len(text)):
        if 65 <= ord(text[i]) <= 90:
            if (ord(text[i]) + n) <= 90:
                new_text.append(chr(ord(text[i]) + n))
            else:
                new_text.append(chr(((ord(text[i]) + n) - 90) + 64))
        if 97 <= ord(text[i]) <= 122:
            if (ord(text[i]) + n) <= 122:
                new_text.append(chr(ord(text[i]) + n))
            else:
                new_text.append(chr(((ord(text[i]) + n) - 122) + 96))
        if not 65 <= ord(text[i]) <= 90 and not 97 <= ord(text[i]) <= 122:
            new_text.append(text[i])
    return new_text


print(*(shifr_cezar("To be, or not to be, that is the question!", 17)), sep='')
