from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

def change_ep(request, anime, ep_str: str, ep_total_amount):
    if int(ep_str.split('-')[1]) == ep_total_amount:
        return
    
    int_ep = int(ep_str.split('-')[1]) + 1
    ep_str = ep_str.replace(ep_str.split('-')[1], str(int_ep))
    # return redirect(request, 'watch.html', {'anime': anime, 'current_episode': ep_str})

# Create your views here.
def show_ep(request, anim, ep):
    if request.method == 'POST':
        # print(str(ep).split('-'))
        change_ep(request, anim, ep, 12)
        print(ep)
    return render(request, 'watch.html', {'anime': anim, 'current_episode': ep})

def show_ep_test(request):
    return render(request, 'watch.html')