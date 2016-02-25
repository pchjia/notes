#!/bin/env python3

import csv
import re
import json
import codecs


def main():
    f = open('beijing_jt.csv', 'r')
    csv_reader = csv.reader(f)
    result = {}
    rev_result = {}
    next(csv_reader)
    for row in csv_reader:
        name = row[1]
        desc = row[-1]
        desc = desc.replace('\n', '')
        desc = re.sub('\d', '', desc)
        desc = re.split('\s+', desc)
        desc = [i for i in desc if len(i) > 0]
        result[name] = desc
    f.close()

#    f = codecs.open('beijing_bus.json', 'w', 'utf-8')
#    json.dump(result, f)
#    f.close()
#    for res in result:
#        print(res + ': ' + str(result[res]))

    for res in result:
        for station in result[res]:
            key = station
            val = res
            if rev_result.get(key):
                rev_result.get(key).append(val)
            else:
                rev_result[key] = [val]

    for res in rev_result:
        print(res + ": " + str(rev_result[res]))
        print('')
    f = open('beijing_station.json', 'w')
    json.dump(rev_result, f)
    f.close()


if __name__ == '__main__':
    main()
