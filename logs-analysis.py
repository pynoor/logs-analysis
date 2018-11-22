#!/usr/bin/env python3
import psycopg2

db = psycopg2.connect(database="news")
c = db.cursor()

top_three_articles_query = '''
SELECT articles.title, views.num
FROM articles, views
WHERE views.path LIKE '%' || articles.slug
ORDER BY num DESC
LIMIT 3;'''

top_authors_query = '''
SELECT authors.name, authorviews.num
FROM authorviews, authors
WHERE authors.id = authorviews.author;'''

days_of_major_bad_requests_query = '''
SELECT viewsperday.day, failedviewsperday.failedrequests, viewsperday.views
FROM viewsperday, failedviewsperday
WHERE failedrequests > (views/100)
ORDER BY failedrequests DESC;'''

print("These are the most popular three articles of all time: \n")
c.execute(top_three_articles_query)
top_three_articles = c.fetchall()
for article in top_three_articles:
    print(article[0] + ' -- ' + str(article[1]) + ' views')

print("\nNext up, we have our most popular authors of all time: \n")

c.execute(top_authors_query)
top_authors = c.fetchall()
for author in top_authors:
    print(author[0] + ' -- ' + str(author[1]) + ' views')

print("""\nAnd finally, here is a list of days on which our website
        didn't work so well: \n""")

c.execute(days_of_major_bad_requests_query)
bad_requests_days = c.fetchall()
for day in bad_requests_days:
    if round(day[1]/day[2]*100, 1) > 1:
        print('{:%B %d, %Y}'.format(day[0]) + ' -- ' +
              str(round(day[1]/day[2]*100, 1)) + '% errors')

db.close()
