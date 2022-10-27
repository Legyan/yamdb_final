from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from reviews.validators import year_validator


class CustomUser(AbstractUser):
    """Модель юзера."""

    USER_ROLE_USER = 'user'
    USER_ROLE_MODERATOR = 'moderator'
    USER_ROLE_ADMIN = 'admin'
    CHOICE_USER_ROLE = (
        (USER_ROLE_USER, 'пользователь'),
        (USER_ROLE_MODERATOR, 'модератор'),
        (USER_ROLE_ADMIN, 'админ')
    )

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
        blank=True
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=254,
        unique=True
    )
    bio = models.TextField(
        verbose_name='Дополнительная информация',
        blank=True
    )
    role = models.CharField(
        verbose_name='Пользовательская роль',
        max_length=24,
        choices=CHOICE_USER_ROLE,
        default=USER_ROLE_USER
    )
    confirmation_code = models.CharField(
        verbose_name='Код подтверждения',
        max_length=30,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_admin(self):
        return self.role == self.USER_ROLE_ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.USER_ROLE_MODERATOR


class Category(models.Model):
    """Модель Категории."""

    name = models.CharField(
        verbose_name='Название категории', max_length=256, unique=True)
    slug = models.SlugField(
        max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Модель Жанры."""

    name = models.CharField(
        verbose_name='Название жанра', max_length=256, unique=True)
    slug = models.SlugField(
        max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    """Модель Произведения."""

    name = models.CharField(
        verbose_name='Название произведения', max_length=256)
    year = models.IntegerField(
        verbose_name='Год выпуска',
        validators=(year_validator,))
    description = models.TextField(
        verbose_name='Описание', blank=True, null=True)
    genre = models.ManyToManyField(Genre, through='GenresTitle')
    category = models.ForeignKey(
        Category, related_name='title', blank=True, null=True,
        on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class GenresTitle(models.Model):
    """Промежуточная модель для реализации отношения многие ко многим."""

    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title} {self.genre}'


class Review(models.Model):
    """Модель отзывов."""

    text = models.TextField(
        help_text='Введите текст отзыва',
        verbose_name='Текст отзыва',
    )
    score = models.IntegerField(
        help_text='Введите оценку произведения',
        verbose_name='Оценка',
        validators=[
            MinValueValidator(1, message='Оценка не может быть меньше 1'),
            MaxValueValidator(10, message='Оценка не может быть больше 10'),
        ]
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации отзыва'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='username пользователя',
        related_name='reviews'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Произведение',
        related_name='reviews'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('author', 'title'),
                name='unique_review_on_title')
        ]

    def __str__(self):
        return self.text[:25]


class Comment(models.Model):
    """Модель комментариев."""

    text = models.TextField(
        help_text='Введите текст комментария',
        verbose_name='Текст комментария',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='username автора комментария',
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации комментария'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        verbose_name='Отзыв',
        related_name='comments'
    )

    def __str__(self):
        return self.text[:25]
