import datetime as dt
import string

def number_days(day1, day2):
	da_stop = (day1.replace('-', '').replace('Jan', '01').replace('Feb', '02').replace('Mar', '03').replace('Apr', '04').replace('May', '05').replace('Jun', '06').replace('Jul', '07').replace('Aug', '08').replace('Sep', '09').replace('Oct', '10').replace('Nov', '11').replace('Dec', '12'))
	da_stop = dt.date(int(da_stop[2:]), int(da_stop[:2]), int(da_stop[3:5]))
	
	da_start = (day2.replace('-', '').replace('Jan', '01').replace('Feb', '02').replace('Mar', '03').replace('Apr', '04').replace('May', '05').replace('Jun', '06').replace('Jul', '07').replace('Aug', '08').replace('Sep', '09').replace('Oct', '10').replace('Nov', '11').replace('Dec', '12'))
	da_start = dt.date(int(da_start[2:]), int(da_start[:2]), int(da_start[3:5]))
	
	return(da_stop-da_start).days

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
