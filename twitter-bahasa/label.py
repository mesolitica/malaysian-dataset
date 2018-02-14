import os
import pickle

files = os.listdir(os.getcwd())
del files[files.index('label.py')]
for i in reversed(xrange(len(files))):
    if files[i].find('.p') >= 0 or files[i].find('-processed') >= 0:
        del files[i]
for i in xrange(len(files)):
    with open(files[i], 'r') as fopen:
        sentences = fopen.read().split('\n')
    sentences = filter(None, sentences)
    print '1 for negative, 2 for positive'
    answers = []; starting = 0
    print files[i] + ' got ' + str(len(sentences)) + ' of sentences'
    try:
        with open(files[i] + '.p', 'r') as fopen:
            answers = pickle.load(fopen)
        starting = len(answers)
    except Exception as e:
        print 'no checkpoint found'
    for no in xrange(starting, len(sentences)):
        while True:
            ans = raw_input(str(no + 1) + '. ' + sentences[no] + ': ')
            try:
                if int(ans) == 1 or int(ans) == 2:
                    answers.append(ans)
                    with open(files[i] + '.p', 'wb') as fopen:
                        pickle.dump(answers, fopen)
                    break
            except Exception as e:
                print e
                continue
    with open(files[i] + '-processed', 'wb') as fopen:
            for no, k in enumerate(sentences):
                answer = 'negative' if int(answers[no]) == 1 else 'positive'
                fopen.write(k + '+++++' + answer + '\n')
                