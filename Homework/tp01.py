#import the important modules (csv to manage csv and txt files .. , webbrowser to open our file html in browser ..)#
import csv
import webbrowser
#open csv file in mode read#
csv_file = open("etudiants.txt", "r")
# open html file in mode write to write the output inside it
html_file = open("students.html", "w")
# read TXT file with reader() and appends all data from csv file to csv_reader attr
csv_reader = csv.reader(csv_file, delimiter=',')

line_count = 0
# the head and body of the html file
html_t = """
<!DOCTYPE html>
    <head>
        <title>CSV to HTML</title>
        <meta charset = 'utf-8'>
        <style>
            body{
                background-color: #DDD;
            }
            table{
                width:100%;
            }table ,td,th{
                border-collapse: collapse;
            }
            th, td {
                padding: 10px;
                text-align: left;
            }
            table tr:nth-child(even) {
                background-color: #b1b1b1;
            }
            table tr:nth-child(odd) {
                background-color: #fff;
            }
            table th {
                background-color: black;
                color: white;
                border:1px solid black
            }
        </style>
    </head>
    <body>
        <h2> Students list </h2>
        <br>
        <table>
            <thead>
                <tr>"""

#################################################
###### Start Reading and collecting data ########
#################################################

item_count = 0
# list with the first line in csv file
table_head = []
# list with the reste of the lines in the csv file
table_body = []
# loop for to read the csv file line by line
for line in csv_reader:
    if line_count == 0:
        while item_count != len(line):
            #append the items in the first line of the csv file to tabel_head list#
            table_head.append("<th>"+line[item_count]+"</th>")
            #item_count ++ to pass in to the next item in the first line#
            item_count += 1
        #line_count ++ to stop append the rest of the lines in to table_head list#
        line_count += 1
    else:
        #append the rest of lines to table_body list#
        table_body.append(line)
        #line_count ++ to pass to the next line#
        line_count += 1
#write the content of the html_t attr (in the top of code) to html file (students.html) with write()#
html_file.write(html_t)
#append <th> html elements to table_head list#
table_head.append('<th>Moy Gene</th>')
table_head.append('<th>Result</th>')
#attr to calc nmbr of Admin & ajournee & admis avec dettes students#
nbr_admis = 0
nbr_ajournee = 0
nbr_ad_a_dette = 0

for th in table_head:
    html_file.write("""
                    %s""" % th)
html_file.write("""
                </tr>
            </thead>
            <tbody>""")
for tb in table_body:
    html_file.write("""
                <tr>""")
    for tb_data in tb:
        html_file.write("""
                    <td> %s </td>""" % tb_data)
    html_file.write("""
                    <td> %s </td>""" % ((float(tb[3])+float(tb[4]))/2))
    if float(tb[3]) >= 10 and float(tb[4]) >= 10:
        nbr_admis += 1
        html_file.write("""
                    <td> Admis </td>""")
    else:
        if float(tb[3]) < 10 or float(tb[4]) < 10:
            if int(tb[5]) > 45:
                nbr_ad_a_dette += 1
                html_file.write("""
                    <td> Admis ave detts </td>""")
            else:
                nbr_ajournee += 1
                html_file.write("""
                    <td> Ajournee </td>""")
    html_file.write("""
                </tr>""")
html_file.write("""
            </tbody>
        </table > 
        </br>
        </br>
        <h2> Top Grade </h2>
        <span> is : </span>""")

################################
### Start get year results #####
################################

students_grade = []
students_nmbr = 0
print(nbr_admis)
print(nbr_ajournee)
print(nbr_ad_a_dette)
#access to table_body list and get the s1 and s2 moy to calc the Moyen Gen#
for tb in table_body:
    #append to students_grade list all the Moy gene of the students#
    students_grade.append((float(tb[3])+float(tb[4])) / 2)
    #calc the student's number#
    students_nmbr += 1
#write to the html file some Statical like (top grade , worst grade , number of students admis...)#
html_file.write("""
        <span><b>%s / 20</b></span>""" % max(students_grade))
html_file.write("""
        <h2>Worst Grade</h2>
        <span>is : </span>
        <span><b>%s / 20</b></span>""" % min(students_grade))
html_file.write("""
        <h2>Statistics</h2>
        <p>Number of students Admis : <b>%s</b> """% nbr_admis)
html_file.write("""of %s """%students_nmbr)
html_file.write(""" ( %s%% ) </p>
        """%(nbr_admis * 100 /students_nmbr))

html_file.write("""<p>Number of students Admis avec dette : <b>%s</b> """% nbr_ad_a_dette)
html_file.write(""" of %s """%students_nmbr)
html_file.write(""" ( %s%% )</p>
        """%(nbr_ad_a_dette* 100 /students_nmbr))

html_file.write("""<p>Number of students Ajournee : <b>%s</b> """% nbr_ajournee)
html_file.write(""" of %s """%students_nmbr)
html_file.write("""( %s%% )</p>"""%(nbr_ajournee * 100 /students_nmbr))

html_file.write("""
    </body>
</html>""")
#########################################
## End write all data to the htnl file ##
#########################################

#close the file#
html_file.close()
#the link of the html file in the disk#
filename = '/home/yasser_dx/Desktop/Python/students.html'
#open html file in new tab in the browser#
webbrowser.open_new_tab(filename)
