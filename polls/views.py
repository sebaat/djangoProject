from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from polls.forms.forms import NameForm
from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('is  bound (post): ' + str(form.is_bound))
            print(form.cleaned_data.get('your_name'))
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/polls/myform')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        print('is  bound: ' + str(form.is_bound))

    return render(request, 'polls/name.html', {'form': form})
