import os
print ("This is the file to push the current file into git repository")
print ("--------------------------------------------------------------------------------------------------------------")
#print ("please enter the comment for the commit")
m= raw_input("Please enter the comment for the commit\n")
os.system("git init")
os.system("git add --all")
os.system('git commit -m "'+m+'"')
os.system("git push -u origin master")

