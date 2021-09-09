def remDuplicates(str):
    list = [0]*26
    print(str)
    out = ""
    for i in str:
        index = ord(i)-ord('a')
        if list[index] == 0:
            out = out + i
            list[index] = 1
    return str

if __name__ == "__main__":
    strings = ['aabb','abb','abcabcabc','a','aa','abcaaabc', 'abcaa', '']
    for i in strings:
        print(remDuplicates(i))