import json
import pandas as pd

def texttolist(fromfile):
    fo = open(fromfile, "r")
    result = fo.read().split('\n')
    result = map(str.strip, result)
    result = filter(None, result)
    return result

def jsontotext(lists, filename):
    texts = []
    for k in lists:
        x = json.loads(k)
        texts.append(x['text'])
    fo = open(filename, "wb")
    for i in xrange(len(texts)):
        texts[i] = texts[i].encode('ascii', 'ignore').decode('ascii')
        fo.write(texts[i])
        fo.write("\n")
    fo.close()

def filterlist(lists):
    for i in reversed(xrange(len(lists))):
        strings = lists[i].split()
        for x in reversed(xrange(len(strings))):
            if strings[x].find('@') >= 0 or strings[x].find('http') >= 0:
                del strings[x]
        lists[i] = ' '.join(strings)
        if len(lists[i]) <= 3:
            del lists[i]
    return lists

def listtotext(lists, filename):
    fo = open(filename, "wb")
    lists = filterlist(lists)
    for i in xrange(len(lists)):
        fo.write(lists[i])
        fo.write("\n")
    fo.close()
    
def readcsv(filename):
    dataset = pd.read_csv(filename)
    negative = []
    positive = []
    for i in xrange(dataset.shape[0]):
        if (i + 1) % 10000 == 0:
            print 'done process ' + str(i + 1)
        try:
            string = ' '.join(dataset.ix[i][3].split())
            if dataset.ix[i][1] == 0:
                negative.append(string)
            else:
                positive.append(string)
        except:
            continue
    listtotext(negative, 'negativetweet')
    listtotext(positive, 'positivetweet')

jsontotext(texttolist('negative_tweets.json'), 'negative')
listtotext(texttolist('negative'), 'negative')
jsontotext(texttolist('positive_tweets.json'), 'positive')
listtotext(texttolist('positive'), 'positive')
readcsv('Sentiment Analysis Dataset.csv')