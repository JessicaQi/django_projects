# the simplest view possible in Django. To call the view, we need
# to map it to a URL - and for this we need a URLconf.(urls.py/polls)
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
from django.utils import timezone

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1  # models里的choice attribute决定views
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Exclude any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
        # """
        # Return the last five published questions(not including those set to be published in the future).
        # """
        # return Question.objects.filter(
        #     pub_date__lte=timezone.now()
        # ).order_by('-pub_date')[:5]
        # """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
#  def index(request):
#     lastest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {      
#         'latest_question_list': lastest_question_list,
#     }
    # return HttpResponse(template.render(context, request))
    # render结构： render(request, template_name, dictionary)
    # 一旦render代替HttpRes, 不再需要import HttpRe和loader
# return render(request, 'polls/index.html', context)
    #output = ','.join([q.question_text for q in lastest_question_list])
    # return HttpResponse(output)
    # return HttpResponse("Hello,world. You're at the polls index.")

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
# def detail(request, question_id):
#     #return HttpResponse("You're looking at question %s." % question_id)
#     try: #抛出404错误
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
    # 一个快捷function：使用get()获取函数对象 抛出http404
    #quesiton = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question':question})
#     # response = "You're looking at the results of question %s"
#     # return  HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s" % question_id)
