from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)

    def __str__(self):
        return self.number


class Origin(models.Model):
    origin = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=200, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.origin


class ContentArea(models.Model):
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True,
                               null=True)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, blank=True,
                               null=True)

    def __str__(self):
        return self.description


class Objective(models.Model):
    objective_text = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True,
                               null=True)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, blank=True,
                               null=True)
    source_number = models.CharField(max_length=200, blank=True)
    content_area = models.ForeignKey(ContentArea, on_delete=models.CASCADE,
                                     blank=True, null=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.objective_text
