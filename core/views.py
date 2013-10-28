import json
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.generic import FormView, ListView, DetailView, CreateView
from django.views.generic.edit import ProcessFormView

from .forms import ItemForm
from .models import Item

COLORS = ['success', 'warning', 'danger', 'error', 'info',
          'success', 'warning', 'danger', 'error', 'info']

def item_list_and_form(request, status, template_name="core/list_and_form.html",
                       form=None ):
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
        if not form: 
            context['form'] = ItemForm()
        status = check_int(status)
    context['object_list'] = Item.objects.values().filter(status=status)
    context['page_title'] = get_page_title(status)
    context['color'] = COLORS[status-1]
    context['action'] = "."
    context.update(csrf(request))
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))



def item_detail(request, slug, template_name="core/item_detail.html"):
    context = {}
    item = Item.objects.get(slug=slug)
    # If it's a POST than we have an item  edit
    if request.method == 'POST':
        form = ItemForm(request, item)
        if form.is_valid():
            form.save()
        
        url = reverse('core_item_list_and_form',
                      status=check_int(form.cleaned_data["status"]),
                      form=form)
        return HttpResponseRedirect(url)
        
            
    # Otherwise it's a simple GET and we just render a form      
    context["object"] = item
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))
    
def get_page_title(value):
    for choice in Item.STATUS_CHOICES:
        if choice[0] == value:
            return choice[1]
            
def all_actions(request, template_name="core/all_actions.html"):
    context = {}
    action_lists = []  
    for choice in Item.STATUS_CHOICES:  
        action_lists.append({"name":choice[1], "actions":[], "color":COLORS[choice[0] - 1]})
        for action in Item.objects.filter(status=choice[0]):
            action_lists[-1]["actions"].append(action)
            
    context["action_lists"] = action_lists            
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))
    
def blank_redirect(request):
    return HttpResponseRedirect(reverse('core_item_list_and_form', kwargs={'status':1}))

def ajax_remove_item(request):
    result = 'False'
    slug = request.REQUEST.get("slug")
    item = Item.objects.get(slug=slug)
    if item:
        item.delete()
        result = 'True'
    
    json_response = json.dumps({'success': result})
    return HttpResponse(json_response, 
                        content_type='application/javascript; charset=utf-8')
def check_int(value):
    # prevent non-int values being passed
    if not isinstance(value, int):
        try: 
            value = int(value)
        except ValueError:
            value = 1
    return value
        
def ajax_load_edit_item_form(request):
    context = {}
    slug = request.REQUEST.get("slug", "")
    item = Item.objects.get(slug=slug)
    if item:
        form = ItemForm(instance=item)
    else:
        form = ItemForm()
        
    template_name = "core/item_form.html"
    context["form"] = form 
    context["action"] = item.get_absolute_url()
    html = render_to_string(template_name, context)
    json_response = json.dumps({"success": "True", "html": html})
    return HttpResponse(json_response,
                        content_type='application/javascript; charset=utf-8') 