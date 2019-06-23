from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

# Don't Repeat Yourself = DRY

def home_page(request):
    # You want to do the condition logic here
    my_title = "Hello there..."
    context = {"title": my_title}
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]}
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