# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

film_list = ['valley of the dolls', 'Fahrenheit', 'goodbye, mr. chips', 'the reivers', 'fiddler on the roof', 'images', 'memoirs of a geisha', 'jaws']

def alphabetical_order(film_list):
    return sorted(film_list)


def won_golden_globe(film_name):
    if film_name.lower() in ['fiddler on the roof', 'jaws', 'memoirs of a geisha']:
        return True
    else:
        return False
    


