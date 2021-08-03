import string
import argparse
import random
import math

# global variables assigned
# extract words from words.txt
# assumes each word is on its own line, no quotes/spaces/etc.
def words_from_file():
  f = open('/Users/admin/Desktop/Projects/Python/Password-Maker/words.txt', 'r')
  lines = f.readlines()
  f.close()

  # remove \n
  words = [line[:-1] for line in lines]
  return words

# extracts a random word from a list of words
def random_word(words):
  # SystemRandom relies on /dev/urandom
  r = random.SystemRandom()
  return r.choice(words)

# extracts n random words from a list of words
def random_words(words, n):
  chosen = []
  for i in range(n):
    new_word = random_word(words)
    chosen.append(new_word)
  return chosen

def entropy_per_word(words):
  n = len(words)
  return math.log(n, 2)

def args():
  parser = argparse.ArgumentParser(description='Randomly generate a password from a list of words')
  parser.add_argument('-n', '--num', help='Number of words to generate. Defaults to 5.', type=int, default=5)
  args = parser.parse_args()
  return args

passlen = 8
def pw_gen(size = passlen, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

def run(num):
  print ("Chosen Words:\n")
  with open('PWDs.txt', 'w') as fr:
      for i in range(35):
          words = words_from_file()
          chosen = random_words(words, num)
          entropy = entropy_per_word(words)
          total_entropy = entropy*num
          mixer=[]
          for word in chosen:
            print (word)
            mixer+=word.title()
          passwd=(''.join(mixer) + pw_gen())
          fr.write(passwd + "\n")
  print ("\nEntropy Per Word: " + str(entropy))
  print ("Total Entropy: " + str(total_entropy) + '\n')
  print ('Password: ' + ''.join(mixer) + pw_gen())
  if total_entropy >= 80:
    print ('\nAcceptable Enthropy')
  else:
    print ('\nUnacceptable Enthropy. Retry.')
if __name__ == '__main__':
  args = args()
  n = args.num
  run(n)
