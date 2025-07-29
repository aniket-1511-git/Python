'''
 Concepts: 
    Try-except blocks, raising exceptions, and creating custom error messages.  
 Task:  Create a script that attempts to open a file and gracefully handles the case when the file is missing, logging an appropriate error message.  
 Validation: Simulate a missing file scenario and confirm that the error is caught and logged as expected. 
 '''
try:
     fs=open('err_logs.log','r')
     
except FileNotFoundError:
    print("Err : file not found")

    