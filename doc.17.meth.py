
#  sorting on the basis of keys
color_dict = {'red':'rose','green':'plants','black':'hair','white':'shirt'}

for key in sorted(color_dict):
    print(key, color_dict[key])
	
 
 
color_dict ={'red':'rose',
          'green':'plants',
          'black':'hair',
          'white':'shirt'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))
	
 
 
 
# sorting on the basis of keys"
key_value={}

key_value[5] = 10      
key_value[3] = 8
key_value[6] = 77
key_value[4] = 23
key_value[2] = 9     
key_value[1] = 43
 
print("sorting on the basis of keys")

for i in sorted(key_value) :
    print ((i, key_value[i]), end =" ")

