import string
#get alphabet
alphabet = string.ascii
#get words
file = open("words.txt")
words = file.read()
words = words.split("\n")
def filter(word):
  if word in words:
    return False
  x = len(word)
  word_chars = list(word)
  for i in range(0, x-1):
    for letter in alphabet:
      word_chars[i] = letter
      edit_word = ""
      edit_word.join(word_chars)
      if edit_word in words:
        return False
      word_chars = list(word)
  return True
