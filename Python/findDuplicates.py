#Find the first duplicate/repeated character in the string

def findDuplicate(str):
    for i in range(1, len(str)):
        if str[i-1] == str[i]:
            return str[i-1] + str[i]
    return ''

if __name__ == "__main__":
    strings = ['aabb','abb','abcabcabc','a','aa','abcaaabc', 'abcaa', '']
    for i in strings:
        print(findDuplicate(i))