import sys
import glob
import numpy as np

#
# Simple parser to parse hte DNA-sequence
# from a generated text file.
#

def parseBasePairs(fileName, partitionLength):
    # load data
    data = np.loadtxt(fileName, dtype=np.dtype('|S1'), comments='#',
    delimiter=None, usecols=([3]));
    print('data loaded succesfully');

    # remove unknown base pairs and reshape data
    cleanData = [x for x in data if x!='I' and x!='-'];
    nbrRows = int(len(cleanData)//partitionLength);
    tidyData = cleanData[0:partitionLength*nbrRows];
    tidyData = np.reshape(tidyData,(nbrRows,partitionLength));

    return tidyData;

def generateFile(basePairs):
    # string representation
    separators = np.repeat([' '], basePairs.shape[0])[:,None];
    bp = np.concatenate((basePairs,separators),axis=1).tostring();

    print('starting file generation')
    text_file = open("sequence.txt", "w+");
    text_file.write(bp);
    text_file.close()

def main(argv=None):
    try:
        mode = sys.argv[1];
        partitionLength = sys.argv[2];
    except IndexError:
        print('Provide "test" or "full"  and the int length of each partition as input arguments when running script')
        sys.exit()

    if mode == 'test':
        fileName = 'short_test_file.txt';
    elif mode == 'full':
        fileName = 'genome_Josefin_Ondrus_Chigha_v4_Full_20161217035948.txt';
    else:
        print('Provide "test" or "full"')
        sys.exit()

    bp = parseBasePairs(fileName, int(partitionLength))
    generateFile(bp)
    print('sequence.txt is generated')

if __name__ == "__main__":
    sys.exit(main())
