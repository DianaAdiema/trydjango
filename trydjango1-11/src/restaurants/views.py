from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import RestaurantLocation
# Create your views here.
# function based view
 


def restaurant_listview(request):
	template_name = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	context = { "object_list": queryset}

	return render(request, template_name, context)

class RestaurantListView(ListView):
	queryset = RestaurantLocation.objects.all()  #default template - restaurantlocation, comes from the model-restaurantlocation
	

	def get_queryset(self):
		
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(Q(category__iexact= slug)|Q(category__icontains=slug))

		else:
			queryset = RestaurantLocation.objects.all()

		return queryset

	
class RestaurantDetailView(ListView):
	queryset = RestaurantLocation.objects.all() 

	def get_context_data(self, *args, **kwargs):
		print(self.kwargs)
		context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
		print (context)
		return context

	



	
	


 	

  