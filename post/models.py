from distutils.text_file import TextFile
from unicodedata import name
from django.db import models
from django.forms import CharField
from pytz import timezone
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post-img/')

    

    class Meta:
        verbose_name = ("post")
        verbose_name_plural = ("posts")
# الي تحت هذا لتجعل اسم المنشور الذي عملته يظهل بدل كلمة اوبجيكت , التايتل تتغير على حسن الفونكشون
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

