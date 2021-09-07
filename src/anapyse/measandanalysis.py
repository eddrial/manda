'''
Created on 7 Sep 2021

@author: oqb
'''
import argparse
import os
import h5py

import anapyse.anapyse_class as ac


if __name__ == '__main__':
    ### Set up Argument Parsing ###
    parser = argparse.ArgumentParser()
    
    ### set up argument helplines ###
    parser.add_argument("datafile", help = "datafile is the path to the measurement campaign. \nIf it does not exist, it is created. If it exists, it is modified.")
    
    args = parser.parse_args()
    
    print (args.datafile)
    
    #check for existance of datafile.
    if os.path.isfile(args.datafile):
        print ("{} exists.".format(args.datafile))
        
    elif not os.path.isfile(args.datafile):
        print("creating {}.".format(args.datafile))
        ac.Measurement_Campaign(args.datafile)
        
        f = h5py.File(args.datafile,"w")
        f.close()
        print("{} created.".format(args.datafile))
    