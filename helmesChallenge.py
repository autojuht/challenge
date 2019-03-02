#!usr/bin/python3
import time
import argparse
tstart = time.process_time()


def anagramFinder(dictFilePath, word):

    word = ''.join(word)
    dictFilePath = ''.join(dictFilePath)
    keyword = sorted(word.lower())
    with open(dictFilePath, encoding='windows-1252') as f:
        words = f.read().splitlines()

    resList = ', '.join([w for w in words if sorted(str(w)) == keyword])
    return resList


tstop = time.process_time()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dictFilePath', help='path to file', nargs=1, type=str)
    parser.add_argument('word', help='the word to find an anagram to', nargs=1, type=str)
    args = parser.parse_args()
    print(str(round((tstop - tstart) * 1000000, 2)) + ' ms,', anagramFinder(args.dictFilePath, args.word))
