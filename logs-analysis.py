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

c.execute(days_of_major_bad_requests_query)
bad_requests_days = c.fetchall()
worst_day = bad_requests_days[0][0]
for day in bad_requests_days:
    if round(day[1]/day[2]*100, 1) > 1:
        print("\n\nOn " + '{:%B %d, %Y}'.format(worst_day) +
              " things really didn't look well... " +
              str(round(day[1]/day[2]*100, 1)) +
              "% of requests produced an error.")
        break


print("""\nIn fact, here is a whole list of days on which over 1%
of requests failed: \n""")

c.execute(days_of_major_bad_requests_query)
bad_requests_days = c.fetchall()
for day in bad_requests_days:
    if round(day[1]/day[2]*100, 1) > 1:
        print('{:%B %d, %Y}'.format(day[0]) + ' -- ' +
              str(round(day[1]/day[2]*100, 1)) + '% errors')

db.close()
