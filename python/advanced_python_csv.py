import csv

def read_data(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        return(data)

def email_get(data):
	email_list = []
	for professors in data[1:]:
		email_list.append(professors[3])
	return(email_list)

def write_emails(list):
    with open('emails.csv', 'w') as file:
        writer = csv.writer(file)
        for email in list:
            writer.writerow([email])

def main():
    data = read_data('biostats2.csv')
    email_list = email_get(data)
    write_emails(email_list)

if __name__ == '__main__':
    main()
