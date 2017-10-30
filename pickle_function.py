import dill
import pickle
import re
def clearstring(string):
    string = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', string, flags=re.MULTILINE)
    string = re.sub('[^@#A-Za-z0-9 ]+', '', string)
    string = string.split(' ')
    string = filter(None, string)
    string = [y.strip() for y in string]
    string = ' '.join(string)
    return string.lower()

def pickle_function(func, name):
    g = dill.dumps(func)
    with open(name + '.p', 'wb') as fopen:
        pickle.dump(g, fopen)

def unpickle_function(name):
    with open(name + '.p', 'rb') as fopen:
        func = pickle.load(fopen)
    return dill.loads(func)

string = 'Ricky Wilson The Best FRONTMAN/Kaiser Chiefs The Best BAND Xxxx Thank you Kaiser Chiefs for an incredible year of gigs and memories to cherish always :) Xxxxxxx'
print(clearstring(string))
pickle_function(clearstring, 'clearstring')
g = unpickle_function(g, 'clearstring')
print(g(string))