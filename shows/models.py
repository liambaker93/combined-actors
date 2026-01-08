from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Shows(models.Model):
    """
    This model is for displaying show information on the homepage and will hold more
    data than will potentially be shown, but can be used for filtering by users and by admins.
    """
    class Meta:
        verbose_name = 'Show'
        verbose_name_plural = 'Shows'

    name = models.CharField(max_length=256, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    director = models.CharField(max_length=256, blank=False)
    writer = models.CharField(max_length=256, blank=False)
    theatre = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=True, null=True)
    on_sale = models.BooleanField(default=False, blank=True)
    in_future = models.BooleanField(default=False, blank=True)
    image = models.ImageField(default=None, null=True, blank=True)
    tag_line = models.CharField(max_length=128, blank=True, null=True)

    def timeCheck(self):
        """
        Logic to ensure that the end date is after the start date
        """
        if self.start_date and self.end_date:
            if self.end_date <= self.start_date:
                raise ValidationError("The end date must be after the start date")

    def __str__(self):
        return f"{self.name} from {self.start_date} to {self.end_date} at the {self.theatre}"
