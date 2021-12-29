# title-name-organizer
This is a little python program that reads a csv file containing names and email addresses of clients.
Its common to find a company's database with client contacts has the title and name mixed up in the name column.
This program will help solve the issue by reading through the name column, identify if there is a title.
For contacts with titles, the program will format the full name as ([Title] [Name]) and where there is no title it will leave it as it were originally.
Some of the titles being looked for are ('MR', 'MS', 'DR','MRS', 'PROF', 'HON','REV','ENG','COL','MISS','MR.', 'MS.', 'DR.','MRS.', 'PROF.', 'HON.','REV.','ENG.','COL.','MISS.')
The final csv file will be writen in the final folder. This will not affect the original csv file.
