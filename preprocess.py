




import csv


with open('spambase_preprocess.csv', 'w') as csvfile_out:
   	spamwriter = csv.writer(csvfile_out, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)

   	head = []
   	for i in range(1,58):
   		head.append("X"+str(i))


   	head.append("Y")
   	spamwriter.writerow(head)


   	with open('spambase.csv', 'r') as csvfile_in:
   		spamreader = csv.reader(csvfile_in, delimiter=',', quotechar='|')
   		for row in spamreader:
   			spamwriter.writerow(row)

