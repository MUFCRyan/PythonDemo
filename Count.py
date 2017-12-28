#coding=utf-8
import string

def main():
    str1=input("input:")
    l=0
    s=0
    d=0
    o=0

    for x in str1:
        if x.isalpha():
            l+=1
        elif x.isspace():
            s+=1
        elif x.isdigit():
            d+=1
        else:
            o+=1

    print('letter: %d, space: %d, digit: %d, other: %d'%(l,s,d,o))

if __name__ == '__main__':
    main()