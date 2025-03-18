from django.db import models
from middlewares.auth import hash_passwd


class Usuarios(models.Model):
    TIPO_CHOICES = [
        ("C", "comum"),
        ("CC", "criador de conteudo"),
    ]

    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20)
    date_joined = models.DateField(auto_now_add=True)

    typed = models.CharField(max_length=50, choices=TIPO_CHOICES, default="C")

    def save(self, *args, **kwargs):
        # Verifica se é um novo usuário ou se a senha foi alterada
        if not self.pk or Usuarios.objects.get(pk=self.pk).password != self.password:
            self.password = hash_passwd(self.password)
        super(Usuarios, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class Images(models.Model):
    user = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.url


class Post(models.Model):
    user = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Images, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Videos(models.Model):
    user = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    video = models.FileField(upload_to="videos/")
    date_uploaded = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
