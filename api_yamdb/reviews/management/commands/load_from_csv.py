import csv
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from reviews.models import (Category, Comment, Genre, GenresTitle,
                            Review, Title)


User = get_user_model()


class Command(BaseCommand):
    help = "Loads data to database from csv files"

    def handle(self, *args, **options):

        print("Loading Users ... ", end="")
        with open('static/data/users.csv') as csvfile:
            users_reader = csv.reader(csvfile)
            next(users_reader)
            for row in users_reader:
                User(
                    id=row[0],
                    username=row[1],
                    email=row[2],
                    role=row[3],
                    bio=row[4],
                    first_name=row[5],
                    last_name=row[6],
                ).save()
            print('Done')

        print("Loading Categories ... ", end="")
        with open('static/data/category.csv') as csvfile:
            categories_reader = csv.reader(csvfile)
            next(categories_reader)
            for row in categories_reader:
                Category(
                    id=row[0],
                    name=row[1],
                    slug=row[2],
                ).save()
            print('Done')

        print("Loading Genres ... ", end="")
        with open('static/data/genre.csv') as csvfile:
            genres_reader = csv.reader(csvfile)
            next(genres_reader)
            for row in genres_reader:
                Genre(
                    id=row[0],
                    name=row[1],
                    slug=row[2],
                ).save()
            print('Done')

        print("Loading Titles ... ", end="")
        with open('static/data/titles.csv') as csvfile:
            titles_reader = csv.reader(csvfile)
            next(titles_reader)
            for row in titles_reader:
                category = Category.objects.get(id=row[3])
                Title(
                    id=row[0],
                    name=row[1],
                    year=row[2],
                    category=category
                ).save()
            print('Done')

        print("Loading Genre_Titles ... ", end="")
        with open('static/data/genre_title.csv') as csvfile:
            genre_titles_reader = csv.reader(csvfile)
            next(genre_titles_reader)
            for row in genre_titles_reader:
                title = Title.objects.get(id=row[1])
                genre = Genre.objects.get(id=row[2])
                GenresTitle(
                    id=row[0],
                    title=title,
                    genre=genre
                ).save()
            print('Done')

        print("Loading Reviews ... ", end="")
        with open('static/data/review.csv') as csvfile:
            reviews_reader = csv.reader(csvfile)
            next(reviews_reader)
            for row in reviews_reader:
                title = Title.objects.get(id=row[1])
                author = User.objects.get(id=row[3])
                Review(
                    id=row[0],
                    title_id=title.id,
                    text=row[2],
                    author=author,
                    score=row[4],
                    pub_date=row[5],
                ).save()
            print('Done')

        print("Loading Comments ... ", end="")
        with open('static/data/comments.csv') as csvfile:
            comments_reader = csv.reader(csvfile)
            next(comments_reader)
            for row in comments_reader:
                review = Review.objects.get(id=row[1])
                author = User.objects.get(id=row[3])
                Comment.objects.create(
                    id=row[0],
                    review=review,
                    text=row[2],
                    author=author,
                    pub_date=row[4]
                ).save()
            print('Done')
