# --*- encoding: utf-8 -*--
__author__ = 'Zhao, Yongjiang'
import re
from progressbar import progressbar
import os


class TestFilter(object):
    def __init__(self, fq):
        self.in_q = fq
        self.out_q = list()
        self.file_counter = 0
        self.filter_stopwords()
        filelist = os.listdir(os.getcwd())
        for f in filelist:
            if f[-4:] == ".out":
                os.remove(f)

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
                self.out_q.append(' '.join(job))
            else:
                break
        self.in_q = self.out_q
        self.out_q = list()
        return

    def filter_template(self, func, s=""):
        pb = progressbar(len(self.in_q), ".", s)
        ctr = 0
        while True:
            if self.in_q:
                ctr += 1
                pb.progress(ctr)
                job = self.in_q.pop()
                func(job)
            else:
                break
        print len(self.out_q)
        self.in_q = self.out_q
        self.out_q = list()
        return

    def filter_nums(self):
        def nums(job):
            temp = job.split()
            if len(temp) == 2:
                if re.match(r'\w+', temp[0]):
                    pass
                else:
                    self.out_q.append(job)
            elif len(temp) > 2:
                self.out_q.append(job)
        self.filter_template(nums, "remove lines with only numbers or alphabets.")
        self.output(str(self.file_counter) + ".out")
        return

    def filter_ads(self):
        pattern1 = r'.*(?:关注|微信|wechat|WX|QQ|V 信|加.{0,4}(?:扣|q|Q|qq)).*\d+.*'
        pattern2 = r'.*(?:互粉|求赞|求粉|求 关注|请 关注|(?:加|加个).{0,4}关注|关注.{0,4}我).*'
        pattern3 = r'.*(?:招|聘).*(?:暑假|寒假|宅家).*适合.*(?:学生|上班族).*'
        #pattern4 = r'.*A.{0,4}片.*加.*'
        pattern5 = r'.*職小時工.*'
        pattern6 = r'.*(?:工钱|日结|工资).*(?:小时|咨询).*(?:咨询|详情|详细).*'
        pattern7 = r'.*(?:学生|上班族).*(?:上班族|学生).*'
        self.filter_ad(pattern1)
        self.filter_ad(pattern2)
        self.filter_ad(pattern3)
        #self.filter_ad(pattern4)
        self.filter_ad(pattern5)
        self.filter_ad(pattern6)
        self.filter_ad(pattern7)
        return

    def filter_ad(self, pattern):
        def ad_pattern(job):
            if not re.match(pattern, job):
                self.out_q.append(job)
        self.filter_template(ad_pattern, "remove ads in comments.")
        self.output(str(self.file_counter) + ".out")

    def filter_nonsense(self):
        def nonsense(job):
            job_done = list()
            for words in job:
                try:
                    temp = words.encode("gbk")
                    job_done.append(temp)
                except:
                    pass
            if job_done > 1:
                self.out_q.append(job)
        self.filter_template(nonsense, "remove comments of nonsense.")
        self.output(str(self.file_counter) + ".out")
        return

    def output(self, filename="out_content.txt"):
        if filename == str(self.file_counter) + ".out":
            self.file_counter += 1
        print "saving ", filename
        f = open(filename, "wb")
        for o in self.in_q:
            f.write(o)
        f.close()
        return