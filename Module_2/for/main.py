from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"

""" Write your functions here. """
def shortest_names(countries):  
  shortest_names = []
  len_country_names = [len(country) for country in countries]
  for country in countries:
     if len(country) == min(len_country_names):
       shortest_names.append(country)
       continue
  return shortest_names

def most_vowels(countries):
  vowels = ['a', 'e', 'i', 'o', 'u']
  for i in range(len(countries)):
     countries[i]=countries[i].lower()     
  sorted_countries = sorted(
    countries,
    key=lambda country: sum([country.count(vowel) for vowel in vowels]),
    reverse=True)
  formatted_countries = [country.title().replace("And", "and").replace("The", "the").replace("Of", "of") for country in sorted_countries]
  return (formatted_countries[:3])
  
def alphabet_set(countries):
  result = []
  alphabets = 'abcdefghijklmnopqrstuvwxyz'
  countries = [country.lower() for country in countries]
  for country in countries:
     for charachter in country:
        if charachter in alphabets:
         alphabets = alphabets.replace(charachter, '')
         if country not in result:
            result.append(country)
            continue
  return result
          
# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()
     
    """ Write the calls to your functions here. """
    #print(shortest_names(countries))
    print(most_vowels(countries)[:3])
    #print(alphabet_set(countries))

