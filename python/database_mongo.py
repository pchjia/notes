#!/bin/env python3
# coding: utf-8

import pymongo


def main():
    con = pymongo.MongoClient()
    tdb = con.database_name
    cur = tdb.table_name # tdb['table_name']

    dic1 = {'name': 'pchjia', 'age': 23, 'school': 'hnu'}
    cur.insert(dic1)
#    post_info.remove({'name': 'pchjia'})

if __name__ == '__main__':
    main()
