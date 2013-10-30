from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import urlresolvers, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _




from .forms import RegistrationForm



def register(request, template_name="registration/register.html"):
    
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = RegistrationForm(postdata)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = postdata.get('email', '')
            user.save()
            username = postdata.get('username', '')
            password = postdata.get('password1', '')
            from django.contrib.auth import login, authenticate
            new_user = authenticate(username=username, password=password)
            if new_user and new_user.is_active:
                login(request, new_user)
                url = urlresolvers.reverse('my_account')
                return HttpResponseRedirect(url)
    else:
        form = RegistrationForm()
    page_title = _("User registration")
    context = locals()
    context.update(csrf(request))
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))


@login_required
def my_account(request, template_name="registration/my_account.html"):
    page_title = _("My account")
    name = request.user.username
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

