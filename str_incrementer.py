strng = "skla!@sdfjioweu2"
# this works rather than looping bc while looping through
# we attempt to loop through bunch of special characters amongst 
# characters and they would throw base(10) error i.e. STDERR
char_str = strng.rstrip('0123456789')
num_str = strng[len(char_str):]
        
if len(num_str) == 0:
    print(char_str + num_str + '1')
else:
    print(char_str + str(int(num_str)+1).zfill(len(num_str)))