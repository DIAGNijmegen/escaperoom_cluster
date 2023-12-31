from django.shortcuts import render
from django.http import HttpResponse
from rooms.forms import AccessForm, PuzzleForm
from django.http import HttpResponse, Http404
from django.conf import settings
import os
from rooms.code_checks import check_access_code, check_puzzle_solution, fetch_acces_code
def main_page(request):
    return render(request, 'main.html')


def clear_session(request):
    request.session.flush()  # This will delete the current session data and cookie.
    return HttpResponse("Session cleared!")

def room(request, room_number):
    access_session_key = f'access_granted_room_{room_number}'
    puzzle_session_key = f'puzzle_solved_room_{room_number}'
    puzzle_session_answer = f'puzzle_answer_room_{room_number}'
    
    access_granted = request.session.get(access_session_key, False)
    puzzle_solved = request.session.get(puzzle_session_key, False)
    puzzle_answer = request.session.get(puzzle_session_answer, False)

    access_form = AccessForm(prefix='access')
    puzzle_form = PuzzleForm(prefix='puzzle')
    

    if request.method == 'POST':
        if 'access' in request.POST:
            access_form = AccessForm(request.POST, prefix='access')
            if access_form.is_valid():
                if check_access_code(f'room{room_number}', access_form.cleaned_data['code']):
                    access_granted = True
                    request.session[access_session_key] = True  # Set session variable for access
        elif 'puzzle' in request.POST:
            puzzle_form = PuzzleForm(request.POST, prefix='puzzle')
            if puzzle_form.is_valid():
                if check_puzzle_solution(f'room{room_number}', puzzle_form.cleaned_data['puzzle_answer']):
                    puzzle_solved = True
                    puzzle_answer = fetch_acces_code(f'room{room_number+1}')
                    request.session[puzzle_session_key] = True # Set session variable for puzzle
                    request.session[puzzle_session_answer] = puzzle_answer

    context = {
        'access_form': access_form,
        'puzzle_form': puzzle_form,
        'allowed': access_granted,
        'success': puzzle_solved,
        'success_key': puzzle_answer,
        'room_number': room_number
    }
    return render(request, f'room{room_number}.html', context)


def download_file(request, room_number, file_name):
    access_session_key = f'access_granted_room_{room_number}'
    puzzle_session_key = f'puzzle_solved_room_{room_number}'

    # Check if the user has access
    if not request.session.get(access_session_key) and not request.session.get(puzzle_session_key):
        raise Http404("You don't have permission to access this file.")

    file_path = os.path.join(settings.BASE_DIR, 'files', file_name)

    # Check if file exists
    if not os.path.exists(file_path):
        raise Http404("File does not exist.")

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type="application/octet-stream")
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response


# load the emergency page
def emergency(request):
    return render(request, 'emergency.html')