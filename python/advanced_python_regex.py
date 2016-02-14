import csv
import re
import string
def read_data(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        return(data)

def clean(degs):
	final_degs = []
	for degrees in degs.strip(string.whitespace).split(' '):
		deg_clean = degrees.replace('.','').upper()
		final_degs.append(deg_clean)
	return(final_degs)
	
	#this section is where the 1 is being attached
def make_histogram(data, num):
	dict = {}
	for professors in data[1:]:
		if num == 1:
			dl = clean(professors[num])
			if professors[num] == "0" or "":
				continue
			else:	
				for dict_entry in dl:
					dict[dict_entry] = dict.get(dict_entry, 0) + 1
				
		elif num == 2:
			professors[num] = professors[num].replace(" is", "of")
			dict[professors[num]] = dict.get(professors[num], 0) + 1
			#if re.search(dict[professors[num]], "is"):
			#	replace(re.search(dict[professors[num], "is" with ("of")
		
		
	return(dict)

def prnt_freq(dict):
	for dict_entry in dict:
		print(dict_entry, "appears %s times." % str(dict[dict_entry]))

def email_get(data):
	email_list = []
	for professors in data[1:]:
		email_list.append(professors[3])
	return(email_list)

def print_list(list):
		print(list)

def domain_get(email_list):
	domain_list = []
	dict = {}
	for item in email_list:
		uname, domain = item.split('@')
		domain_list.append(domain)
	for item in domain_list:
		dict[item] = dict.get(item, 0) + 1
	return(list(dict.keys()))

def main():
	data = read_data('biostats2.csv')
	deg_dict = make_histogram(data, 1)
	print('There are %d unique degrees.' % (len(deg_dict.keys())))
	prnt_freq(deg_dict)
	
	print("") #space for ease of reading

	titles_dict = make_histogram(data, 2)
	print('There are %d unique titles.' % (len(titles_dict.keys())))
	prnt_freq(titles_dict)

	print("") #space for ease of reading

	email_list = email_get(data)
	print_list(email_list)

	print("") #space for ease of reading

	domain_list = domain_get(email_list)
	print('There are %d unique domains.' % (len(domain_list)))
	#print_list(domain_list)

	email_list = email_get(data)
	print_list(domain_list)

if __name__ == '__main__':
	main()
