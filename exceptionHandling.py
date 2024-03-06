# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# The try block will generate an exception,Since the try block raises an error, the except block will be executed.
# Without the try block, the program will crash and raise an error
try:
    f=open("demo.py")
    try:
        f.write("ABCD")
    except:
        print("Error in flie")
    finally:
        f.close()
except:
    print("Can't read this file")
    
    
        