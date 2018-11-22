# Project: Log Analysis

## The task:

"Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database."

The tool is supposed to answer three questions:

1. What are the three most popular articles of all time?

2. Who are the most popular authors of all time?

3. On what days did more than 1% of requests lead to errors?


## The Set-Up / Requirements:

Here's a list of <b>requirements</b> you'll need to run this program:

- Python 3 (https://www.python.org/downloads/)
- Psycopg2 (http://initd.org/psycopg/download/)
- PostgreSQL (https://www.postgresql.org/download/)

Now, let's set up our database:

First you want to start the psql program by cd-ing to your working directory (the one that contains all the code) and typing 'psql' into your command line.

From there you want to run the following query:
'CREATE DATABASE [newsdata];'

Mind you, the database file is in the same zip file this README came in.


Furthermore, to run this program you'll need to define a bunch of views:

### View 1: views

This view results in a table that counts the amount of views per
path (that did not result in an error).

SELECT log.path, count(*) AS num <br>
FROM log <br>
WHERE status = '200 OK' <br>
GROUP BY path <br>
ORDER BY num DESC;


### View 2: authorviews

In this view we are obtaining the total amount of views per author, referenced by their id.

SELECT articles.author, sum(views.num) AS num <br>
FROM articles, views <br>
WHERE views.path LIKE '%' || articles.slug <br>
GROUP BY author <br>
ORDER BY num DESC;

### View 3: viewsperday

This view gives us the amount of views (log entries) per day

SELECT date_trunc('day', log.time) "day", count(*) AS views <br>
FROM log <br>
GROUP BY 1 <br>
ORDER BY 1;

### View 4: failedviewsperday

Finally, in this view, we get the amount of failed requests per day

SELECT date_trunc('day', log.time) "day", count(*) AS failedrequests <br>
FROM log <br>
WHERE log.status != '200 OK' <br>
GROUP BY 1 <br>
ORDER BY 1;

## Concerning Git:

I've had a lot of trouble trying to push this repo to my remote repo. The main problem was that I made a few commits before pushing (or rather attempting to) for the first time and the first commit still included the database file which is too big to upload to Git.
As such, everytime I try to push, I get an error message that I'm pushing a file that's too big.
I've tried fixing this by removing the large file (which only appears in the initial commit) but that nearly made me lose my entire code.
I've decided to submit the project this way, and will know better for the future.

In the zip file you should see some images of my git log, just to show you that I've been using git along this project.
