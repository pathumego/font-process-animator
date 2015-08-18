# -*- coding: utf-8 -*-

import os, sys

def genFonts(fileName, outputDir):
    os.system('mkdir -p ' + outputDir)
    os.system('git log --pretty=%h ' + fileName + ' > ' + outputDir + 'gitlogtmp')
    commits = open(outputDir + 'gitlogtmp').read().splitlines()
    ##print(commits)

    count = 1
    try:
        for commitHash in commits:
            os.system('git checkout ' + commitHash)
            outputFileName =  str(count) + fileName
            os.system('cp ' + fileName + ' ' + outputDir +
            outputFileName)

        os.sytem('rm ' + outputDir +'gitlogtmp')

    except:
        print("log file read error or no git commits...")

def main(argv):
    genFonts(argv[1], argv[2])

if __name__ == "__main__":
    main(sys.argv)
