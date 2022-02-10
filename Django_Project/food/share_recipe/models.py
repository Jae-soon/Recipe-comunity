from django.contrib.auth.models import User
from django.db import models


menu_Korea = "한식"
menu_China = "중식"
menu_Western = "양식"
menu_Japan = "일식"
menu_Choice = ((menu_Korea, "한식"), (menu_China, "중식"), (menu_Western, "양식"), (menu_Japan, "일식"))

class share_recipe(models.Model):
    subject = models.CharField(max_length=200)
    menu = models.CharField(choices=menu_Choice, max_length = 10)
    material = models.TextField()
    how_Make = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'author_recipe')
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name = 'voter_recipe')

    def __str__(self):
        return self.subject

class Answer(models.Model):
    recipe = models.ForeignKey(share_recipe, on_delete = models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'author_answer')
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name = 'voter_answer')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank = True)
    recipe = models.ForeignKey(share_recipe, null = True, blank = True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null = True, blank = True, on_delete = models.CASCADE)


class Photo(models.Model):
    recipe = models.ForeignKey(share_recipe, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

