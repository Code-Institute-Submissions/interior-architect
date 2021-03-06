from django.db import models
from django.utils import timezone
from portfolio.models import Project


class Role(models.Model):
    '''Individual role.
    Job field differentiates employment from education.
    '''
    company = models.CharField(max_length=200)
    link = models.URLField(max_length=200, blank=True)
    title = models.CharField(max_length=200)
    timeframe = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    order = models.IntegerField(null=True, blank=True)
    job = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.company} {self.title}'


class Point(models.Model):
    '''Bullet point for an individual role.
    '''
    role = models.ForeignKey(
        'Role',
        on_delete=models.CASCADE,
        related_name='points'
    )
    content = models.TextField()


class Example(models.Model):
    '''Link between a project and an individual role.
    Credit: Related names
    https://simpleisbetterthancomplex.com/tips/2018/02/10/django-tip-22-designing-better-models.html#naming-your-models
    '''
    role = models.ForeignKey(
        'Role',
        on_delete=models.CASCADE,
        related_name='examples'
    )
    project = models.ForeignKey(
        'portfolio.Project',
        on_delete=models.CASCADE,
        related_name='cv_examples'
    )
    order = models.IntegerField(null=True, blank=True)


class Skill(models.Model):
    '''Skill level to display in animated data circle.
    '''
    program = models.CharField(max_length=50)
    percent = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f'{self.program}'
