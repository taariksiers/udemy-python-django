from . import forms
from django.contrib import messages
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Hi there')
    return render(request, 'basicapp/index.html')


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            messages.add_message(request, messages.INFO, 'Data post success')
            logger.info('Data post success %s <%s>', form.cleaned_data['name'], form.cleaned_data['email'])
        else:
            logger.error('Data post failure')

    return render(request, 'basicapp/form_page.html', {'form': form})
