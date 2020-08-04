import os, sys
import csv
import random
import numpy as np

def check_file(fname):
    if os.path.isfile(fname):
         while True:
             answer = input('* %s is Already Exist. Continue? (y / n)'%fname)
             if answer=='y':
                 print('* Save %s'%fname)
                 break
             elif answer=='n':
                 sys.exit()
             else:
                 print('Answer y or n ')
    else:
        print('* Save %s'%fname)

def make_list():
    
    blockTime=[2,2,2,6]
    setTime=[]
    for i in range(10):
        setTime.extend(blockTime)
    setTime=[time for i in range(10) for time in blockTime]
    
    imgIdx=[i+1 for i in range(40)]
    np.random.shuffle(imgIdx)
    
    return setTime, imgIdx

def make_matrix(idx, session):
    fname='output/sub%s_%s_matrix.csv'%(idx,session)
    fout = open(fname, 'w', newline='')
    wout = csv.writer(fout)
    
    setTime, imgIdx = make_list()
    wout.writerow(setTime)
    wout.writerow(imgIdx)
    print('-------Make Matrix--------') 
    print(setTime)
    print(imgIdx)
    print('--------------------------')
    return fname

def main():
    idx = '00'
    session='00'
    if len(sys.argv)>1:
        idx=sys.argv[1]
        session=sys.argv[2]
    fname = make_matrix(idx, session)

if __name__=='__main__':
    main()
