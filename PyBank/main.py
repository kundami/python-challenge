# PyBank Homework
# This will allow us to create file paths across operating systems
import os
import csv

#Function to check for float value since I am getting an error
def isfloat(value):
    try:
        float(value)
        return True
    except:
        return False

# Finding the info to some of netlfix's most popular videos
files = ['1','2']
lines = []
period = []
change = []
total_revenue = 0.0
revenue_period = 0
change_revenue = 0.0
max_revenue = 0.0
max_revenue_1 = 0.0
min_revenue = 10000000000000
min_revenue_1 = 0.0
prev_period = ""
max_period = ""
max_period_1 = ""
min_period = ""
min_period_1 = ""

for filename_ext in files:
    print("filename ext:"+str(filename_ext))
    csvpath = os.path.join('Resources', 'budget_data_'+filename_ext+'.csv')

    # Improved Reading using CSV module
    with open(csvpath) as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        prev_revenue = 0.0
        #  Each row is read as a row
        next(csvreader,None)
        for row in csvreader:
            curr_date = row[0]
            curr_revenue = float(row[1])
            change_revenue = change_revenue + (curr_revenue - prev_revenue)
            if max_revenue <= (curr_revenue - prev_revenue):
                max_revenue = (curr_revenue - prev_revenue)
                max_revenue_1 = prev_revenue
                max_period = curr_date
                max_period_1 = prev_period
            if min_revenue >= (curr_revenue - prev_revenue):
                min_revenue = (curr_revenue - prev_revenue)
                mim_revenue_1 = prev_revenue
                min_period = curr_date
                min_period_1 = prev_period

            if isfloat(row[1])  == True:
                total_revenue = total_revenue+float(row[1])
                print("rev -"+row[1]+"prev_revenue:"+str(prev_revenue)+" curr rev:"+str(curr_revenue))
            else:
                print("bad float -"+row[1]+"prev_revenue:"+str(prev_revenue)+" curr rev:"+str(curr_revenue))
                total_revenue = total_revenue+0.0
            revenue_period = revenue_period + 1
            prev_revenue = float(row[1])
            prev_period = row[0]
            # print(row)

 
output_file = os.path.join('Output','Output.txt')
with open("Output.txt", "w") as text_file:
    print("Financial Analysis")
    text_file.write("Financial Analysis\n")
    print("-------------------------")
    text_file.write("-------------------------\n")
    print("Total Months:"+str(revenue_period))
    text_file.write("Total Months:"+str(revenue_period)+"\n")
    print("Total revenue:"+str(total_revenue))
    text_file.write("Total Revenue:"+str(total_revenue)+"\n")
    print ("Average Revenue Change:"+str(change_revenue/revenue_period))
    text_file.write("Average Revenue Change:"+str(change_revenue/revenue_period)+"\n")
    print ("Greatest Increase in Revenue:" + str(max_period)+" ("+str(max_revenue)+")" )
    text_file.write("Greatest Increase in Revenue:" + str(max_period)+" ("+str(max_revenue)+") \n" )
    print ("Greatest Decrease in Revenue:" + str(min_period)+" ("+str(min_revenue)+")" )
    text_file.write("Greatest Decrease in Revenue:" + str(min_period)+" ("+str(min_revenue)+") \n" )

text_file.close()

 