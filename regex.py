
import re
value="this is a string"
output=re.search("^This.*string$",value)
print(output)

pattern=r"^(?=.[a-z])(?=.[A-Z])(?=.[!@#$%^&()_+=-])(?=.{8,})"
# []	A set of characters
# \	    Signals a special sequence (can also be used to escape special characters)
# .	    Any character (except newline character)
# ^	    Starts with
# $	    Ends with
# *	    Zero or more occurrences
# +	    One or more occurrences
# ?	    Zero or one occurrences
# {}	Exactly the specified number of occurrences
# | 	Either or
# ()	Capture and group



# \A	Returns a match if the specified characters are at the beginning of the string	
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
#           (the "r" in the beginning is making sure that the string is being treated as a "raw string")	
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
#           (the "r" in the beginning is making sure that the string is being treated as a "raw string")	
# \d	Returns a match where the string contains digits (numbers from 0-9)	
# \D	Returns a match where the string DOES NOT contain digits	
# \s	Returns a match where the string contains a white space character	
# \S	Returns a match where the string DOES NOT contain a white space character	
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)		
# \W	Returns a match where the string DOES NOT contain any word characters
# \Z	Returns a match if the specified characters are at the end of the string



# [arn]	        Returns a match where one of the specified characters (a, r, or n) is present	
# [a-n] 	    Returns a match for any lower case character, alphabetically between a and n	
# [^arn]	    Returns a match for any character EXCEPT a, r, and n	
# [0123]    	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
# [0-9]	        Returns a match for any digit between 0 and 9	
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
# [a-zA-Z]	    Returns a match for any character alphabetically between a and z, lower case OR upper case	
# [+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string;
