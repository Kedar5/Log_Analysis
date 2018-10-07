# Logs_analysis

The main objective of the Logs Analysis Project is to create a reporting tool that fetches the data from the database and prints out the report based on the data. This reporting tool is a Python program using the psycopg2 module to connect to the database.


## Installation Steps:
1.Install [Virtual Box](https://www.virtualbox.org/)<br>
2.Install [Vagrant](https://www.vagrantup.com/)<br>
3.Download or Clone the [repository](https://github.com/udacity/fullstack-nanodegree-vm)<br>
4.You now have newsdata.sql with which u can work.<br>

## Steps to run:<br>
1. Change to the directory containing vagrant file<br>
2. Run **vagrant up** to start<br>
3. **vagrant ssh** to login into vm<br>
4. Change directory to **cd /vagrant**<br>
5. Use command **psql -d news -f newsdata.sql** to load database<br>
    -use **\c** to connect to database="news"<br>
    -use **\dt** to see the tables in database<br>
    -use **\dv** to see the views in database<br>
    -use **\q** to quit the database<br>
6. Use command **python log.py** to run the programm<br>

## Views
#### article_view
```
CREATE VIEW article_view AS 
SELECT articles.title,articles.slug
FROM articles;
``` 
#### article_count
```
CREATE VIEW article_count AS 
SELECT article_view.title,count(log.id) AS num
FROM article_view LEFT JOIN log ON log.path = ('/article/' || article_view.slug)
GROUP BY article_view.title;
```
#### article_popularity
```
CREATE VIEW article_popularity AS 
SELECT article_count.title, article_count.num
FROM article_count ORDER BY num desc;
```
#### authors_view
```
CREATE VIEW authors_view AS 
SELECT authors.name,authors.id,articles.slug
FROM authors LEFT JOIN articles ON
articles.author = authors.id;
```     
#### authors_article_view
```
CREATE VIEW authors_article_view AS 
SELECT authors_view.name,count(log.id) AS num1
FROM authors_view LEFT JOIN log on log.path = ('/article/'||authors_view.slug)
GROUP BY authors_view.name;
```
#### authors_popularity
```
CREATE VIEW authors_popularity AS
SELECT authors_article_view.name, authors_article_view.num1 
FROM authors_article_view 
ORDER BY num1 DESC;
```
#### date_time_error
```
CREATE VIEW date_time_error AS 
SELECT date(time),count(*) 
FROM log WHERE status != '200 OK'
GROUP BY date(time);
```
#### date_time
```
CREATE VIEW date_time AS 
SELECT date(time),count(*)
FROM log
GROUP BY date(time);
```
#### cond_error
```
CREATE VIEW cond_error AS 
SELECT to_char(date_time_error.date,'DD-MM-YYYY') AS date, 
to_char(((date_time_error.count::decimal/date_time.count::decimal)*100),'9.99') || '%' as percentage
FROM date_time_error, date_time
WHERE ((date_time_error.count::decimal/date_time.count::decimal)*100) > 1 and date_time.date = date_time_error.date;
```
## Screenshot

<img src="" alt="Website image">

## Acknowledgments

* Thank you Udacity team for the continuous support through lectures.
