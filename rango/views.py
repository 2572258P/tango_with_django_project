from django.shortcuts import render
from rango.models import Category
from rango.models import Page
from rango.form import CategoryForm
from django.shortcuts import redirect

def index(request):    
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy,creamy,cookie,candy,cupcake!'
    context_dict['categories'] = category_list
    
    page_list = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = page_list
    context_dict['cat_ML'] = Category.objects.order_by('-likes')[0]
    
    return render(request, 'rango/index.html',context=context_dict)
    
def about(request):
    return render(request,'rango/about.html')

def show_category(request, category_name_slug):
    context_dict = {}
    
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context=context_dict)

def add_category(request):
    form = CategoryForm();    
    if request.method == 'POST': #HTTP request is POST(to check that users submitted data via form)
        form = CategoryForm(request.POST) #create new category form
        
        if form.is_valid():
            form.save(commit=True) # Save the new category to the database.
            return redirect('/rango/')
        else:
            print(form.errors) #print errors to the terminal
    return render(request, 'rango/add_category.html',{'form':form})


        