def vowel_change(txt, vow):
    for char in 'aeiou':
        txt = txt.replace(char, vow)
    return txt
