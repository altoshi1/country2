#main.py
import pycountry
import pycountry_convert



for country in pycountry.countries:
    try:
        continent_code = pycountry_convert.country_alpha2_to_continent_code(country.alpha_2)
        continent_name = pycountry_convert.convert_continent_code_to_continent_name(continent_code)
    except KeyError:

        continent_name = "Unknown"
    print(f"{country.name} ({continent_name})".rstrip())


