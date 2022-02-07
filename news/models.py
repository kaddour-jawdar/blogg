from django.db import models
from django.contrib.auth import get_user_model
user = get_user_model()



class Category(models.Model):
    """Class category news"""
    title = models.CharField("Название", max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Tag(models.Model):
    """Class tag news"""

    title = models.CharField("Тег", max_length=50)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.title


class News(models.Model):
    """class News"""
    user = models.ForeignKey(
        user,
        verbose_name="Автор",
        on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null=True)
    title = models.CharField("Загогловок", max_length=100)
    text_min = models.TextField("Описоние", max_length=350)
    text = models.TextField("Текст статьи",)
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    created = models.DateTimeField("Дата создоние", auto_now_add=True)  # when he created
    description = models.CharField("Дискрипшен", max_length=100)
    keywords = models.CharField("Ключевые слова", max_length=50)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Cтатьи"

    def __str__(self):
        return self.title


class Comments(models.Model):
    """Class comments"""
    user = models.ForeignKey(
        user,
        verbose_name="Пользователь",
        on_delete=models.CASCADE) # if we deleted user also deleted data
    new = models.ForeignKey(
        News,
        verbose_name="Новость",
        on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    created = models.DateTimeField("Дата добавления", auto_created=True, null=True)
    moderation = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "{}".format(self.user)

