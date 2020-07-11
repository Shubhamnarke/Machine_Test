
''' Question 2 : Assume some email address like "username@companyname.com",now write a snippet that extracts the 
company name of a given email
address.'''

email = 'shubhamnarke@codehube.com'

email = str(email)
count = 0
index = []
for i in email:
	count+=1
	if i == '@':
		index.append(count)
	elif i == '.':
		index.append(count-1)
	else:
		pass
		
start = index[0]
stop = index[1]

print('Company name is : ' + email[start : stop])

