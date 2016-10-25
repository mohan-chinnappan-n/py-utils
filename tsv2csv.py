import sys, csv
from optparse import OptionParser

# sample usage: python tsv2csv.py -i input.tsv -d "," --strip True -t ''> output.csv

parser = OptionParser()
parser.add_option("-i", "--infile",    dest="in_file", help="input tsv file" )
parser.add_option("-s", "--strip",     dest="b_strip", help="want to trim fields (eg: True|False)" )
parser.add_option("-d", "--delimiter",  dest="field_delimiter", help="field delimiter (eg: ,)" )
parser.add_option("-t", "--textdelimiter",  dest="text_delimiter", help="text field delimiter (eg: \")" )

(options, args) = parser.parse_args()

in_file = options.in_file
b_strip = options.b_strip
field_delimiter = options.field_delimiter
text_delimiter = options.text_delimiter



lst = list(csv.reader(open(in_file, 'rb'), delimiter='\t'))
for  rec in lst:
    outrec = ""
    for field in rec:
        if outrec == "":
            delimiter = ''
        else:
            delimiter = field_delimiter
        if b_strip == 'True' :
            outrec = outrec  + delimiter + text_delimiter + field.strip() + text_delimiter
        else:
            outrec = outrec + delimiter + text_delimiter + field + text_delimiter
    print outrec
