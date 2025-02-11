# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2024.

import sys, csv, re

codes = [{"code":"Eu02z13","system":"readv2"},{"code":"F11yz00","system":"readv2"},{"code":"F11x400","system":"readv2"},{"code":"Eu00012","system":"readv2"},{"code":"Eu00113","system":"readv2"},{"code":"F112.00","system":"readv2"},{"code":"F11xz00","system":"readv2"},{"code":"F11x200","system":"readv2"},{"code":"F11z.00","system":"readv2"},{"code":"F11x500","system":"readv2"},{"code":"F11x.00","system":"readv2"},{"code":"F11x700","system":"readv2"},{"code":"F11x000","system":"readv2"},{"code":"F11x800","system":"readv2"},{"code":"F11x600","system":"readv2"},{"code":"F11y.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('dementia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["dementia-p13-degen---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["dementia-p13-degen---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["dementia-p13-degen---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
