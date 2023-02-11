from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  temp_list = []
pattern = '\s{1,}'
for column in contacts_list:
  fullname=column[0]+' '+column[1]+' '+column[2]
  column[0] = re.split(pattern, fullname)[0]
  column[1] = re.split(pattern, fullname)[1]
  column[2] = re.split(pattern, fullname)[2]
  regex = r"(\+7|8)\s*\(?(\d{3})\)?\s*\-?(\d{3})?\s*\-?(\d{2})?\s*\-?(\d{2})?\s*\(?(доб.)?\s*(\d*)?\)?"
  subst = "+7(\\2)\\3-\\4-\\5 \\6\\7"
  column[5] = re.sub(regex, subst, column[5], 0, re.MULTILINE)
for column in contacts_list:
  for another_user in contacts_list:
    if column[0] == another_user[0] and column[1] == another_user[1]:
      if len(column[2])<1:
        column[2] = another_user[2]
      if len(column[3]) < 1:
        column[3] = another_user[3]
      if len(column[4]) < 1:
        column[4] = another_user[4]
      if len(column[5]) < 1:
        column[5] = another_user[5]
      if len(column[6]) < 1:
        column[6] = another_user[6]
for contacts in contacts_list:
  if  contacts not in temp_list:
    temp_list.append(contacts)

# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(temp_list)