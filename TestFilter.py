# --*- encoding: utf-8 -*--
__author__ = 'ZhaoYongjiang'
import re
from progressbar import progressbar


class TestFilter(object):
    def __init__(self, fq):
        self.in_q = fq
        self.out_q = list()
        self.filter_stopwords()

    @staticmethod
    def init_stopwords():
        print "initializing stopwords list..."
        stopwords_set = set()
        f = open("stopwords_zh.txt", 'rb')
        lines = f.readlines()
        for line in lines:
            stopwords_set.add(line[:-1])
        return stopwords_set

    def filter_stopwords(self):
        stopwords = self.init_stopwords()
        pb = progressbar(len(self.in_q), ".", "remove stopwords")
        ctr = 0
        while True:
            if self.in_q:
                ctr += 1
                pb.progress(ctr)
                job = self.in_q.pop().split(',')
                job = filter(lambda x: x not in stopwords, job)
                self.out_q.append(job)
            else:
                break
        self.in_q = self.out_q
        self.out_q = list()
        return

    def filter_nums(self):
        pb = progressbar(len(self.in_q), ".", "remove lines with numbers only")
        ctr = 0
        while True:
            if self.in_q:
                job = self.in_q.pop()
                #temp = re.search(r'\d+\n', job)
                ctr += 1
                pb.progress(ctr)
                if len(job) <= 2:
                    if len(job) < 2:
                        continue
                    if re.match(r'\d+', job[0]):
                        continue
                self.out_q.append(job)
            else:
                break
        print len(self.out_q)
        self.in_q = self.out_q
        self.out_q = list()
        return

    def filter_ads(self):
        pb = progressbar(len(self.in_q), ".", "remove ads comments")
        ctr = 0
        while True:
            if self.in_q:
                ctr += 1
                pb.progress(ctr)
                job = self.in_q.pop()
                pattern1 = re.compile(r'.*(?:微信|QQ|V 信|加扣|加.{0,4}(?:扣|q|Q|qq)).*\d+.*')
                pattern2 = re.compile(r'.*(?:互粉|求赞|求 关注|请 关注).*')
                pattern3 = re.compile(r'.*招.*(?:暑假|寒假|宅家).*适合.*(?:学生|上班族).*')
                temp = pattern1.match(' '.join(job))
                if temp:
                    continue
                temp = pattern2.match(' '.join(job))
                if temp:
                    continue
                temp = pattern3.match(' '.join(job))
                if temp:
                    continue
                self.out_q.append(job)
            else:
                break
        print len(self.out_q)
        self.in_q = self.out_q
        self.out_q = list()
        return

    def filter_nonsense(self):
        pb = progressbar(len(self.in_q), ".", "remove comments with nonsense")
        ctr = 0
        while True:
            if self.in_q:
                ctr += 1
                pb.progress(ctr)
                job = self.in_q.pop()
                job_done = list()
                for words in job:
                    try:
                        temp = words.encode("gbk")
                        job_done.append(temp)
                    except:
                        pass
                if job_done > 1:
                    self.out_q.append(job)
                    #print job
            else:
                break
        print len(self.out_q)
        self.in_q = self.out_q
        self.out_q = list()
        return

    def output(self, filename="out_content.txt"):
        print "saving..."
        f = open(filename, "wb")
        for o in self.in_q:
            f.write(','.join(o))
        f.close()
        return