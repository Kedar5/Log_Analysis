#!/usr/bin/env python2.7

import psycopg2


def popular_articles():

    my_db = psycopg2.connect(database="news")
    query1 = """SELECT * from article_popularity limit 3"""
    cur1 = my_db.cursor()
    cur1.execute(query1)
    result1 = cur1.fetchall()
    print "Three most popular articles :\n"
    for data in result1:
        print "%s - %d views" % (data[0], data[1])
    my_db.close()
    cur1.close()


def popular_authors():
    my_db = psycopg2.connect(database="news")
    query2 = """select * from authors_popularity"""
    cur2 = my_db.cursor()
    cur2.execute(query2)
    result2 = cur2.fetchall()
    print "The most popular article authors :\n"
    for data in result2:
        print "%s - %d views" % (data[0], data[1])
    my_db.close()
    cur2.close()


def largest_errors():
    my_db = psycopg2.connect(database="news")
    query3 = """select * from cond_error"""
    cur3 = my_db.cursor()
    cur3.execute(query3)
    result3 = cur3.fetchall()
    print "The Day with more than 1% error :\n"
    for data in result3:
        print "%s - %s errors" % (data[0], data[1])
    my_db.close()
    cur3.close()


if __name__ == '__main__':
    print "------------------------------------------------"
    popular_articles()
    print "------------------------------------------------\n"
    popular_authors()
    print "------------------------------------------------\n"
    largest_errors()
