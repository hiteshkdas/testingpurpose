import time

f = open('/home/ubuntu/workspace/test.txt')  
lines = f.readlines()  # return a list of lines in file
no = 0
last_lno= len(lines)
print last_lno
latest_line = lines[last_lno - 1]

start_last = latest_line.find('{"created_at":"') + 19
end_last = latest_line.find('","id"', start_last)

print latest_line[start_last:end_last]
a_latest_line = time.strptime(latest_line[start_last:end_last], '%b %d %H:%M:%S +0000 %Y')

a_latest_line = time.mktime(a_latest_line)

fob1_1 = open('/home/ubuntu/workspace/ext_hashtag.txt', 'a')
fob1_1.write ("The extracted hash tags in the 60 second window:" "\n")
fob1_1.close()

list_of_elements = []
list_of_b = []
hash_tag_list = []
dic_h = {}
dir_a = {}
for line in lines:
     testline = line[:line.find('created_at":"') + 43]
    
     print testline[19:]
     b_latest_line = time.strptime(testline[19:], '%b %d %H:%M:%S +0000 %Y')
     b_latest_line = time.mktime(b_latest_line)
     seconds = a_latest_line - b_latest_line
     print seconds
     start = line.find('{"text":"') + 110
     end = line.find('","source"', start)
    
     a= line[start:end]
     b= line[start:end].decode('unicode_escape').encode('ascii','ignore')
     
     if a == b:
         pass
     else:
         no = no + 1
         
     fob = open('/home/ubuntu/workspace/result.txt', 'a')
     fob.write (line[start:end].decode('unicode_escape').encode('ascii','ignore') + " (timestamp: " + testline[15:] + ")" "\n")
     fob.close()
     
     if seconds < 61:
     
        list_of_b += b.split()
     
        for element in list_of_b:
         
            if element.startswith("#"):
             
               hash_tag_list.append(element)
             
            else:
               pass
        print hash_tag_list 
        print len(hash_tag_list)
     
        fob1 = open('/home/ubuntu/workspace/ext_hashtag.txt', 'a')
        fob1.write (', '.join(hash_tag_list) +" (timestamp: " + testline[15:] + ")" "\n")
        fob1.close()
     
        if len(hash_tag_list) < 2:
           pass
        else:
           for hash_element in hash_tag_list:
           
              if dic_h == {}:
                  dir_a[hash_element]=(len(hash_tag_list) -1)
                  
              else:
                 
                for item in dic_h:
                    
                    if hash_element == item:
                        
                       dir_a[hash_element]=(len(hash_tag_list) -1) + dic_h[item]
                       break
                    else:
                     
                       dir_a[hash_element]=(len(hash_tag_list) -1)
                      
        dic_h = dir_a.copy()
             
        list_of_b = []
        hash_tag_list = []
     
f.close()

print no
print dir_a

fob2 = open('/home/ubuntu/workspace/ext_hashtag.txt', 'a')
fob2.write ("\n""\n""The degree of each node (hash tag):" "\n")
for item_1 in dir_a:
  fob2.write (item_1 +" : " + str(dir_a[item_1])+"\n")
fob2.close()


memb=0
tot=0
avg=0
for member in dir_a:
    memb=memb+1
    memb_val= int(dir_a[member])
    tot =memb_val+tot
    
avg = float(tot)/float(memb)
print avg
fob3 = open('/home/ubuntu/workspace/ext_hashtag.txt', 'a')
fob3.write ("\n""\n""The rolling average degree is:" "\n")
fob3.write (str(avg)+"\n")
fob3.close()


fob_agn = open('/home/ubuntu/workspace/result.txt', 'a')
fob_agn.write ("\n")
fob_agn.write (str(no) + " tweets contained unicode. \n")
fob_agn.close()
