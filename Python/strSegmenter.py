'''
7. String segmentation
You are given a dictionary of words and a large input string. You have to find out whether the input string can be completely segmented into the words of a given dictionary. The following two examples elaborate on the problem further.

Given a dictionary of words.

apple
apple
pear
pie

Input string of “applepie” can be segmented into dictionary words.

apple
pie
Input string “applepeer” cannot be segmented into dictionary words.

apple
peer

'''

def can_segment_string(s, dictionary):
  n = len(s)
  for i in range (1, n + 1):
    firstWord = s[0:i]
    if firstWord in dictionary:
      secondWord = s[i:]
      if secondWord in dictionary or can_segment_string(secondWord, dictionary):
        return True
  return False

#tested in browser