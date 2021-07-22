# initializing string 
test_str = "Mississippi"
  
 # of each element in string 
all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
  
# printing result 
print (" \n " +  str(all_freq))

