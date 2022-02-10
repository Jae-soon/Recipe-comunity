from django.contrib.auth.models import User
from django.db import models

menu_Korea = "한식"
menu_China = "중식"
menu_Western = "양식"
menu_Japan = "일식"
menu_Choice = ((menu_Korea, "한식"), (menu_China, "중식"), (menu_Western, "양식"), (menu_Japan, "일식"))


class main_recipe(models.Model):
    subject = models.CharField(max_length=200)
    menu = models.CharField(choices=menu_Choice, max_length=10)
    material = models.TextField()
    how_Make = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject

class Photo(models.Model):
    recipe = models.ForeignKey(main_recipe, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)