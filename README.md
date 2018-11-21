# Project: Log Analysis

## The task:

"Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database."

The tool is supposed to answer three questions:

1. What are the three most popular articles of all time?

2. Who are the most popular authors of all time?

3. On what days did more than 1% of requests lead to errors?

## The Set-Up:

To run this program you'll need to define a bunch of views:

### View 1: views

This view results in a table that counts the amount of views per
path (that did not result in an error).

SELECT log.path, count(*) AS num
FROM log
WHERE status = '200 OK'
GROUP BY path
ORDER BY num DESC;


### View 2: authorviews

In this view we are obtaining the total amount of views per author, referenced by their id.

SELECT articles.author, sum(views.num) AS num
FROM articles, views
WHERE views.path LIKE '%' || articles.slug
GROUP BY author
ORDER BY num DESC;

### View 3: viewsperday

This view gives us the amount of views (log entries) per day

SELECT date_trunc('day', log.time) "day", count(*) AS views
FROM log
GROUP BY 1
ORDER BY 1;

### View 4: failedviewsperday

Finally, in this view, we get the amount of failed requests per day

SELECT date_trunc('day', log.time) "day", count(*) AS failedrequests
FROM log
WHERE log.status != '200 OK'
GROUP BY 1
ORDER BY 1;