from django.db import models


class Movie(models.Model):
    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2
    RATED_R = 3
    RATINGS = (
        (NOT_RATED, 'NR - Not Rated'),
        (RATED_G, 'G - General Audiences'),
        (RATED_PG, 'PG - Parental Guidance Suggested'),
        (RATED_R, 'R - Restricted'),
        (RATED_PG, 'PG - Parental Guidance'),
    )
    title = models.CharField(max_length=200)
    plot = models.TextField()
    year = models.PositiveIntegerField()
    rating = models.IntegerField(choices=RATINGS, default=NOT_RATED)
    runtime = models.PositiveIntegerField()
    website = models.URLField(blank=True)
    director = models.ForeignKey(to='Person', on_delete=models.SET_NULL, related_name='directed', blank=True, null=True)
    writers = models.ManyToManyField(to='Person', related_name='writing_credits', blank=True)
    actors = models.ManyToManyField(to='Person', through='Role', related_name='acting_credits', blank=True)

    class Meta:
        ordering = ('-year', 'title')

    def __str__(self):
        return '{} ({})'.format(self.title, self.year)


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    born = models.DateField()
    died = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ('last_name', 'first_name')

    def __str__(self):
        if self.died:
            return '{}, {} ({} - {})'.format(
                self.last_name,
                self.first_name,
                self.born,
                self.died
            )

        return '{}, {}, ({})'.format(
            self.last_name,
            self.first_name,
            self.born
        )


class Role(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)

    def __str__(self):
        return "{} {} {}".format(self.movie_id, self.person_id, self.name)

    class Meta:
        unique_together = ('movie', 'person', 'name')
