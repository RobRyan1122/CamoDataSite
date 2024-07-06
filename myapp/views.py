from django.shortcuts import render, redirect
from .models import Post
from .models import Question, Image
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse

def home(request):
    posts = Post.objects.all()
    return render(request, 'myapp/home.html', {'posts': posts})


def image_list(request):
    images = Image.objects.all()
    return render(request, 'image_list.html', {'images': images})

from django.shortcuts import render
from .models import Image

from django.shortcuts import render, redirect
from .models import Image
from django.shortcuts import redirect
from .models import Question, Image
def nth_image(request):
    session_id = request.session.session_key
    if not session_id:
        request.session.create()  # This will create a session if one doesn't exist

    image_index = request.session.get('image_index', 0)
    images = Image.objects.all()

    if not images:
        return redirect('home')  # Redirect to home if no images are available

    if image_index >= len(images):
        # Reset image index to 0 and redirect to the thanks page
        request.session['image_index'] = 0
        return redirect('thanks')

    image = images[image_index % len(images)]
    request.session['current_image_id'] = image.image_id
    request.session['image_index'] = image_index + 1  # Increment the image index

    context = {
        'image': image,
        'session_id': session_id,
    }

    return render(request, 'myapp/first_image.html', context)




def create_question(request):
    if request.method == 'POST':
        session_id = request.session.session_key
        animal_present = request.POST.get('animal_present') == 'on'
        animal_type = request.POST.get('animal_type') if animal_present else ''

        current_image_id = request.session.get('current_image_id')
        if current_image_id:
            current_image = Image.objects.get(image_id=current_image_id)
            ap_correct = (current_image.animal_present == animal_present)
            at_correct = (current_image.animal_type == animal_type) if animal_present else None
        else:
            ap_correct = None
            at_correct = None
            current_image = None

        # Create a blank Question object
        question = Question.objects.create(
            animal_present=animal_present,
            animal_type=animal_type,
            session_num=session_id,
            ap_correct=ap_correct,
            at_correct=at_correct,
            image=current_image
        )
        question.save()

        return redirect('nth_image')  # Redirect to the nth_image view

    return HttpResponse("Invalid request method", status=405)


def start_session(request):
    # Clear the current session data
    request.session.flush()

    # Create a new session
    request.session.create()

    return JsonResponse({"session_key": request.session.session_key})

def thanks(request):
    return render(request, 'myapp/thanks.html')  # Render the thanks template