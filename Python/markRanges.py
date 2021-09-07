#Take the students Mark as User input and check the range of Mark

def findRange(marks):
    lowest = 101
    greatest = -1
    for i in marks:
        if i > greatest:
            greatest = i
        elif i < lowest:
            lowest = i
        print("greatest: "+str(greatest))
        print("lowest: "+str(lowest))
    return greatest-lowest

if __name__ == "__main__":
    print(findRange([30, 75, 45, 20, 89, 60, 57]))