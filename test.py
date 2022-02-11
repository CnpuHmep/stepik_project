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


s = []
n = 'Day, mice.'.split()

for i in range(len(n)):
    count = 0
    for m in n[i]:

        if 65 <= ord(m) <= 90 or 97 <= ord(m) <= 122:
            count += 1
    s += shifr_cezar(n[i], count)
print(*s)
