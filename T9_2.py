def convertor(i, msg):
    output = ""
    dic = {'a': 2, 'b': 22, 'c': 222, 'd': 3, 'e': 33, 'f': 333, 'g': 4, 'h': 44, 'i': 444,
    'j': 5, 'k': 55, 'l': 555, 'm': 6, 'n': 66, 'o': 666, 'p': 7, 'q': 77, 'r': 777, 's': 7777,
    't': 8, 'u': 88, 'v': 888, 'w': 9, 'x':99, 'y':999, 'z':9999, ' ':0}
    lastIn = " "
    for char in msg:
        num = str(dic[char])
        if lastIn[0] == num[0]:
            output = output + " "
        output = output + num
        lastIn = num
    print("Case #" + str(i) + ":", output)
 
def main():
    N = int(input())
    for i in range(1, N + 1):
        msg = input()
        convertor(i, msg)
 
if __name__ == '__main__':
    main()
