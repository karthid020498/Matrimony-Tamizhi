from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

# உங்கள் ஆப் பெயருடன் மாடல்களை இம்போர்ட் செய்தல் (Absolute Import)
from matrimony.models import Like, UserProfile


@login_required
def profile_list_view(request):
  profiles = UserProfile.objects.exclude(user=request.user)

  # வயது மற்றும் ஊரின் அடிப்படையில் தேடுதல் (Searching by age/city)
  age_query = request.GET.get('age')
  city_query = request.GET.get('city')

  if age_query:
    profiles = profiles.filter(age=age_query)
  if city_query:
    profiles = profiles.filter(city__icontains=city_query)

  return render(
      request, 'matrimony/profile_list.html', {'profiles': profiles}
  )


@login_required
def send_like_view(request, user_id):
  receiver_user = get_object_or_404(User, pk=user_id)
  if receiver_user != request.user:
    Like.objects.get_or_create(sender=request.user, receiver=receiver_user)
  return redirect('profile_list')
