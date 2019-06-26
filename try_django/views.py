from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

# Don't Repeat Yourself = DRY
from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):
    # You want to do the condition logic here
    qs = BlogPost.objects.all()[:5]
    context = {"title": 'Welcome to Try  Django', 'blog_lis': qs}
    return render(request, "home.html", context)

def about_page(request):
    return render(request, "about.html", {"title": "About Us"})



def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm() # Reinitialize the form
    context = {
        "title": "Contact Us",
        "form": form
    }
    return render(request, "form.html", context)



def example_page(request):
    context = {"title": "Example"}
    template_name = 'hello_world.html'
    template_obj = get_template(template_name)
    render_item = template_obj.render(context)
    return HttpResponse(render_item)