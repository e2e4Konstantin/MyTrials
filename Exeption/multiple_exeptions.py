
#
# try:
#     first = float(input("What is your first number? "))
#     second = float(input("What is your second number? "))
#     print(f"{first} divided by {second} is {first / second}")
# except ValueError:
#     print("You must enter a number")
# except ZeroDivisionError:
#     print("You can't divide by zero")
#
#
# try:
#     pass # do something that may fail
# except (IDontLikeYouException, YouAreBeingMeanException) as e:
#     pass


try:
    may_raise_specific_errors():
except (SpecificErrorOne, SpecificErrorTwo) as error:
    handle(error) # might log or have some other default behavior...


import sys

try:
    mainstuff()
except (KeyboardInterrupt, EOFError): # the parens are necessary
    sys.exit(0)

try:
    mainstuff()
except (KeyboardInterrupt, EOFError) as err:
    print(err)
    print(err.args)
    sys.exit(0)


# 3.6
try:
    mainstuff()
except (KeyboardInterrupt, EOFError), err: # don't do this in Python 2.6+
    print err
    print err.args
    sys.exit(0)

from contextlib import suppress

with suppress(IDontLikeYouException, YouAreBeingMeanException):
     do_something()
So when you want to pass on certain exceptions, use suppress.



#This example code is a technique I use in a library that connects with websites to gather data

ConnectErrs  = (URLError, SSLError, SocketTimeoutError, BadStatusLine, ConnectionResetError)

def connect(url, data):
    #do connection and return some data
    return(received_data)

def some_function(var_a, var_b, ...):
    try: o = connect(url, data)
    except ConnectErrs as e:
        #do the recovery stuff
    blah #do normal stuff you would do if no exception occurred



try:
   You do your operations here;
   ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
   If there is any exception from the given exception list,
   then execute this block.
   ......................
else:
   If there is no exception then execute this block.




try:
   You do your operations here;
   ......................
except Exception1:
    functionname(parameterList)
except Exception2:
    functionname(parameterList)
except Exception3:
    functionname(parameterList)
else:
   If there is no exception then execute this block.

def functionname( parameters ):
   //your task..
   return [expression]
__________________________________________________________________________________________
