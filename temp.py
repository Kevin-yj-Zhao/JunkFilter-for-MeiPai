# --*- encoding: utf-8 -*--
__author__ = 'Zhao, Yongjiang'
import csv


def main():
    fin = open("testpositivecomment.txt", 'rb')
    fout = open("testpositivecomments.txt", 'wb')
    reader = fin.readlines()
    for line in reader:
        if line[0] == "1":
            fout.write(line)
    fin.close()
    fout.close()


if __name__ == "__main__":
    main()