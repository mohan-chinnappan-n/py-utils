import csv,json,sys

from optparse import OptionParser

# sample usage: python csv2jon.py --infile output.csv

parser = OptionParser()
parser.add_option("-i", "--infile",    dest="in_file", help="input csv file" )
parser.add_option("-p", "--pretty",     dest="pretty", help="pretty (eg: pretty|nopretty)" )

(options, args) = parser.parse_args()
in_file = options.in_file
pretty = options.pretty


def read_csv(csv_infile, format):
    csv_rows = []
    with open(csv_infile) as csvfile:
         reader = csv.DictReader(csvfile)
         title = reader.fieldnames
         for row in reader:
                 csv_rows.extend( [{title[i]:row[title[i]] for i in range(len(title))}] )
         write_json(csv_rows, format)


def write_json(data, format):
        if format == "pretty":
            print(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
        else:
            print(json.dumps(data))





read_csv(in_file, pretty)
