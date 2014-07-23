# --*- encoding: utf-8 -*--
__author__ = 'Zhao, Yongjiang'

from TestFilter import TestFilter
import os


def init(filename):
    print "initializing..."
    comments_list = list()
    f = open(filename, 'rb')
    reader = f.readlines()
    for line in reader:
        #comments_list.append(line)
        comments_list.append(line)
    print len(comments_list)
    return comments_list


def main():
    if not os.path.exists("seged_content.txt"):
        os.system("tf.python")
    clist = init("seged_content.txt")
    comment_filter = TestFilter(clist)
    comment_filter.filter_nums()
    #comment_filter.filter_nonsense()
    comment_filter.filter_ads()
    comment_filter.output()

if __name__ == "__main__":
    main()


