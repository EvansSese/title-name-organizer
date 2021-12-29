#import dependencies
import pandas as pd
import csv

#import csv file
read_folder = 'original/'
write_folder = 'final/'
file = 'clients.csv'
read_path = read_folder + file
write_path = write_folder + file
data = pd.read_csv(read_path,encoding = 'unicode_escape')

#print(path)
#print(data['name'])

#read names in the name column
names = data['Name']

table_headers = ['Code','Name','Full Name','Email']
#write headers to final csv
with open(write_path, 'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(table_headers)

for i in range(len(names)):
    contact = []
    email = data['Email'][i]
    code = data['Code'][i]
    #print(name)
    name_items = data['Name'][i].split(' ')
    name = data['Name'][i]
    #print(name_items)
    titles = ['MR', 'MS', 'DR','MRS', 'PROF', 'HON','REV','ENG','COL','MISS','MR.', 'MS.', 'DR.','MRS.', 'PROF.', 'HON.','REV.','ENG.','COL.','MISS.']

    #check if name_items has any title
    res = any(title in name_items for title in titles)

    if res == True:
        for title in titles:
            if title in name_items:
                #print(title,name_items)
                #remove title from name items
                name_items.remove(title)
                #print(title,name_items)
                #combine title and name items
                name_items.insert(0,title)
                #print(title,name_items)
                full_name = ' '.join(name_items)
                #print(full_name)
                contact = [code,name,full_name,email]
                with open(write_path, 'a', newline='') as f:
                    write = csv.writer(f)
                    write.writerow(contact)
                print(contact)
                #write/append title and full name in new file
                break
    else:
        
        full_name = ' '.join(name_items)
        #print(full_name)
        contact = [code,name,full_name,email]
        with open(write_path, 'a', newline='') as f:
            write = csv.writer(f)
            write.writerow(contact)
        print(contact)
        #append full contact list

        #write/append full name in new file

    #print(str(res))

    #print("Next line")