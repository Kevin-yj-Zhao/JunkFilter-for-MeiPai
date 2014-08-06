#--*- encoding: utf-8 -*--
__author__ = 'Zhao Yongjiang'
import os
import random


def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip()
        dataMat.append(curLine)
    return dataMat


def RandomSampling(dataMat,number):
    try:
         slice = random.sample(dataMat, number)
         return slice
    except:
         print 'sample larger than population'


def cleancomment(filename):
    f = open(filename,'rb')
    try:
        string = "".join(map(lambda x: x.strip().decode("gb2312").encode("utf-8"), filter(lambda x: x.strip() != '', f.readlines())))
    except:
        return 0
    f.close()
    return string


def process(directory):
    f = open("jdcomment.txt", 'wb')
    for root, dirs, files in os.walk(directory):
        for filename in files:
            print os.path.join(*[root, filename])
            comment = cleancomment(os.path.join(*[root, filename]))
            if comment:
                f.write(comment + '\n')
    f.close()


if __name__ == "__main__":
    #process("Jingdong_NB_4000")
    data = loadDataSet("content.txt")
    res = RandomSampling(data, 4000)
    f = open("sampledjcomment.txt", 'wb')
    for r in res:
        try:
            f.write(r + '\n')
        except:
            pass
    f.close()
