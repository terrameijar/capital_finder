#!/usr/bin/python

# A program that tells the user what the capital city of the country they entered is.
#the country and city list should be stored in a separate text file. The program should read this file
# and create a data structure of sorts at run time.
#use a regex pattern to match country names

# author: terrameijar
from sys import argv

def __init__():
        try:
            cmd_country = argv[1]
        except:
            print("You need to pass in a country as a commandline option")
            quit()

	country = {}

	try:
		c_data = open('list.txt','r')

	except IOError as err:
		print("The country list file could not be opened " + str(err))
		quit()

	#Generate a dictionary from file data
	for each_line in c_data:
		try:
			(country_name, city) = each_line.split(':',1)
			country_name = country_name.strip()
			city = city.strip()
			country[country_name] = city # for example "Japan": "Tokyo"
		
		except ValueError:
			pass	

	try:
		if cmd_country.istitle():
                    print("The Capital city of %s is %s.") % (cmd_country,country[cmd_country])
                else:
		    cmd_country = cmd_country.capitalize()
		    print ("The Capital city of %s is %s.") % (cmd_country,country[cmd_country])

	except Exception as err:
	        print str(err)
		print("Please Enter a valid Country name")

if __name__ == '__main__':
	__init__()
