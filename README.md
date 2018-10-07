# Logs_analysis

The main objective of the Logs Analysis Project is to create a reporting tool that fetches the data from the database and prints out the report based on the data. This reporting tool is a Python program using the psycopg2 module to connect to the database.


## Installation Steps :
1. Install [Virtual Box](https://www.virtualbox.org/).<br>
2. Install [Vagrant](https://www.vagrantup.com/).<br>
3. Download or Clone the [repository](https://github.com/udacity/fullstack-nanodegree-vm).<br>
4. The downloaded file contains newsdata.sql with which you can work.<br>

## Steps to run :<br>
1. Change to the directory containing vagrant file.<br>
2. Run **vagrant up** to start.<br>
3. **vagrant ssh** to login into vm.<br>
4. Change directory to **cd /vagrant**.<br>
5. Use command **psql -d news -f newsdata.sql** to load database.<br>
    * Use **\c** to connect to database="news".<br>
    * Use **\dt** to see the tables in database.<br>
    * Use **\dv** to see the views in database.<br>
    * Use **\q** to quit the database.<br>
6. Use command **python log.py** to run the program.<br>

#### The tables in news database:
* The **authors** table includes information about the authors of articles.
* The **articles** table includes the articles themselves.
* The **log** table includes one entry for each time a user has accessed the site.

#### The project drives following conclusions:
* Most popular three articles of all time.
* Most popular article authors of all time.
* Days on which more than 1% of requests lead to errors.

### Functions in log.py:
* **connect():** Connects to the PostgreSQL database and returns a database connection.
* **cursor():** Allows Python code to execute PostgreSQL command in a database session.
* **fetchall():** Fetch all rows from the database table.
* **popular_article():** Prints most popular three articles of all time.
* **popular_authors():** Prints most popular article authors of all time.
* **largest_errors():** Print days on which more than 1% of requests lead to errors.

## Views :
#### article_view :
```
CREATE VIEW article_view AS
SELECT articles.title,articles.slug
FROM articles;
``` 
* articles table's two columns title and slug is used to create article_view.
#### article_count :
```
CREATE VIEW article_count AS
SELECT article_view.title,count(log.id) AS num
FROM article_view LEFT JOIN log ON log.path = ('/article/' || article_view.slug)
GROUP BY article_view.title;
```
* title column of article_view and count of id of log table is selected and left join is created to match the rows with similar path. || is the concatenation operator used here to match the right syntax of path in article_view and log table.
#### article_popularity :
```
CREATE VIEW article_popularity AS
SELECT article_count.title, article_count.num
FROM article_count ORDER BY num desc;
```
* title and num colums of article_count view are arranged in descending order and article_popularity view is created.
#### authors_view :
```
CREATE VIEW authors_view AS
SELECT authors.name,authors.id,articles.slug
FROM authors LEFT JOIN articles ON
articles.author = authors.id;
```
* name, id and slug columns of the authors table is used to create authors_view with the join condition of articles column of author table and authors id which needs to be same.
#### authors_article_view :
```
CREATE VIEW authors_article_view AS
SELECT authors_view.name,count(log.id) AS num1
FROM authors_view LEFT JOIN log on log.path = ('/article/'||authors_view.slug)
GROUP BY authors_view.name;
```
* name column of authors_view and count of id column of log table is used to create authors_article_view. authors_view is joined so that their path is matched and that is the join condition for the two. view is grouped by the name column of the authors_view view.
#### authors_popularity :
```
CREATE VIEW authors_popularity AS
SELECT authors_article_view.name, authors_article_view.num1
FROM authors_article_view
ORDER BY num1 DESC;
```
* name and num1 column of authors_article view are used to create authors_popularity view which is arranged in descending order.
#### date_time_error :
```
CREATE VIEW date_time_error AS
SELECT date(time),count(*)
FROM log WHERE status != '200 OK'
GROUP BY date(time);
```
* date_time_error is a view that has date extracted from the time column of the log table. The date along with the count is checked for the '200 OK' which represents the status of the requested resource. The condition is checked for the status code of != '200 OK'. The obtained result is then grouped based on the date in the log table and thus stored in date_time_error view. The date with error are basically stored here.
#### date_time :
```
CREATE VIEW date_time AS
SELECT date(time),count(*)
FROM log
GROUP BY date(time);
```
* The date with no errors and selected along with the count from log tableand stored in the date_time view. It is then grouped by date in the log table.
#### cond_error :
```
CREATE VIEW cond_error AS
SELECT to_char(date_time_error.date,'Month DD, YYYY') AS date,
to_char(((date_time_error.count::decimal/date_time.count::decimal)*100),'9.99') || '%' as percentage
FROM date_time_error, date_time
WHERE ((date_time_error.count::decimal/date_time.count::decimal)*100) > 1 and date_time.date = date_time_error.date;
```
* to char is used to convert the values into the required format of characters. date and percentage are selected and stored based on the condition that the error must be more than 1%.
## Output Screenshot :

<img src="https://github.com/Kedar5/Logs_analysis/blob/master/Output_Screenshot.png" alt="Output image">

## Acknowledgments :

* Thank you Udacity team for the continuous support through lectures.
