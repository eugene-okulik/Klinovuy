text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel.' \
       'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'

list_text = text.split()
ing_text = []

for element in list_text:
    if element[-1] in ',.':
        word = element[:-1]
        symbol = element[-1]
        ing_text.append(f'{word}ing{symbol}')
    else:
        ing_text.append(f'{element}ing')
text = ' '.join(ing_text)
print(text)
