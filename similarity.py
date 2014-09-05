# --*- encoding: utf-8 -*--
__author__ = 'Zhao, Yongjiang'

import sys
sys.path.insert(0, "tmsvm\src")
import tms


def training(filename, path):
    tms.tms_train(filename, indexes=[1], main_save_path=path, seg=1, local_fun="tf", global_fun="one")


def predicting(filename, configfile, savepath):
    tms.tms_predict(filename, configfile, result_save_path=savepath, seg=1)


def analysis(filename, step):
    tms.tms_analysis(filename, step=step)


def main():
    #training("testcomments.txt", "balanced/")
    predicting("labeled_content.txt", "balanced/model/tms.config", "balanced/tms.result")
    analysis("balanced/tms.result", 1)


if __name__ == "__main__":
    main()