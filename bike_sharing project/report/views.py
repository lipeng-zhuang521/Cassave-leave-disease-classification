from django.shortcuts import render, redirect
from .models import ReportBikes
from rent.models import RentTable

def home(request):   
    if request.method == 'POST':
        bikeId = request.POST['bikeCode']
        message = request.POST['message']

        object = RentTable.objects.filter(bikeId=bikeId)

        if object is not None:
            object = ReportBikes(bikeId=bikeId, message=message)
            object.save()

            redirect('/')
            return render(request, template_name='report/index.html', context={'bikeId': 'Bike Id not found'})

        else:
            return render(request, template_name='report/index.html', context={'bikeId': 'Bike Id not found'})

    return render(request, template_name='report/index.html', context={})