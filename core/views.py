from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import FormView, ListView, DetailView, CreateView
from django.views.generic.edit import ProcessFormView

from .forms import ItemForm
from .models import Item


def item_list_and_form(request, status, template_name="core/list_and_form.html"):
    context = {}
    # If it's POST process a form 
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = ItemForm(postdata)
        context['form'] = form
        if form.is_valid():
            form.save()
            status = form.cleaned_data["status"]
    # If it's a get - just rende an object list and an empty form
    else:
        context['form'] = ItemForm()
        # prevent non-int values being passed
        if not isinstance(status, int):
            try: 
                status = int(status)
            except ValueError:
                status = 1
    context['object_list'] = Item.objects.values().filter(status=status)
    context['page_title'] = get_page_title(status)
    context.update(csrf(request))
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))



def item_detail(request, slug, template_name="core/item_detail.html"):
    context = {}
    context["object"] = Item.objects.get(slug=slug)
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))
    
def get_page_title(value):
    for choice in Item.STATUS_CHOICES:
        if choice[0] == value:
            return choice[1]
            

def blank_redirect(request):
    return HttpResponseRedirect(reverse('core_item_list_and_form', kwargs={'status':1}))


        