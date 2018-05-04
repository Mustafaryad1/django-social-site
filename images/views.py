from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm


# Create your views here.

@login_required
def image_create(request):
    """
    View for creating images using JavaScript Bookmarks
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            new_item = form.save(commit=False)
            new_item.user = request.user

            new_item.save()
            messages.success(request, 'Image add Successfully')
            return redirect(new_item.get_absolute_url())
        else:
            messages.error(request, 'Image Can not add')
    else:
        form = ImageCreateForm()
    return render(request, 'images/image/create.html', {'section': 'images',
                                                        'form': form})
