import csv

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(['fromID,' + 'toID'])
    with open('Cit-HepPh.txt', 'r') as f:
        for lines in f:
            if lines[0] == '#':
                pass
            else:
                (fromID, toID) = lines.split()
                writer.writerow([fromID + ',' + toID])