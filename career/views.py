from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context, RequestContext, loader
from django.template.loader import get_template
from django.core.urlresolvers import reverse
# Create your views here.

# auth
# from django.conf import settings
# from django.http import HttpResponseRedirect
# from django.shortcuts import render_to_response
# from django.template import RequestContext
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout as auth_logout
# from django.contrib.messages.api import get_messages

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import LinkForm
from algorithm1 import *



def home(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LinkForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cd = form.cleaned_data
            link_name = str(cd['link'])
            # request.session['link_name'] = link_name
            # link_name = request.session.get('link_name')
            crawler = Crawler()
            list = sort_skills(get_profession(crawler.get_skills(link_name)))[:3]
            t = get_template('career/result.html')
            result = t.render(Context({'user':request.user, 'list':list}))
            return HttpResponse(result)
            # return HttpResponseRedirect(reverse('result', args=(), kwargs={'link_name' : link_name}))
            # return HttpResponseRedirect(reverse('result'))

    else:
        form = LinkForm()

    return render(request, 'career/home.html', {'form': form})



# def result(request):
#     # link_name = "https://www.linkedin.com/in/oleksandrsochka"
#
#     link_name = request.session.get('link_name')
#     crawler = Crawler()
#     list = sort_skills(get_profession(crawler.get_skills(link_name)))[:3]
#     t = get_template('career/result.html')
#     result = t.render(Context({'user':request.user, 'list':list}))
#     return HttpResponse(result)

def about(request):
    t = loader.get_template('career/about.html')
    result = t.render(Context({'user':request.user}))
    return HttpResponse(result)

def faq(request):
    t = loader.get_template('career/faq.html')
    result = t.render(Context())
    return HttpResponse(result)

def contact(request):
    return render_to_response('career/contact.html', context_instance=RequestContext(request))


