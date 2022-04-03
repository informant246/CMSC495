from django.forms import ModelForm, SelectDateWidget
from django import forms
from bug_tracker.models import BugTracker


class BugTrackerForm(ModelForm):
    """ Class that represents the form to create a new bug tracker obejct. """
    class Meta:
        model = BugTracker
        fields = ["bug_title", 'project_name', 'date_occured',
                  'bug_description', 'bug_risk']
        labels = {
            'bug_title': ("Exception Title"),
            'project_name': ("Project"),
            'date_occured': ("Bug Found"),
            'bug_description': ("Describe the Bug"),
            'but_risk': ("Risk Level")

        }
        widgets = {
            'date_occured': SelectDateWidget()
        }


class SearchForm(forms.Form):
    """ Class that represents the search bar to retrieve the bug tracker objects """
    search = forms.CharField(label='Search', max_length=100)
