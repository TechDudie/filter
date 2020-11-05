#NO TYPO ALGORITHIMS IMPLEMENTED YET, IMPLEMENTION IS TOP PRIORITY.
file = open("words.txt")
words = file.read()
words = words.split("\n")
keyboardtypos = None
def filter(word):
  if word in words:
    return False
  else:
    return True
