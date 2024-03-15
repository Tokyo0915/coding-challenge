from datetime import datetime
import csv
import os
import sys

def check_arguments(args):
    if len(args) != 4:
        print(f"Usage: {args[0]} <csv_file> -d yyyy-mm-dd")
        return False
    if not os.path.isfile(args[1]) or not args[1].lower().endswith('.csv'):
        print("Invalid CSV file path provided.")
        return False
    if args[2] != "-d":
        print('Command line flag must be "-d".')
        return False
    try:
        datetime.strptime(args[3], "%Y-%m-%d")
    except ValueError:
        print("Date must be in format: yyyy-mm-dd")
        return False
    return True

def process_cookies(file_path, target_date):
    cookie_count = {}
    with open(file_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            timestamp = row['timestamp']
            timestamp_datetime = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z")
            if target_date.strftime("%Y-%m-%d") == timestamp_datetime.strftime("%Y-%m-%d"):
                cookie = row['cookie']
                cookie_count[cookie] = cookie_count.get(cookie, 0) + 1
    return cookie_count

def most_active_cookies(cookie_count):
    if not cookie_count:
        print("Date not found.")
        return
    max_count = max(cookie_count.values())
    most_active = [cookie for cookie, count in cookie_count.items() if count == max_count]
    for cookie in most_active:
        print(cookie)

def main():

    if not check_arguments(sys.argv):
        sys.exit(1)
    
    file_path = sys.argv[1]
    target_date = datetime.strptime(sys.argv[3], "%Y-%m-%d")
    
    cookie_count = process_cookies(file_path, target_date)
 
    most_active_cookies(cookie_count)

if __name__ == "__main__":
    main()