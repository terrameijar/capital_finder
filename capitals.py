#!/usr/bin/python

from sys import argv


def main():
    try:
        user_input = argv[1]
    except IndexError:
        print("You need to pass in a country as a commandline option")
        quit()

    countries = {}

    try:
        country_data = open('list.txt', 'r')
    except IOError:
        print("Country list file could not be opened.")
        quit()

    # Generate a dictionary from country list file.
    for each_line in country_data:
        try:
            (country_name, capital_city) = each_line.split(':', 1)
            country_name = country_name.strip()
            capital_city = capital_city.strip()
            countries[country_name] = capital_city  # "Japan": "Tokyo"
        except ValueError:
            pass

    try:
        if user_input.istitle():
            print("The Capital city of %s is %s." % (user_input, countries[user_input]))
        else:
            user_input = user_input.capitalize()
            print("The Capital City of %s is %s." % (user_input, countries[user_input]))
    except:
        print("Please enter a valid country name.")

if __name__ == "__main__":
    main()
