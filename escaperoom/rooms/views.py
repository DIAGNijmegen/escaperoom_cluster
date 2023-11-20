from django.shortcuts import render
from django.http import HttpResponse
from rooms.forms import AccessForm, PuzzleForm
from rooms.code_checks import check_access_code, check_puzzle_solution
def main_page(request):
    return render(request, 'main.html')

def room(request, room_number):
    access_session_key = f'access_granted_room_{room_number}'
    puzzle_session_key = f'puzzle_solved_room_{room_number}'
    
    access_granted = request.session.get(access_session_key, False)
    puzzle_solved = request.session.get(puzzle_session_key, False)

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
                    request.session[puzzle_session_key] = True  # Set session variable for puzzle

    context = {
        'access_form': access_form,
        'puzzle_form': puzzle_form,
        'allowed': access_granted,
        'success': puzzle_solved,
        'room_number': room_number
    }
    return render(request, f'room{room_number}.html', context)

