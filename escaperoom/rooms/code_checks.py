def access_codes():
    access_codes = {
        'room1': '67787',
        'room2': '29976',
        'room3': '65747',
        'room4': '77874',
    }
    return access_codes

def puzzle_codes():
    puzzle_codes = {
        'room1': 'upright-evergreen-transform-subtract-cubicle-frosted',
        'room2': 'pursuit-bouncy-unstable-lettuce-sensuous-shaking',
        'room3': 'turbine-overshot-displace-upturned-rotunda-chef',
        'room4': 'void-shadow-upcountry-levitator-prism-displace',
    }
    return puzzle_codes

def check_access_code(room_number, code):
    valid_codes = access_codes()
    return valid_codes.get(room_number) == code

def check_puzzle_solution(room_number, code):
    valid_codes = puzzle_codes()
    return valid_codes.get(room_number) == code

def fetch_acces_code(room_number):
    valid_codes = access_codes()
    return valid_codes.get(room_number)