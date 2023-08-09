# Cardoso V.,Nirantharakumar K.,Gkoutos G, 2023.

import sys, csv, re

codes = [{"code":"1C13.00","system":"readv2"},{"code":"1C13.11","system":"readv2"},{"code":"1C13200","system":"readv2"},{"code":"2BL..11","system":"readv2"},{"code":"2BL2.00","system":"readv2"},{"code":"2BL3.00","system":"readv2"},{"code":"2BL4.00","system":"readv2"},{"code":"2BL5.00","system":"readv2"},{"code":"2BM4.00","system":"readv2"},{"code":"A560200","system":"readv2"},{"code":"F59..11","system":"readv2"},{"code":"F591211","system":"readv2"},{"code":"F591500","system":"readv2"},{"code":"F596.00","system":"readv2"},{"code":"F59z.00","system":"readv2"},{"code":"F59z.11","system":"readv2"},{"code":"SJ15.12","system":"readv2"},{"code":"ZE87.11","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hearing-loss-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hearing-loss-deafness---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hearing-loss-deafness---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hearing-loss-deafness---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
