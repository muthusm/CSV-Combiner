#!/usr/bin/python
import os
import sys

def csv_combiner(filenames, outputfile='combined_csv.csv'):
    
    if all([filename.endswith('.csv') for filename in filenames]):
        header_done = False
        with open(outputfile, 'w') as outfile:
            for fname in filenames:
                filename = os.path.basename(fname)
                with open(fname) as infile:
                    if header_done:
                        next(infile)
                    for line in infile:
                        if not header_done:
                            outfile.write(line.replace('\n', '') + ',"filename"\n') 
                            header_done = True  
                        else:
                            outfile.write(line.replace('\n', '') + ',"' + filename + '"\n')
    else:
        print('Unsupported filenames are provided')

if __name__ == "__main__":
    filenames = sys.argv[1:] or ['fixtures/accessories.csv', 'fixtures/clothing.csv', 'fixtures/household_cleaners.csv']
    csv_combiner(filenames)
