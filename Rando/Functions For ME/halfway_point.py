from datetime import datetime, timedelta

def get_duration_input(prompt):
    while True:
        try:
            time_str = input(prompt)
            time_obj = datetime.strptime(time_str, "%H:%M:%S")
            return timedelta(hours=time_obj.hour, minutes=time_obj.minute, seconds=time_obj.second)
        except ValueError:
            print("Invalid format. Please enter time in HH:MM:SS format.")

def halfway_point(time1, time2):
    return time1 + (time2 - time1) / 2

def main():
    print("Please enter the times in HH:MM:SS format.")
    time1 = get_duration_input("Enter the first time: ")
    time2 = get_duration_input("Enter the second time: ")
    
    halfway = halfway_point(time1, time2)
    halfway_time = (datetime.min + halfway).time()
    
    print(f"The halfway point between the two times is: {halfway_time}")

if __name__ == "__main__":
    main()