from django.db import models

# Create your models here.
class Document(models.Model):
    TYPE_CHOICES = [
        ("json", "json"),
        ("pdf",  "pdf"),
        ("word", "word")
    ]
    name = models.CharField(max_length=250, null=True, blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True, blank=True)
    file = models.FileField(upload_to="documents")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)
