import os
from parameters import params as pm
str2num = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6,
 'g':7, 'h':8, 'i':9, 'j':10,'k':11,'l':12,
 'm':13,'n':14,'o':15,'p':16,'q':17,'r':18,
 's':19,'t':20,'u':21,'v':22,'w':23,'x':24,
 'y':25,'z':26,'%':27,',':28,'.':29,'?':30,
 "'":31,' ':32,'!':33}
def text2label(text):
    text = text + '%'
    label = [str2num[text[i].lower()] if text[i].lower() in str2num else 34 for i in range(len(text))]
    if len(label) <= pm.Tx:
        label += [0] * (pm.Tx - len(label))
    else:
        label = label[:pm.Tx]
    return label
