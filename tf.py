# --*- encoding: utf-8 -*--
__author__ = 'Zhao, Yongjiang'

import jieba
from progressbar import progressbar
import sys


num_of_line = 0

def init(filename):
    global num_of_line
    print "initializing..."
    comments_list = list()
    f = open(filename, 'rb')
    reader = f.readlines()
    for line in reader:
        #comments_list.append(line)
        comments_list.append(line)
    print len(comments_list)
    num_of_line = len(comments_list)
    return comments_list


def process(content):
    global num_of_line
    pb = progressbar(num_of_line)
    ctr = 0
    worddict = dict()
    wordlist = list()
    for item in content:
        ctr += 1
        pb.progress(ctr)
        seg_list = jieba.cut(item)
        for word in seg_list:
            if worddict.has_key(word):
                worddict[word] += 1
            else:
                worddict[word] = 1
    print "total words:", len(worddict)
    temp = list()
    for k, v in worddict.iteritems():
        temp.append([k, v])
    wordlist = sorted(temp, key=lambda x: x[1], reverse=True)
    f = open("terms.txt", 'wb')
    for word in wordlist:
        f.write(word[0] + '\t' + str(word[1]) + '\n')
    f.close()


def segment(content):
    global num_of_line
    pb = progressbar(num_of_line)
    ctr = 0
    contentlist = list()
    for item in content:
        ctr += 1
        pb.progress(ctr)
        seg_list = jieba.cut(item)
        contentlist.append(','.join(seg_list))
    f = open("seged_content.txt", 'wb')
    for sentence in contentlist:
        f.write(sentence.encode("utf-8"))
    f.close()


if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding("utf-8")
    #clist = init("content.txt")
    clist = init(sys.argv[1])
    #process(clist)
    segment(clist)
