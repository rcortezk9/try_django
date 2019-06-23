from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

# Don't Repeat Yourself = DRY

def home_page(request):
    my_title = "Hello there..."
    context = {"title": my_title}
    # doc = "<h1>{title}</h1>".format(title=my_title)
    # django_rendered_doc = "<h1>{{title}}</h1>".format(title=my_title)
    return render(request, "home.html", context)

def about_page(request):
    return render(request, "about.html", {"title": "About Us"})

def contact_page(request):
    return render(request, "hello_world.html", {"title": "Contact Us"})

def example_page(request):
    context = {"title": "Example"}
    template_name = 'hello_world.html'
    template_obj = get_template(template_name)
    render_item = template_obj.render(context)
    return HttpResponse(render_item)