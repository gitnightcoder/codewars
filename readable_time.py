time = 359999

temp = []
temp.extend([str(time // 3600).zfill(2),
             str(time%3600//60).zfill(2),
             str(time%3600%60%60).zfill(2)]) 
    
print(':'.join([i for i in temp]))

#please check other solutions for this code again