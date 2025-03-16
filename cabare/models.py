from django.db import models
from middlewares.auth import hash_passwd


class Usuarios(models.Model):
    username = models.CharField(max_length=255)
    useremail = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    date_joined = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Verifica se é um novo usuário ou se a senha foi alterada
        if not self.pk or Usuarios.objects.get(pk=self.pk).password != self.password:
            self.password = hash_passwd(self.password)
        super(Usuarios, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
