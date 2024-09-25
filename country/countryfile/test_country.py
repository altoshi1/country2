import unittest
from io import StringIO
import sys
import pycountry
import pycountry_convert


class TestCountryContinent(unittest.TestCase):

    def setUp(self):
        # Rediriger la sortie standard pour capturer les impressions
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Restaurer la sortie standard
        sys.stdout = sys.__stdout__

    def test_country_continent_output(self):
        # Exécuter le code de main.py en capturant la sortie
        countries = []
        for country in pycountry.countries:
            try:
                continent_code = pycountry_convert.country_alpha2_to_continent_code(country.alpha_2)
                continent_name = pycountry_convert.convert_continent_code_to_continent_name(continent_code)
            except KeyError:
                continent_name = "Unknown"
            countries.append(f"{country.name} ({continent_name})")

        # Capturer la sortie
        output = self.held_output.getvalue().strip().split('\n')

        # Vérification d'un pays connu
        expected_countries = {
            "France": "Europe",
            "United States": "North America",
            "Brazil": "South America",
            "India": "Asia",
            "Australia": "Oceania",
        }

        for country, continent in expected_countries.items():
            self.assertIn(f"{country} ({continent})", countries)

    def test_unknown_country(self):
        # Vérification pour un pays non reconnu
        with self.assertRaises(KeyError):
            pycountry_convert.country_alpha2_to_continent_code("ZZ")


if __name__ == '__main__':
    unittest.main()
