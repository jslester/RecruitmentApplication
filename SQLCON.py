#!/usr/bin/python
import MySQLdb
#from sets import set
import xlsxwriter


# Create an new Excel file and add a worksheet.
worksheetExample = "demo.xlsx"
workbook = xlsxwriter.Workbook(worksheetExample)
worksheet = workbook.add_worksheet()

regularPrint = True
Individualperson = False
class Rushee:
    def __init__(self,FullName,comments,rating,SubmitName):
        self.FullName = FullName
        self.Comments = comments + ' - ' + SubmitName
        self.Total = 1
        self.rating = rating
        
        
db = MySQLdb.connect(host="",    # your host, usually localhost
                     user="",         # your username
                     passwd="",  # your password
                     db="",
                     port=80)        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM RushTable")
Rushee_List = []
# print all the first cell of all the rows
for row in cur.fetchall():
    Rushee_List.append(Rushee(row[1],row[2],row[3],row[4]))

db.close()

#List of all the unique Names in rush
Unique_Names = []

#List of each rushee as an object, including all aspects
Unique_List = []

#Cycle through the original list of Rushees
for OriginalRushee in Rushee_List:
    #Try to find duplciates for the first rushee in the list. The first rushee found will be the
    #Master rushee
    for PossibleDuplicateRushee in Rushee_List:
        #If they are the same object, we can skip them for this cycle
        if OriginalRushee != PossibleDuplicateRushee:
            #If they have the same picklist name, they must be about same person
            if OriginalRushee.FullName == PossibleDuplicateRushee.FullName:
                #Grab the comments from the duplicate and append them to the Master object
                OriginalRushee.Comments+= " | " + PossibleDuplicateRushee.Comments.replace('&rsquo;','')
                #Add up the rating from the duplicate submission
                OriginalRushee.rating+=PossibleDuplicateRushee.rating
                #Increment total number of Duplicates by 1
                OriginalRushee.Total+=1

    #At the end of the cycle for the Original rushee, if his name is not already
    #In this list of original rushees, add it, and add his object to UniqueList.
    #Since we have already checked all duolicates for his name, it no longer needs to
    #be edited.
    if OriginalRushee.FullName not in Unique_Names:
        Unique_Names.append(OriginalRushee.FullName)
        Unique_List.append(OriginalRushee)

#End print statements. These can be adjusted.
j = 1
if regularPrint:
    worksheet.write(0, 0, 'Rushee Name')
    worksheet.write(0, 1, 'Comments')
    worksheet.write(0, 2, 'Score')
    for i in Unique_List:
        print("Rushee Name: "+i.FullName)
        print("Comments about Rushee: " + i.Comments)
        #Since overall rating is incrememnted each time, it can be divided by the total
        #at the end to produce an average score for a rushee.
        print("Overall average Rating = "+ str(round(i.rating/i.Total,2)))
        print("\n")
        worksheet.write(j, 0, i.FullName)
        worksheet.write(j, 1, i.Comments)
        worksheet.write(j, 2, str(round(i.rating/i.Total,2)))
        j+=1      
    workbook.close()
    quit()
    
if Individualperson:
    print("Please enter the name of the rushee, you'd like to search for")
    Found = False
    Answer = input()
    print("\n")
    while(Answer!="exit"):
        for i in Unique_List:
            if Answer == i.FullName:
                Found = True
                print("Rushee Name: "+i.FullName)
                print("Comments about Rushee: " + i.Comments)
                #Since overall rating is incrememnted each time, it can be divided by the total
                #at the end to produce an average score for a rushee.
                print("Overall average Rating = "+ str(round(i.rating/i.Total,2)))
                print("\n")
                
        if not Found:
            print("The Rushee was not found in database!\n")
        print("Please enter the name of the rushee, you'd like to search for")
        Found = False
        Answer = input()
        print("\n")














    
