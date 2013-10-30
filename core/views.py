import json
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.generic import FormView, ListView, DetailView, CreateView
from django.views.generic.edit import ProcessFormView

from .forms import ItemForm
from .models import Item

COLORS = ['success', 'warning', 'danger', 'error', 'info',
          'success', 'warning', 'danger', 'error', 'info']
@login_required
def item_list_and_form(request,
                       status=Item.IN_BASKET,
                       template_name="core/list_and_form.html",
                       action=".",
                       form=None):
    context = {}
    user = request.user
    # If it's POST process a form 
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = ItemForm(postdata)
        context['form'] = form
        if form.is_valid():
            item = form.save(commit=False)
            item.user = user
            item.save()
            status = form.cleaned_data["status"]
    # If it's a get - just rende an object list and an empty form
    else:
        context['form'] = form if form else ItemForm()
        status = check_int(status)
        
    context['object_list'] = Item.objects.values().filter(status=status, user=user)
    context['page_title'] = get_page_title(status)
    context['color'] = COLORS[status-1]
    context['action'] = action
    context.update(csrf(request))
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))


@login_required
def item_detail(request, slug, template_name="core/item_detail.html"):
    context = {}
    user = request.user
    item = get_object_or_404(Item, slug=slug, user=user)
    # If it's a POST than we have an item  edit
    if request.method == 'POST':
        form = ItemForm(request.POST.copy(), instance=item)
        if form.is_valid():
            form.save()
        kwargs = {'status': check_int(form.cleaned_data["status"]),
                  'form': form}
        
        return item_list_and_form(request, **kwargs)
        
            
    # Otherwise it's a simple GET and we just render a form      
    context["object"] = item
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))
    
def get_page_title(value):
    for choice in Item.STATUS_CHOICES:
        if choice[0] == value:
            return choice[1]
@login_required            
def all_actions(request, template_name="core/all_actions.html"):
    context = {}
    action_lists = []
    user = request.user
    for choice in Item.STATUS_CHOICES:  
        action_lists.append({"name":choice[1], "actions":[], "color":COLORS[choice[0] - 1]})
        for action in Item.objects.filter(status=choice[0], user=user):
            action_lists[-1]["actions"].append(action)
            
    context["action_lists"] = action_lists            
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))
    
def blank_redirect(request):
    return HttpResponseRedirect(reverse('core_item_list_and_form', kwargs={'status':1}))

@login_required
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
        
@login_required
def edit_item(request, slug):
    context = {}
    item = Item.objects.get(slug=slug)
    form = None
    if item and request.user == item.user:
        form = ItemForm(instance=item) 
    # template_name = "core/item_form.html"
    # context["form"] = form 
    action = item.get_absolute_url()
    # contex.update(csrf(request))
    return item_list_and_form(request, item.status, form=form, action=action)
    
    
    
    
    
    
    
    
    