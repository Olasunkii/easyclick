from .models import Category
#This function helps to show all categories of services in the Navbar tab
def categories(request):
    return {
        'categories': Category.objects.all()
    }