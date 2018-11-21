# Project: Log Analysis:




## Views:

### views

SELECT log.path, count(*) AS num
FROM log
WHERE status = '200 OK'
GROUP BY path
ORDER BY num DESC;


### authorviews

SELECT articles.author, sum(views.num) AS num
FROM articles, views
WHERE views.path LIKE '%' || articles.slug
GROUP BY author
ORDER BY num DESC;

### viewsperday

SELECT date_trunc('day', log.time) "day", count(*) AS views
FROM log
GROUP BY 1
ORDER BY 1;

### failedviewsperday

SELECT date_trunc('day', log.time) "day", count(*) AS failedrequests
FROM log
WHERE log.status != '200 OK'
GROUP BY 1
ORDER BY 1;