# Cardoso V.,Nirantharakumar K.,Gkoutos G, 2023.

import sys, csv, re

codes = [{"code":"F582.00","system":"readv2"},{"code":"F590000","system":"readv2"},{"code":"F591000","system":"readv2"},{"code":"F59y.00","system":"readv2"},{"code":"FyuU100","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hearing-loss-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hearing-loss-specified---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hearing-loss-specified---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hearing-loss-specified---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
