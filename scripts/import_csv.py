import os
import csv

from api.models import User, Genre, Category, Title, Review, Comment

os.chdir('data')

with open('category.csv') as cat:
    reader = csv.reader(cat)
    for row in reader:
        if row[0] != 'id':
            Category.objects.get_or_create(
                name=row[1],
                slug=row[2]
            )

with open('genre.csv') as gen:
    reader = csv.reader(gen)
    for row in reader:
        if row[0] != 'id':
            Genre.objects.get_or_create(
                name=row[1],
                slug=row[2]
            )

with open('titles.csv') as ti:
    reader = csv.reader(ti)
    for row in reader:
        if row[0] != 'id':
            Title.objects.get_or_create(
                name=row[1],
                year=row[2],
                category_id=row[3]
            )

with open('users.csv') as usrs:
    reader = csv.reader(usrs)
    for row in reader:
        if row[0] != 'id':
            User.objects.get_or_create(
                username=row[1],
                email=row[2],
                role=row[3],
            )

with open('review.csv') as rev:
    reader = csv.reader(rev)
    for row in reader:
        if row[0] != 'id':
            Review.objects.get_or_create(
                title=row[1],
                text=row[2],
                author_id=row[3],
                score=row[4],
                pub_date=row[5]
            )

with open('comments.csv') as com:
    reader = csv.reader(com)
    for row in reader:
        if row[0] != 'id':
            Comment.objects.get_or_create(
                review_id=row[1],
                text=row[2],
                author=row[3],
                pub_date=row[4],
            )
