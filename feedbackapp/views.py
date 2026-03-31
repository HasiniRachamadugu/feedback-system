from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def feedback_form(request):

    if request.method == 'POST':

        form = FeedbackForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Feedback submitted successfully!")

            return redirect('feedback_form')

    else:

        form = FeedbackForm()

    return render(request, 'feedback_form.html', {'form': form})


def feedback_list(request):

    feedbacks = Feedback.objects.all()

    count = feedbacks.count()

    return render(request, 'feedback_list.html', {

        'feedbacks': feedbacks,

        'count': count

    })


def delete_feedback(request, id):

    feedback = Feedback.objects.get(id=id)

    feedback.delete()

    return redirect('feedback_list')