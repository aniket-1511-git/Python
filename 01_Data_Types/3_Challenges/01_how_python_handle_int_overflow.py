'''
How does Python handle integer overflow, and what happens if you assign a 
value greater than what a C/C++ int would allow?
'''
'''
1.In Python, integers can grow beyond the limits of C/C++ integers without 
overflow.
2.Python handles large integers gracefully, allowing for calculations that would overflow in statically typed languages like C/C++.
'''
x = 2147483647  
x += 1          
print(x)        
