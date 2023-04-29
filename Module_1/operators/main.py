# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
Lang_swis = "German"  #Language spoken in Switzerland
lang_spain = "Castilian Spanish" #Language spoken in Spain
rel_swis = "Roman Catholic"  #Religion in Switzerland
rel_spain = "Roman Catholic"  #Religion in Spain
cap_swis = "Bern"  #Capital city of Switzerland
cap_spain = "Madrid"  #Capital city of Spain
gdp_swis = 618228000000  #
gdp_spain = 1798000000000
population_rate_swis = 0.64  #Population growth rate of Switzerland is 0.64%
population_rate_spain = 0.12  #Population growth rate of Spain is 0.12%
population_swis = 8563760   #8.57 million polulation in switzerland
population_spain = 47222613  # 47.23 billion population in Spain

print(Lang_swis == lang_spain)
print(rel_swis == rel_spain)
print(len(cap_swis)!=len(cap_spain))
print(gdp_swis>gdp_spain)
print(population_rate_swis and population_rate_spain < 1)
print(population_swis > 10000000 or population_spain > 10000000)
print(
    (population_swis > 10000000 and population_spain < 10000000) or
    (population_spain > 10000000 and population_swis < 10000000))

