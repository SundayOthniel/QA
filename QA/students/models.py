from django.db import models
from django.conf import settings

class QuestionManager(models.Manager):
    def get_specialised_questions(self,specialty):
        return super().get_queryset().filter(specialty=specialty)
    def specialised_questions_count(self,specialty):
        questions_count = super().get_queryset().filter(specialty=specialty).count()
        if questions_count == 1:
            return f'You have unanswer {questions_count} question'
        else:
            return f'You have unanswer {questions_count} questions'
class StudentQuestion(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username', null=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField()
    question = models.TextField(blank=False, null=False)
    specialty = models.CharField(max_length=100, blank=False)

    question_manager = QuestionManager()

    class Meta:
        db_table = 'StudentQuestion'
    def __str__(self):
        return self.name
