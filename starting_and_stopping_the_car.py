user_input = ''
started = stopped = False

while True:
    user_input = input("> ").lower().strip()
    
    if user_input == 'start':
        if started:
            print("Car already started bro!")
        else:
            started = True
            print("Car Started...Ready to go!")
        
    elif user_input == 'stop':
        if stopped:
            print("Car already stopped bro!")
        else:
            stopped = True
            print("Car Stopped!")
        
    elif user_input == 'help':
        print("""
        Start - Start the Car
        Stop - Stop the Car
        Quit - Quit"""
        )
        
    elif user_input == 'quit':
        print("Exiting...")
        break
    else:
        print("Uncrecognized command...")
