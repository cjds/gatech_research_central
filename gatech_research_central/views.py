from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from models import Study

from forms import *

def index(request):
    study_list = Study.objects.order_by('-published_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'study_list': study_list,
        'search':request.GET.get('search',''), 
    }
    return HttpResponse(template.render(context, request))


def submit(request):
    if request.method == 'POST':
        form = StudyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            new_study=form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = StudyForm()
    template = loader.get_template('submit.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def study(request,study):
    template = loader.get_template('study.html')
    obj = Study.objects.get(pk=study)
    context = {
        'study': obj,
    }
    return HttpResponse(template.render(context, request))

