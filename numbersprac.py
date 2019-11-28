import sys
import statistics

def display_menu():
    print("mean: To get the mean")
    print("range: To get the range")
    print("mode: To get the range")
    print("median: To get the median")
    print("exit: To exit")
    choice = input("Choice:\t")
    return choice

def main():
    try:
        file_reader = open("scores.txt", "r")
        file_reader = file_reader.read()
        if len(file_reader) <= 0:
            print("There are no numbers")
        elif len(file_reader) >= 0:
            print("There are currently numbers")
    except FileNotFoundError as fe:
        print("File not found")
        sys.exit()
    user_continue = input("Would you like to update the list(Y)")
    if user_continue.lower() == "y":
        with open("scores.txt", "a") as file_update:
            while True:
                try:
                    integer = input("Number(N to stop):\t")
                    if integer.lower() == "n":
                        break
                    else:
                        integer = int(integer)
                        file_update.write(str(integer))
                        print("You have successfully added", integer)
                except ValueError as ve:
                    print("Value error. Please enter a proper integer")
    else:
        print("Exiting")
        quit()



def mean():
    with open("scores.txt", "r") as mean_reader:
        mean_list = []
        for numbers in mean_reader:
            numbers = int(numbers)
            mean_list.append(int(numbers))
            mean = sum(mean_list)/len(mean_list)
        print(mean)

def range_function():
    with open("scores.txt", "r") as range_reader:
        range_list = []
        for numbers in range_reader:
            numbers = int(numbers)
            range_list.append(int(numbers))
            maximum_num = max(range_list)
            minimum_num = min(range_list)
        print("The range is:\t", (str(maximum_num), str(minimum_num))) #Returns a tuple

def mode():
    with open("scores.txt", "r") as mode_reader:
        mode_list = []
        for numbers in mode_reader:
            numbers = int(numbers)
            mode_list.append(int(numbers))
        print("The mode is:\t", statistics.mode(mode_list))

def median():
    with open("scores.txt", "r") as median_reader:
        median_list = []
        for numbers in median_reader:
            numbers = int(numbers)
            median_list.append(int(numbers))
            n = len(median_list) 
            median_list.sort() 
              
            if n % 2 == 0: 
                median1 = median_list[n//2] 
                median2 = median_list[n//2 - 1] 
                median = (median1 + median2)/2
            else: 
                median = median_list[n//2] 
        print("Median is: " + str(median)) 
            

while True:
    choice = display_menu()
    if choice.lower() == "mode":
        mode()
    elif choice.lower() == "range":
        range_function()
    elif choice.lower() == "mean":
        mean()
    elif choice.lower() == "median":
        median()
    elif choice.lower() == "exit":
        break

if __name__ == "__main__":
    main()