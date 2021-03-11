from django.shortcuts import render

# Create your views here.
from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        #product = request.POST.get('product')
        return redirect('homepage')

    def get(self , request):
    	context = {}
    	return render(request, 'portfolio/index.html', context)