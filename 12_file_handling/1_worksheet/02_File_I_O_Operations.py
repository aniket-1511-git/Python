'''
 Concepts: 
 Reading from and writing to files, handling file paths, and using context managers.    
 Task:  
 Create a script that reads a log file, filters specific lines (e.g., containing "ERROR"), and writes the filtered content to a new file.  
 Validation: 
 Check that the output file contains only the lines that meet the filter criteria. 
'''
fs= open('mixed_logs.log','r')
fd= open('err_logs.log','w')
for i in fs:
    if 'ERROR' in i:
        fd.write(i)
fs.close()
fd.close()

