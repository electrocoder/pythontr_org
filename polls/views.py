# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from pythontr_org.polls.models import Choice, Poll, Vote

from django.core.exceptions import ValidationError
from django.views.generic import ListView, DetailView


class PollListView(ListView):
    template_name = 'polls/index.html'
    paginate_by=15
        
    model = Poll
    

class PollDetailView(DetailView):
    template_name = 'polls/detail.html'
    model         = Poll


    def get_context_data(self, **kwargs):
       context = super(PollDetailView, self).get_context_data(**kwargs)
       
       try:
           vote = Vote.objects.get(user=self.request.user, poll=get_object_or_404(Poll, slug=self.kwargs['slug']))
           context['vote'] = vote
       except:
           pass
       
       return context


@login_required
def vote(request, slug):
    """
        Ankete oy vermek için kullanılır.
    """
    
    poll = get_object_or_404(Poll, slug=slug)
    
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
        
        vote = Vote(user=request.user, poll=poll, choice=Choice.objects.get(pk=request.POST['choice']))
        vote.save()
        
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        
        error_message = u'Bir seçeneği seçmediniz.'
        
        return render(request, 'polls/detail.html', locals())
        
    except ValidationError:
        error_message = u'Bu ankete zaten oy kullanmışsınız.'
        
        return render(request, 'polls/detail.html', locals())
    
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return redirect('polls:results', poll.slug)

    
@login_required
def vote_back(request, slug):
    """ Ankete verilen oyu geri almak için kullanılır."""
    
    poll = get_object_or_404(Poll, slug=slug)
    vote = get_object_or_404(Vote, user=request.user, poll=poll)
    
    vote.delete()
    
    return redirect('polls:detail', slug)