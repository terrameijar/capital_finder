# A program that tells the user what the capital city of the country they entered is.
#the country and city list should be stored in a separate text file. The program should read this file
# and create a data structure of sorts at run time.
#use a regex pattern to match country names

# author: terrameijar

def __init__():
	country = {}

	try:
		c_data = open('list.txt','r')

	except IOError as err:
		print("The file could not be opened " + str(err))
		quit()

	#Generate a dictionary from file data
	for each_line in c_data:
		try:
			(country_name, city) = each_line.split(':',1)
			country_name = country_name.strip()
			city = city.strip()
			country[country_name] = city # for example "Japan": "Tokyo"
			print country_name
		
		except ValueError:
			pass	

	try:
		cnt = raw_input("Enter country name: ")
		cnt = cnt.capitalize()
		print ("The Capital city of %s is %s.") %(cnt,country[cnt])

	except Exception as err:
		print("Please Enter a valid Country name")

if __name__ == '__main__':
	__init__()
