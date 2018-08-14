from django.shortcuts import render
from  registration.forms import RegistrationForm
from registration.models import Registration

# Create your views here.
def index (request):

	register_list = Registration.objects.all()
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			try:
				form.save()

				return redirect('/registration')

			except:
				pass
	else:
		form = RegistrationForm()

	return render(request, 'registration/index.html',{'form': form, 'register_list':register_list})