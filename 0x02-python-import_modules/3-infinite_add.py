#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    add = 0
    for j in range(i - 1):
        add += int(sys.argv[j + 1])
    print("{}".format(add))
