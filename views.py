from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from surveydog.models import Survey, SingleChoiceQuestion, MultiChoiceQuestion,\
    FreeQuestion, MultiChoice


def admin_results(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    context = {'survey_id': survey_id, 'survey': survey }
    return render(request, 'surveydog/adminvote.html', context)


def admin_vote(request, survey_id):
    survey = Survey.objects.get(pk=survey_id)
    single_questions = SingleChoiceQuestion.objects.filter(survey=survey)
    multi_questions = MultiChoiceQuestion.objects.filter(survey=survey)
    free_questions = FreeQuestion.objects.filter(survey=survey)
    try:
        selected_choices = []
        checked_list = []
        for squestion in single_questions:
            selected_choices.append(squestion.singlechoice_set.get(
                pk=request.POST['squestion'+str(squestion.id)+'choice']))
        for mquestion in multi_questions:
            checked_list.append(request.REQUEST.getlist('mquestion' +
                                                   str(mquestion.id)+'choice'))
        for fquestion in free_questions:
            fquestion.answer_text = request.POST['fquestion'+str(fquestion.id)]
            fquestion.save()
    except (KeyError):
        # redisplay the question voting form
        survey = Survey.objects.get(pk=survey_id)
        context = {'survey_id': survey_id,
                   'survey': survey,
                   'error_message': "you didn't answer all questions.",}
        return render(request, 'surveydog/adminvote.html', context)
    else:
        for selected_choice in selected_choices:
            selected_choice.votes += 1
            selected_choice.save()
        for checked_set in checked_list:
            for checked in checked_set:
                choice = MultiChoice.objects.get(pk=int(checked))
                choice.votes += 1
                choice.save()
        return HttpResponseRedirect(reverse('surveydog:admin_results',
                                            args=(survey_id,)))


def admin_detail(request, survey_id):
    context = {}
    try:
        survey = Survey.objects.get(pk=survey_id)
        context = {'survey_id': survey_id,
                   'survey': survey,}
    except Survey.DoesNotExitst:
        raise Http404
    return render(request, 'surveydog/adminvote.html', context)


def index(request):
    latest_survey_list = Survey.objects.order_by('-pub_date')[:5]
    context = {'latest_survey_list': latest_survey_list}
    return render(request, 'surveydog/index.html', context)