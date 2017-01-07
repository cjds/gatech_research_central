from django.http import HttpResponse
from django.template import loader
from models import Study

def index(request):
    study_list = Study.objects.order_by('-published_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'study_list': study_list,
    }
    return HttpResponse(template.render(context, request))


def submit(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('submit.html')
    context = {
        #'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
