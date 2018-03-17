import unittest
import capitals
import subprocess


class TestCapitals(unittest.TestCase):


    def test_correct_capital_returned(self):
        city = capitals.capital("Central African Republic")
        self.assertEqual("Bangui", city)
        city = capitals.capital("Hungary")
        self.assertEqual("Budapest", city)

    def test_correct_capital_returned_when_country_is_uppercase(self):
        city = capitals.capital("HUNGARY")
        self.assertEqual("Budapest", city)

    def test_correct_capital_returned_when_country_is_lowercase(self):
        city = capitals.capital("hungary")
        self.assertEqual("Budapest", city)

    def test_correct_capital_returned_when_country_name_contains_multiple_words(self):
        city = capitals.capital("Saint Vincent And The Grenadines")
        self.assertEqual("Kingstown", city)

    def test_correct_output_returned_when_country_is_invalid(self):
        city = capitals.capital("Atlantis")
        self.assertEqual(0, city)

    def test_correct_help_message_displayed(self):
        help_message = b"""usage: capitals [country]\n\nDisplays capital city of specified country.\n\npositional arguments:\n  country     Displays the capital of country.\n\noptional arguments:\n  -h, --help  show this help message and exit\n"""

        command_output = subprocess.check_output(["python3", "capitals.py", "-h"])
        self.assertEqual(help_message,command_output)

    def test_correct_return_value_returned_when_running_interactively(self):
        return_value = subprocess.check_output(["python3", "capitals.py", "Hungary"])
        return_value = return_value.strip()
        self.assertEqual(b"The Capital city of Hungary is Budapest.", return_value)

    def test_correct_return_value_returned_when_not_running_interactively(self):
        city = capitals.capital("Hungary")
        self.assertEqual("Budapest", city)

    def test_correct_return_value_returned_when_country_is_incorrect(self):
        return_value = subprocess.check_output(["python3", "capitals.py", "Atlantis"])
        return_value = return_value.strip()
        self.assertEqual(b"Please enter a valid country name.", return_value)


if __name__ == "__main__":
    unittest.main()
