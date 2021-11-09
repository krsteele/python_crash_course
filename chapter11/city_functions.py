# Exercise 11-1: City, Country and 11-2: Population

def city_country_name(city, country, population=''):
    """Generate neatly formatted city and country."""
    if population:
        formatted_name = f"{city}, {country} - population: {population}"
    else:
        formatted_name = f"{city}, {country}"

    return formatted_name.title()