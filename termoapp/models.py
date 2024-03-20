from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
    def save(self, *args, **kwargs):
        if not self.pk:
            for field in self._meta.fields:
                if isinstance(field, models.ForeignKey):
                    field_name = f"{field.name}_id"
                    related_object = getattr(self, field.name)
                    setattr(self, field_name, related_object.id)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.__class__.__name__} {self.id}"
    
class User(BaseModel):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    ranking = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        constraints = [
            models.UniqueConstraint(fields=['username'], name='unique_username')
        ]

class Word(BaseModel):
    word = models.CharField(max_length=5, validators=[MinLengthValidator(5)])

    class Meta:
        verbose_name = "Word"
        verbose_name_plural = "Words"
        constraints = [
            models.UniqueConstraint(fields=['word'], name='unique_word')
        ]

class UserWord(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    word = models.ForeignKey(Word, on_delete=models.PROTECT)
    score = models.IntegerField()

    class Meta:
        verbose_name = "UserWord"
        verbose_name_plural = "UserWords"
        constraints = [
            models.UniqueConstraint(fields=['user', 'word'], name='unique_user_word')
        ]
      