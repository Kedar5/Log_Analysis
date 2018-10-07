#!/usr/bin/env python2.7
# import psycopg2 module into the python code
import psycopg2


# Returns most popular three articles of all time
def popular_articles():
    # Establish connection with database and execute the query passed to it
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


# Returns most popular three authors of all time
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


# Returns date(s) with more than 1% of GET request errors
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

    
# Prints results for each query
if __name__ == '__main__':
    print "------------------------------------------------"
    popular_articles()
    print "------------------------------------------------\n"
    popular_authors()
    print "------------------------------------------------\n"
    largest_errors()
    print "------------------------------------------------"
