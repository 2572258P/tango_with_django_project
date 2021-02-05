from django.shortcuts import render
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm
from django.shortcuts import redirect
from django.urls import reverse
#from django.http import HttpResponse

def index(request):    
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    
    page_list = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = page_list
    
    likedobjs = Category.objects.order_by('-likes')
    if likedobjs.count() > 0:
        context_dict['cat_ML'] = likedobjs[0]
    
    return render(request, 'rango/index.html',context=context_dict)
    
def about(request):
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy,creamy,cookie,candy,cupcake!'
    return render(request,'rango/about.html',context=context_dict)


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

def add_page(request,category_name_slug):
    
    try:
        category = Category.objects.get(slug=category_name_slug)
        print("---Log: Show Category : " + category_name_slug)
        print("---Log: Category" + category_name_slug)
    except Category.DoesNotExist:
        print("---Log: do not exist" + category_name_slug)
        category=None
        
    if category is None:
        print("---Log: Category is none")
        return redirect('/rango/') #redirect user to the appropriate URL
    form = PageForm()
    
    if request.method == 'POST':
        form = PageForm(request.POST)        
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                #print("---Log: Page" + category +"Saved")
                return redirect(reverse('rango:show_category',
                                        kwargs={'category_name_slug':
                                                category_name_slug}))
            else:
                print("---Log: Errors")
                print(form.errors)
        
    context_dict = {'form' : form, 'category' : category }
    return render(request, 'rango/add_page.html', context=context_dict)
    
