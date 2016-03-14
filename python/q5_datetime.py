import datetime as dt
import string

def number_days(day1, day2):
	da_stop = (day1.replace('-', '').replace('Jan', '1').replace('Feb', '2').replace('Mar', '3').replace('Apr', '4').replace('May', '5').replace('Jun', '6').replace('Jul', '7').replace('Aug', '8').replace('Sep', '9').replace('Oct', '10').replace('Nov', '11').replace('Dec', '12'))
	da_stop = int(da_stop)
	da_stop = dt.date(da_stop)
    
	da_start = (day2.replace('-', '').replace('Jan', '1').replace('Feb', '2').replace('Mar', '3').replace('Apr', '4').replace('May', '5').replace('Jun', '6').replace('Jul', '7').replace('Aug', '8').replace('Sep', '9').replace('Oct', '10').replace('Nov', '11').replace('Dec', '12'))
	da_start = int(da_start)
	da_start = dt.date(da_start)
    
	diff = (da_stop-da_start).days
	return(diff)

def main():
	#question a
	day1 = '01-02-2013'
	day2 = '07-28-2015'
	diff = number_days(day1, day2)
	print('the difference between', day1, 'and', day2, 'is', str(diff), 'days')
	
	#question b
	day1 = '12312013'
	day2 = '05282015'
	diff = number_days(day1, day2)
	print('the difference between', day1, 'and', day2, 'is', str(diff), 'days')
	
	#question c
	day1 = '15-Jan-1994'
	day2 = '14-Jul-2015'
	diff = number_days(day1, day2)
	print('the difference between', day1, 'and', day2, 'is', str(diff), 'days')

if __name__ == '__main__':
	main()
