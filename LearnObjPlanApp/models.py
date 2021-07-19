from django.db import models

# TODO these will come from locale files
# TODO make these specific to objectives or content areas
course_name_help = 'Example: College Algebra'
course_number_help = 'Example: MATH 136'
origin_help = ('Where did this requirement come from? Common sources are '
               + 'syllabi, accreditors, or institutional objectives. Leave '
               + 'blank for children.')
origin_abbr_help = 'Shortened name or acryonym for origin.'
origin_url_help = 'Webpage where the origin is found.'
origin_number_help = ('The number for objective from the origin. '
                      + 'Leave blank if there is no origin or the origin does '
                      + 'not list a number.')
parent_help = ('Is this requirement devirived from a different requirement? If'
               + 'so, put that requirement here. If not, leave blank.')


class Course(models.Model):
    name = models.CharField(max_length=200, help_text=course_name_help)
    number = models.CharField(max_length=200, help_text=course_number_help)

    def __str__(self):
        return self.number


class Origin(models.Model):
    origin = models.CharField(max_length=200, help_text=origin_help)
    abbreviation = models.CharField(max_length=200, blank=True,
                                    help_text=origin_abbr_help)
    url = models.URLField(blank=True, help_text=origin_url_help)

    def __str__(self):
        return self.origin


class ContentArea(models.Model):
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True,
                               null=True, help_text=parent_help)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, blank=True,
                               null=True, help_text=origin_help)

    def __str__(self):
        return self.description


class Objective(models.Model):
    objective_text = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True,
                               null=True, help_text=parent_help)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, blank=True,
                               null=True, help_text=origin_help)
    origin_number = models.CharField(max_length=200, blank=True,
                                     help_text=origin_number_help)
    content_area = models.ForeignKey(ContentArea, on_delete=models.CASCADE,
                                     blank=True, null=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.objective_text
