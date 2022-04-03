from django.db import models
from django.conf import settings
# List of choices the user can select from


class BugTracker(models.Model):
    """ 
    Model class represents the bug tracker object. Detailing what problem what 
    the developer is dealing with in their program
    """

    risk_list = [("High", "High"), ("Medium", "Medium"), ("Low", "Low")]

    bug_title = models.CharField(max_length=200)
    # what project does the bug belong to
    project_name = models.CharField(max_length=100)
    # when was the bug first noticed
    date_occured = models.DateField()
    bug_description = models.TextField()
    date = models.DateField(auto_now_add=True)
    # how important is solving this bug
    bug_risk = models.CharField(max_length=7, choices=risk_list, default="Low")
    # Ensure that the bug is associated with the signed in user
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    def __str__(self):
        """The model will be given the bug's name in the admin panel
        """
        return self.bug_title

    class Meta:
        ordering = ["-date"]
