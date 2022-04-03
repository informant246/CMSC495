from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import HttpResponseForbidden
from bug_tracker.forms import BugTrackerForm
from bug_tracker.models import BugTracker

from .forms import SearchForm


def aboutView(request):
    """ View that will display the about page. """
    return render(request, 'bug_tracker/about.html')


def homeView(request):
    """ View that displays the home page and the search bar. """
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            # get the users query
            query = form.cleaned_data['search']
            # search for the users query
            object_list = BugTracker.objects.filter(bug_title__icontains=query)
            # send the user to the page with the results
            return render(request, 'bug_tracker/search_results.html', {"object_list": object_list})

        else:
            form = SearchForm()
        return render(request, 'bug_tracker/home.html', {"form": form})


class IndexListView(ListView):
    """ List View will display all Bug Tracker objects in a list. """

    model = BugTracker


class BugCreateView(CreateView):
    """
    Create View that will allow logged in users the permission to create new 
    bug objects.
    """

    model = BugTracker
    form_class = BugTrackerForm
    # on successful submission of form, the view will send the user to the list view index
    success_url = reverse_lazy('bug_list')

    def form_valid(self, form_class):
        """ Method validates the form and assigns it to the user signed in"""
        form_class.instance.user = self.request.user
        return super().form_valid(form_class)


class BugDetailView(DetailView):
    """
    Detail View that displays the selected Bug Tracker object with all 
    defined attributes. 
    """

    model = BugTracker
    context_object_name = 'bug'


class BugUpdateView(UpdateView):
    """
    Update View that will update the selected object if the user passes the 
    authentication check.
    """

    model = BugTracker
    fields = ["bug_title", 'project_name', 'date_occured',
              'bug_description', 'bug_risk']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy("bug_list")

    def get(self, request, *args, **kwargs):
        """
        Method verifies if user created the object. If the user did not create
        the object, they are redirected to an error page.
        """
        # get the user who created the object
        object_user = BugTracker.objects.filter(user=request.user)
        # get the user logged in
        current_user = self.request.user

        if object_user != current_user:
            return HttpResponseForbidden('Permission Error')
        else:
            return render(request, self.template_name)


class BugDeleteView(DeleteView):
    """
    View will delete the selected object if the user passes the authentication check.
    """

    model = BugTracker
    success_url = reverse_lazy('bug_list')

    def get(self, request, *args, **kwargs):
        """
        Method verifies if user created the object. If the user did not create the object, they are redirected to an error page.
        """
        object_user = BugTracker.objects.filter(user=request.user)
        current_user = self.request.user

        if object_user != current_user:
            return HttpResponseForbidden('Permission Error')
        else:
            return render(request, self.template_name)


class BugSearchListView(ListView):
    """
    List View that displays the object list provided from the homeView method's search form. 
    """

    model = BugTracker
    template_name = 'search_results.html'
