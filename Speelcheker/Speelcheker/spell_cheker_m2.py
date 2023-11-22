from autocorrect import Speller

spell = Speller('ru')
# text = 'Проверкка текста на ашибки.'
text = 'Длинна реки, длина волос.'
print(spell(text))