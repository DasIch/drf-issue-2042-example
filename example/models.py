from django.db import models


class A(models.Model):
    pass


class B(models.Model):
    a = models.ForeignKey(A, editable=False)

    def clean(self):
        self.a # should be here