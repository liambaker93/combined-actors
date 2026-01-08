from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Shows
from .forms import ShowsForm
# Create your views here.


def shows(request):
    shows = Shows.objects.all()

    context = {
        'shows': shows,
    }

    template = 'shows/shows.html'

    return render(request, template, context)


def addNewShow(request):
    """
    Ability for an admin/staff user to add new shows to the db
    """
    if not request.user.is_staff:
        messages.error(request, "Sorry, only the admins can do that!")
        return redirect(reverse('shows'))

    if request.method == 'POST':
        newShow = ShowsForm(request.POST, request.FILES)
        if newShow.is_valid():
            newShow.save()
            messages.success(request, "Successfully added new show!")
            return redirect(reverse('shows'))
        else:
            messages.error(request, "Adding new show failed. \
                           Please ensure the form is valid.")
    else:
        newShow = ShowsForm()

    template = 'shows/add_show.html'
    context = {
        'newShow': newShow,
    }

    return render(request, template, context)
