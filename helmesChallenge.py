#!usr/bin/python3
import time
import argparse


def anagramFinder(dictFilePath, word):

    tstart = time.process_time()
    word = ''.join(word)
    dictFilePath = ''.join(dictFilePath)
    keyword = sorted(word.lower())
    with open(dictFilePath, encoding='windows-1252') as f:
        words = f.read().splitlines()

    resList = ', '.join([w for w in words if sorted(str(w)) == keyword])

    tstop = time.process_time()
    return str(round((tstop - tstart) * 1000000, 2)) + ' ms, ' + resList


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dictFilePath', help='path to file', nargs=1, type=str)
    parser.add_argument('word', help='the word to find an anagram to', nargs=1, type=str)
    args = parser.parse_args()
    print(anagramFinder(args.dictFilePath, args.word))
