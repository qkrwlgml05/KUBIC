import pandas as pd
from pandas import DataFrame as df

wf = df()
from_df = pd.read_csv('./ntst/nswords_find.csv')
from_df.columns = ['kp', 'kr']

file_n = open('./ntst/KUBIC_north.txt', 'r')
file_s = open('./ntst/KUBIC_south.txt', 'r')
file_final = open('./ntst/KUBIC_final.txt', 'w')
index = 1

while True:
    line_n = file_n.readline()
    line_s = file_s.readline()
    if line_n == '\n':
        continue
    if not line_n: break
    line_n = line_n.split('\t')
    line_s = line_s.split('\t')
    print(line_n)
    for i in range(len(line_n)-1):
        north = line_n[i]+'.'
        south = line_s[i]+'.'
        if i != 0:
            north = north[1:]
            south = south[1:]
        file_final.write('{0}\t{1}\n'.format(south, north))

file_n.close()
file_s.close()
file_final.close()
