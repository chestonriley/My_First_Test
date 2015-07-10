__author__ = 'fiestcheston1'

# Text is in file:  http://www.pythonlearn.com/code/mbox-short.txt

'''
7.2 Write a program that prompts for a file name, then opens that file and reads
through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the
lines and compute the average of those values and produce an output as shown below.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name.
'''


sumval = 0
countval = 0

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue

    fh1 = line.rstrip()
    pos1 = fh1.find(':')
    val1 = float(fh1[pos1+1:].strip())

    sumval = sumval + val1
    countval += 1

print "Average spam confidence:", sumval/countval

