alphabet = "qwertyuiopasdfghjklzxcvbnm"
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
      for x in word_chars:
        edit_word += x
      if edit_word in words:
        return True
      word_chars = list(word)
  return False
