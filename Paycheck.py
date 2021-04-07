#***********************************************************************************************\
#Program Name:         Paycheckpro2.0
#Programmer:           Matthew Dalton
#Date Of Program:      Februrary 11, 2020
#Purpose:              Calculate take home pay for bi-weekly work period
#                      Prompt user for name, hours, payrate and insurance (if applicable)
#                      Take hours and pay rate, calculate gross pay and net pay, overtime if any
#                      Calculate deductions, Add paycheck amount and date to file
#Modules:              import os
#Input Variables:      hours_worked, hourly_wage[], paycheck_period, insurance_ask, name_ask
#Output:               hour_worked, hourly wage, insurance_amt, state_tax_amt, federal_tax_amt, medicare_amt
#                      readlogic(), writelogic(), deletelogic()
#***********************************************************************************************

#Function used to calculate entire paycheck

def paycheckProcessing(hours, hourly_wage, insurance_amt):
    
    state_tax_rate = .04
    federal_tax_rate = .05
    medicare_rate = .014
    social_security_rate = .06

    # Calculate Gross Pay, Check For Overtime
    if hours > 40:
        gross_pay = round((hourly_wage * 40) + ((hourly_wage * 1.5) * (hours - 40)), 3)
    else:
        gross_pay = round(hourly_wage * hours, 3)

    # Calculate Deductions
    state_tax_amt = round(gross_pay * state_tax_rate, 3)
    medicare_amt = round(gross_pay * medicare_rate, 3)
    federal_tax_amt = round(gross_pay * federal_tax_rate, 3)
    social_security_amt = round(gross_pay * social_security_rate, 3)
    net_pay = gross_pay - social_security_amt - state_tax_amt - medicare_amt - federal_tax_amt - float(insurance_amt)

    # Print Results
    print("  Hours-", hours, " ", "Hourly Pay Rate", hourly_wage)
    print("  Your gross pay will be", gross_pay)
    print("  Amount owed to state tax is", state_tax_amt)
    print("  Amount owed to federal tax is", federal_tax_amt)
    print("  Amount owed to medicare is", medicare_amt)
    print("  Amount owed to social security is", social_security_amt)

    return net_pay

#Getting user's possible insurance info

def Getinsurance():

    dental_insurance = 0
    health_insurance = 0
    vision_insurance = 0

    insurance_ask = input("Would you like to add insurance? (Y/N) ")
    if insurance_ask == "Y":
        health_insurance = float(input("How much is your health insurance? "))
        dental_insurance = float(input("How much is your dental insurance? "))
        vision_insurance = float(input("How much is your vision insurance? "))
    insurance_amt = health_insurance + dental_insurance + vision_insurance

    return insurance_amt

#Function for Viewing information in file

def readlogic():
    file = open ("c:/Users/Matt Dalton/Documents/paycheckpro.txt", "r")
    record = file.readline()
    while record:
        print(record)
        fields = record.split(",")
        print(fields[0], "\t\t\t\t", fields[1])
        record = file.readline()
    file.close()


#Function for writing/appending file

def writelogic(total_paycheck, paycheck_period):
    f = open("c:/Users/Matt Dalton/Documents/paycheckpro.txt", "a")
    record_to_write = str(total_paycheck) + "," + str(paycheck_period) + "\n"
    f.write(record_to_write)
    f.close()

#Imported library os to allow user to delete file if nessessary (new from original version)

def deletelogic():
    import os
    os.remove("c:/Users/Matt Dalton/Documents/paycheckpro.txt")

# Function to prompt user for two weeks of pay data

def add_check(insurance_amt):
    hourly_wage = float(input("what is your hourly wage? "))
    hours_worked[0] = float(input("How many hours did you work for week 1? "))
    hours_worked[1] = float(input("How many hours did you work for week 2? "))
    paycheck_period = input("Enter the date for this file ")

    net_pay_week_1 = paycheckProcessing(hours_worked[0], hourly_wage, insurance_amt)
    net_pay_week_2 = paycheckProcessing(hours_worked[1], hourly_wage, insurance_amt)
    total_paycheck = round(net_pay_week_1 + net_pay_week_2, 2)

    return total_paycheck, paycheck_period

#Initalizing everything to zero so it can be populated by the user's information

#dental_insurance = 0
#health_insurance = 0
#vision_insurance = 0
total_paycheck = 0
paycheck_period = 0
hourly_wage = 0
hours_worked = [0, 0]

# Prompt user for action needed
#   V - View Paychecks in file
#   A - Write Paychecks to file
#   D - Delete file
user_prompt = input("Would you like to (V)iew, (A)dd, or (D)elete? ")

name1 = input("Can I have a name for this check? ")

if user_prompt == "V":
    print("Thanks", name1, "I retrived this information for you")
    readlogic()
elif user_prompt == "A":
    insurance_amt = Getinsurance()
    total_paycheck, paycheck_period = add_check(insurance_amt)
    print("Amount deducted for insurance is", insurance_amt)
    print("Thanks", name1, "For using our paycheck calculator. Your Paycheck is", total_paycheck)
    writelogic(total_paycheck, paycheck_period)
elif user_prompt == "D":
    deletelogic()
else:
    print("The Value You Entered Is Invaild")

