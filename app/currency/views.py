from django.http.response import HttpResponse
from django.shortcuts import render

from currency.models import Rate, ContactUs


def rate_list(request):
    rates = Rate.objects.all()
    context = {
        'rates': rates
    }

    return render(request, 'rate_list.html', context)


def contact_list(request):
    contacts = ContactUs.objects.all()
    context = {
        'title': 'Contacts List',
        'contacts': contacts,
    }

    return render(request, 'contact.html', context)


def status_code(request):
    return HttpResponse(
        'Vic Nesterenko',
        status=301,
        headers={'Location': '/rate/list/'}
    )


def test_template(request):
    name = request.GET.get('name')
    context = {
        'username': name
    }

    return render(request, 'test.html', context)
