'''
8. Reverse Words in a Sentence
Reverse the order of words in a given sentence (an array of characters).

"Hello World" --> "World Hello"
'''

def str_rev(string, start, end):
  if string == None or len(string) < 2:
    return
  
  while start < end:
    temp = string[start]
    string[start] = string[end]
    string[end] = temp

    start += 1
    end -= 1
  return string 

def reverse_words(sentence):    # sentence here is an array of characters
  str_length = len(sentence)
  if sentence == None or str_length == 0:
    return
  
  sentence = str_rev(sentence, 0, str_length - 2) #reverse all the characters in sentence

  start = 0
  end = 0

  while True:
    while start < str_length and sentence[start] == " ":
      start += 1
    
    if start == str_length:
      break
    
    end = start + 1

    while end < str_length and sentence[end] != " " and sentence[end] != "\0":
      end += 1
    
    #use helper fucntion to reverse characters in place
    sentence = str_rev(sentence, start, end - 1)
    start = end
    
  return sentence

#tested in browser