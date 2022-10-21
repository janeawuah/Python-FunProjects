import time


def countdown(time_entered):
    
    while time_entered:
        mins, secs = divmod(time_entered, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        time_entered -= 1
      
    print('Times UP!!!!!')
  
  
# input time in seconds
time_entered = input("Please enter the time in seconds: ")
  
# function call
countdown(int(time_entered))