import sys
import csv
import random
import numpy as np

def make_matrix(idx, session):
    
    # make list
    setTime=np.tile([2,2,2,6], (12))
    imgIdx=[i+1 for i in range(48)]
    np.random.shuffle(imgIdx)
    
    # printing
    print('-------Make Matrix--------') 
    print(setTime)
    print(imgIdx)
    print('--------------------------')
    
    # save as csv file
    fname='output/sub%s_%s_matrix.csv'%(idx,session)
    fout = open(fname, 'w', newline='')
    
    wout = csv.writer(fout)
    wout.writerow(setTime)
    wout.writerow(imgIdx)
    
    return fname, setTime, imgIdx

def main():
    idx=sys.argv[1]
    session=sys.argv[2]

    csvname, setTime, imgIdx  = make_matrix(idx, session)
    print('* Save ', csvname)

if __name__=='__main__':
    main()
