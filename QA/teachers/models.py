from django.db import models
from students.models import StudentQuestion


class QuestionAnswer(models.Model):
    question = models.ForeignKey(StudentQuestion, on_delete=models.PROTECT, null=True) #related_name=answer: It is use for one to one field
    answer = models.TextField()

    class Meta:
        db_table = 'QuestionAnswer'
    def __str__(self):
        return self.question