import random
eng_morse = {
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--.."
}


words = ['cucumber', 'code', 'bit', 'sosiska', 'next']
answers = []

#ПЕРЕВОД
def eng_morse_encode(word):
  itog = ''
  for letter in word:
    encode_letter = eng_morse[letter]
    itog = itog + encode_letter
  return itog


#ВЗЯТЬ ИЗ СПИСКА СЛУЧАЙНО
def get_word(spisok):
  return random.choice(spisok)


def print_st(answers):
  all = len(answers)
  verno = answers.count(True)
  neverno = answers.count(False)

  return f'Всего задачек {all}, верно ответили на {verno}, неверно ответили на {neverno}'


print('Дарова. Нажми Enter и у тебя спишется 100 рублей с карты')
input('Нажмите Enter и начнём')

for x in range(5):
  random_word = get_word(words)
  encode_word = eng_morse_encode(random_word)
  print(f'СЛОВО: {encode_word}')
  user_input = input('Ваш ответ: ')
  if user_input == random_word:
    print('Верный ответ!')
    answers.append(True)
  else:
    print('Ответ неверный! Верный ответ: ', random_word)
    answers.append(False)

print(print.statistics(answers))