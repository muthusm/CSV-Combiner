#!/usr/bin/env python3
import os
import sys

def csv_combiner(filenames):
    if all([filename.endswith('.csv') for filename in filenames]):
        header_done = False
        for fname in filenames:
            filename = os.path.basename(fname)
            with open(fname) as infile:
                if header_done:
                    next(infile)
                for line in infile:
                    if not header_done:
                        sys.stdout.write(line.replace('\n', '') + ',"filename"\n')    
                        header_done = True  
                    else:
                        sys.stdout.write(line.replace('\n', '') + ',"' + filename + '"\n')
    else:
        print('Unsupported filenames are provided')

if __name__ == "__main__":
    filenames = sys.argv[1:]
    if filenames:
        csv_combiner(filenames)