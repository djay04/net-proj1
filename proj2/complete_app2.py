import configparser
import logging
import sys

# creating configuration object to be utilized to parse files
config = configparser.ConfigParser()
config.read('configuration.ini')

# Setting up logging configurations in desired format
logging.basicConfig(filename='log_file.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s  %(message)s', filemode='w')

# Writing application activity to log file
logging.info("3461 Project 1 starting")

# iterating and printing each section in the confugration file
for section in config.sections():
    print(f"Section: {section}\n")
    # iterating and printing each option and its values 
    for key, value in config[section].items():

        # printing the key and value to the screen
        print(f"option {key} = {value}\n")

# while the user wants to enter a string
while True:

    # prompt user for input
    input_string = input('Please enter a string: ')

    # if the input is empty, prompt user for string again
    if not input_string:
        print("Nothing Entered...")
        logging.warning("Nothing entered...")
        continue
    
    # print string to screen
    print("Entered string =  ", input_string)

    # Writing application activity to log file
    logging.info("Entered string = %s ", input_string)

    # tokenize the string (split into words)
    tokenized_string = input_string.split()
    
    # capitalize the first word 
    tokenized_string[0] = tokenized_string[0].upper()

    # join the words back into one sentence
    result = ' '.join(tokenized_string)

    # Writing application activity to log file
    logging.info("Processed string = %s", result)

    if tokenized_string[0].upper() == "QUIT":
        print("Shutting down...")
        # Writing application activity to log file
        logging.info("Shutting down ... ")

        sys.exit()



# shut down logging activity
logging.shutdown()