#!/usr/bin/python3

from sys import argv
import argparse

TTY = False  # Flag will be set to true when running script interactively

def parse_arguments(arg):
    # Handles Commandline input
    PROGRAM = "capitals"
    DESCRIPTION = "Displays capital city of specified country."

    parser = argparse.ArgumentParser(
        prog=PROGRAM, description=DESCRIPTION
    )
    parser.add_argument('country', help="Displays the capital of <country>",
                        nargs='+')
    args = parser.parse_args(arg)
    country_data = ' '.join(args.country)
    return country_data


def get_list_of_countries():
    # Generate a dictionary from country list file.
    countries = {}

    try:
        country_data = open('list.txt', 'r')
    except IOError:
        print("Country list file could not be opened.")
        quit()
    try:
        for each_line in country_data:
            (country_name, capital_city) = each_line.split(':', 1)
            country_name = country_name.strip()
            capital_city = capital_city.strip()
            countries[country_name] = capital_city  # "Japan": "Tokyo"
        return countries
    except ValueError:
        pass


def capital(country):
    countries = get_list_of_countries()
    usr_country = country
    if TTY:
        try:
            if usr_country.istitle():
                print("The Capital city of %s is %s." %
                      (usr_country, countries[usr_country]))
            else:
                usr_country = usr_country.title()
                print("The Capital City of %s is %s." %
                      (usr_country, countries[usr_country]))
        except:
            print("Please enter a valid country name.")
    else:
        try:
            if usr_country.istitle():
                return countries[usr_country]
            else:
                usr_country = usr_country.title()
                return countries[usr_country]
        except:
            return 0


def main(country_arg):
    capital(parse_arguments(country_arg))


if __name__ == "__main__":
    # Everything except the script name is passed to main
    TTY = True
    main(argv[1:])
