# restart this program
def script():
    # program code here...
    restart = raw_input("Would you like to restart this program?")
    if restart == "yes" or restart == "y":
        script()
    if restart == "n" or restart == "no":
        print ("Script terminating. Goodbye.")
script()
