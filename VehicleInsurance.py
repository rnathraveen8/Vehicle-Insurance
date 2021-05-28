from VehicleInsuranceConnectivity import *
from datetime import datetime
from datetime import timedelta
from datetime import date

def callCustomer(User_id):
    while True:
        print("                              ")
        print("1. Add Personal Details")
        print("2. New Insurance")
        print("3. Renew Insurance")
        print("4. Change Username/Password")
        print("5. Logout")
        print("             ")
        
        C = int(input("Enter Choice: "))

        if C == 1:
            print("             ")
            cn = input("Enter Customer Name: ")
            gen =  input("Enter Gender(M/F): ")
            dob = input("Enter DoB(yyyy/mm/dd): ")
            ad =  input("Enter Address: ")
            pc =  int(input("Enter PinCode: "))
            cno =  int(input("Enter Contact Number: "))
            mn =  input("Enter Mother's Name: ")
            fn =  input("Enter Father's Name: ")
            mar =  input("Enter Marital Status: ")

            mycursor.execute("INSERT INTO Customer(Customer_Num,Name,Gender,DOB,Address,Pincode,Contact_Number,Mother_Name,Father_Name,Marital_Status) VALUES({},'{}','{}','{}','{}',{},{},'{}','{}','{}')".format(User_id,cn,gen,dob,ad,pc,cno,mn,fn,mar))
            mydb.commit()
            print("             ")
            print("Customer Detail Added!!")
        elif C == 2:
            print("             ")
            print("Pick Insurance For")
            print("1. Car Insurance")
            print("2. Bike Insurance")
            print("3. Commercial Vehicle")
            print("             ")
            
            NI = int(input("Enter Choice: "))

            #Car Insurance
            if NI ==1:
                print("             ")
                print("Choice Type of Insurance")
                print("1. First Party Insurance")
                print("2. Third Party Insurance")
                print("             ")

                NiC = int(input("Enter Choice: "))


                #First Party Insurance Car
                if NiC == 1:
                    print("Select Time Period Of Insurance")
                    print("1. 1 year Plan")
                    print("2. 2 Year Plan")
                    print("             ")
                    TPI = int(input("Enter Choice: "))

                    if TPI == 1:
                        print("             ")
                        YeaR = input("Enter Vehicle Manufacture Year: ")
                        ModeL = input("Enter Vehicle Model: ")
                        ColoR = input("Enter Vehicle Color: ")
                        MileagE = input("Enter Vehicle Mileage: ")
                        VIN = input("Enter Vehicle VIN Number: ")
                        VNP = input("Enter Vehicle Plate Number: ")
                        VRS = input("Enter Vehicle Registered State: ")
                        print("             ")
                        # class in datetime module
                        Begindatestring = datetime.today()
                        # calculating end date by adding 365 days
                        Enddate = Begindatestring + timedelta(days=365)
                        print("             ")
                        print("You have to pay a Total Amount: Rs. 2,055")
                        P1 = input("To pay press Y: ")
                        
                        if P1 == 'Y':
                            print("             ")
                            mycursor.execute("INSERT INTO vehicle(ID,Year,Model,Color,Mileage,VINNumber,VehicleNumberPlate,VehicleRegisteredState,Vehicletype,VehicleInsuranceType) VALUES({},{},'{}','{}',{},'{}','{}','{}','Car','First Party Insurance')".format(User_id,YeaR,ModeL,ColoR,MileagE,VIN,VNP,VRS))
                            mydb.commit()
                            print("             ")
                            print("Vehicle Detail Saved!!")
                            
                            print("             ")
                            print("Payment Done")
                            mycursor.execute("INSERT INTO Policy(Policy_ID,PolicyEffecttiveDate,PolicyExpireDate,PolicyTimePeriod,TotalAmount,TypeOfPolicy) VALUES({},'{}','{}','1 Year','2055','First Party Insurance')".format(User_id,Begindatestring,Enddate))
                            mydb.commit()
                            print("             ")
                            print("Policy Registered!!!!!")
                            
                            print("             ")
                            mycursor.execute("select * from policy where Policy_ID = {}".format(User_id))
                            PP = mycursor.fetchone()
                            print("Policy ID: ",PP[0])
                            print("Policy Number: ",PP[1])
                            print("Policy Effective Date: ",PP[2])
                            print("Policy Expire Date: ",PP[3])
                            print("Policy Duration: ",PP[4])
                            print("Amout: Rs.",PP[5])
                            print("Type of Policy: ",PP[6])

                            print("             ")
                            mycursor.execute("select * from vehicle where ID = {}".format(User_id))
                            PV = mycursor.fetchone()
                            print("Vehicle ID: ",PV[0])
                            print("Vehicle Manufacture Year: ",PV[2])
                            print("Vehicle Model: ",PV[3])
                            print("Vehicle Colour: ",PV[4])
                            print("Vehicle Mileage: ",PV[5])
                            print("Vehicle VIN Number: ",PV[6])
                            print("Vehicle Number Plate: ",PV[7])
                            print("Vehicle Registered State: ",PV[8])
                            print("Vehicle Type: ",PV[9])
            
                        else:
                            print("Payment Not Done")
                            pass
                        
                    elif TPI ==2:
                        print("             ")
                        YeaR = input("Enter Vehicle Manufacture Year: ")
                        ModeL = input("Enter Vehicle Model: ")
                        ColoR = input("Enter Vehicle Color: ")
                        MileagE = input("Enter Vehicle Mileage: ")
                        VIN = input("Enter Vehicle VIN Number: ")
                        VNP = input("Enter Vehicle Plate Number: ")
                        VRS = input("Enter Vehicle Registered State: ")
                        print("             ")
                        # class in datetime module
                        Begindatestring = datetime.today()
                        # calculating end date by adding 365 days
                        Enddate = Begindatestring + timedelta(days=730)
                        print("             ")
                        print("You have to pay a Total Amount: Rs. 4,000")
                        P1 = input("To pay press Y: ")
                        
                        if P1 == 'Y':
                            print("             ")
                            mycursor.execute("INSERT INTO vehicle(ID,Year,Model,Color,Mileage,VINNumber,VehicleNumberPlate,VehicleRegisteredState,VehicletypeVehicleInsuranceType) VALUES({},{},'{}','{}',{},'{}','{}','{}','Car','First Party Insurance')".format(User_id,YeaR,ModeL,ColoR,MileagE,VIN,VNP,VRS))
                            mydb.commit()
                            print("             ")
                            print("Vehicle Detail Saved!!")
                            
                            print("             ")
                            print("Payment Done")
                            mycursor.execute("INSERT INTO Policy(Policy_ID,PolicyEffecttiveDate,PolicyExpireDate,PolicyTimePeriod,TotalAmount,TypeOfPolicy) VALUES({},'{}','{}','2 Year','4000','First Party Insurance')".format(User_id,Begindatestring,Enddate))
                            mydb.commit()
                            print("             ")
                            print("Policy Registered!!!!!")

                            print("             ")
                            mycursor.execute("select * from policy where Policy_ID = {}".format(User_id))
                            PP = mycursor.fetchone()
                            print("Policy ID: ",PP[0])
                            print("Policy Number: ",PP[1])
                            print("Policy Effective Date: ",PP[2])
                            print("Policy Expire Date: ",PP[3])
                            print("Policy Duration: ",PP[4])
                            print("Amout: Rs.",PP[5])
                            print("Type of Policy: ",PP[6])

                            print("             ")
                            mycursor.execute("select * from vehicle where ID = {}".format(User_id))
                            PV = mycursor.fetchone()
                            print("Vehicle ID: ",PV[0])
                            print("Vehicle Manufacture Year: ",PV[2])
                            print("Vehicle Model: ",PV[3])
                            print("Vehicle Colour: ",PV[4])
                            print("Vehicle Mileage: ",PV[5])
                            print("Vehicle VIN Number: ",PV[6])
                            print("Vehicle Number Plate: ",PV[7])
                            print("Vehicle Registered State: ",PV[8])
                            print("Vehicle Type: ",PV[9])
                        else:
                            print("Payment Not Done")
                            pass

                #Third Party Insurance Car
                elif NiC == 2:
                    print("Select Time Period Of Insurance")
                    print("1. 1 year Plan")
                    print("2. 2 Year Plan")
                    print("             ")
                    TPI = int(input("Enter Choice: "))

                    if TPI == 1:
                        print("             ")
                        YeaR = input("Enter Vehicle Manufacture Year: ")
                        ModeL = input("Enter Vehicle Model: ")
                        ColoR = input("Enter Vehicle Color: ")
                        MileagE = input("Enter Vehicle Mileage: ")
                        VIN = input("Enter Vehicle VIN Number: ")
                        VNP = input("Enter Vehicle Plate Number: ")
                        VRS = input("Enter Vehicle Registered State: ")
                        print("             ")
                        # class in datetime module
                        Begindatestring = datetime.today()
                        # calculating end date by adding 365 days
                        Enddate = Begindatestring + timedelta(days=365)
                        print("             ")
                        print("You have to pay a Total Amount: Rs. 1,895")
                        P1 = input("To pay press Y: ")
                        
                        if P1 == 'Y':
                            print("             ")
                            mycursor.execute("INSERT INTO vehicle(ID,Year,Model,Color,Mileage,VINNumber,VehicleNumberPlate,VehicleRegisteredState,Vehicletype,VehicleInsuranceType) VALUES({},{},'{}','{}',{},'{}','{}','{}','Car','Third Party Insurance')".format(User_id,YeaR,ModeL,ColoR,MileagE,VIN,VNP,VRS))
                            mydb.commit()
                            print("             ")
                            print("Vehicle Detail Saved!!")
                            
                            print("             ")
                            print("Payment Done")
                            mycursor.execute("INSERT INTO Policy(Policy_ID,PolicyEffecttiveDate,PolicyExpireDate,PolicyTimePeriod,TotalAmount,TypeOfPolicy) VALUES({},'{}','{}','1 Year','1895','Third Party Insurance')".format(User_id,Begindatestring,Enddate))
                            mydb.commit()
                            print("             ")
                            print("Policy Registered!!!!!")

                            print("             ")
                            mycursor.execute("select * from policy where Policy_ID = {}".format(User_id))
                            PP = mycursor.fetchone()
                            print("Policy ID: ",PP[0])
                            print("Policy Number: ",PP[1])
                            print("Policy Effective Date: ",PP[2])
                            print("Policy Expire Date: ",PP[3])
                            print("Policy Duration: ",PP[4])
                            print("Amout: Rs.",PP[5])
                            print("Type of Policy: ",PP[6])

                            print("             ")
                            mycursor.execute("select * from vehicle where ID = {}".format(User_id))
                            PV = mycursor.fetchone()
                            print("Vehicle ID: ",PV[0])
                            print("Vehicle Manufacture Year: ",PV[2])
                            print("Vehicle Model: ",PV[3])
                            print("Vehicle Colour: ",PV[4])
                            print("Vehicle Mileage: ",PV[5])
                            print("Vehicle VIN Number: ",PV[6])
                            print("Vehicle Number Plate: ",PV[7])
                            print("Vehicle Registered State: ",PV[8])
                            print("Vehicle Type: ",PV[9])
            
                        else:
                            print("Payment Not Done")
                            pass
                        
                    elif TPI ==2:
                        print("             ")
                        YeaR = input("Enter Vehicle Manufacture Year: ")
                        ModeL = input("Enter Vehicle Model: ")
                        ColoR = input("Enter Vehicle Color: ")
                        MileagE = input("Enter Vehicle Mileage: ")
                        VIN = input("Enter Vehicle VIN Number: ")
                        VNP = input("Enter Vehicle Plate Number: ")
                        VRS = input("Enter Vehicle Registered State: ")
                        print("             ")
                        # class in datetime module
                        Begindatestring = datetime.today()
                        # calculating end date by adding 365 days
                        Enddate = Begindatestring + timedelta(days=730)
                        print("             ")
                        print("You have to pay a Total Amount: Rs. 3,500")
                        P1 = input("To pay press Y: ")
                        
                        if P1 == 'Y':
                            print("             ")
                            mycursor.execute("INSERT INTO vehicle(ID,Year,Model,Color,Mileage,VINNumber,VehicleNumberPlate,VehicleRegisteredState,Vehicletype,VehicleInsuranceType) VALUES({},{},'{}','{}',{},'{}','{}','{}','Car','Third Party Insurance')".format(User_id,YeaR,ModeL,ColoR,MileagE,VIN,VNP,VRS))
                            mydb.commit()
                            print("             ")
                            print("Vehicle Detail Saved!!")
                            
                            print("             ")
                            print("Payment Done")
                            mycursor.execute("INSERT INTO Policy(Policy_ID,PolicyEffecttiveDate,PolicyExpireDate,PolicyTimePeriod,TotalAmount,TypeOfPolicy) VALUES({},'{}','{}','2 Year','3500','Third Party Insurance')".format(User_id,Begindatestring,Enddate))
                            mydb.commit()
                            print("             ")
                            print("Policy Registered!!!!!")

                            print("             ")
                            mycursor.execute("select * from policy where Policy_ID = {}".format(User_id))
                            PP = mycursor.fetchone()
                            print("Policy ID: ",PP[0])
                            print("Policy Number: ",PP[1])
                            print("Policy Effective Date: ",PP[2])
                            print("Policy Expire Date: ",PP[3])
                            print("Policy Duration: ",PP[4])
                            print("Amout: Rs.",PP[5])
                            print("Type of Policy: ",PP[6])

                            print("             ")
                            mycursor.execute("select * from vehicle where ID = {}".format(User_id))
                            PV = mycursor.fetchone()
                            print("Vehicle ID: ",PV[0])
                            print("Vehicle Manufacture Year: ",PV[2])
                            print("Vehicle Model: ",PV[3])
                            print("Vehicle Colour: ",PV[4])
                            print("Vehicle Mileage: ",PV[5])
                            print("Vehicle VIN Number: ",PV[6])
                            print("Vehicle Number Plate: ",PV[7])
                            print("Vehicle Registered State: ",PV[8])
                            print("Vehicle Type: ",PV[9])
                            
                        else:
                            print("Payment Not Done")
                            pass

            #Bike Insurance                     
            elif NI ==2:
                print("             ")
                print("Choice Type of Insurance")
                print("1. First Party Insurance")
                print("2. Third Party Insurance")
                print("             ")

                NiC = int(input("Enter Choice: "))
                
                #First Party Insurance Bike
                if NiC == 1:
                    print("Select Time Period Of Insurance")
                    print("1. 1 year Plan")
                    print("2. 2 Year Plan")
                    print("             ")
                    TPI = int(input("Enter Choice: "))

                    if TPI == 1:
                        print("             ")
                        YeaR = input("Enter Vehicle Manufacture Year: ")
                        ModeL = input("Enter Vehicle Model: ")
                        ColoR = input("Enter Vehicle Color: ")
                        MileagE = input("Enter Vehicle Mileage: ")
                        VIN = input("Enter Vehicle VIN Number: ")
                        VNP = input("Enter Vehicle Plate Number: ")
                        VRS = input("Enter Vehicle Registered State: ")
                        print("             ")
                        # class in datetime module
                        Begindatestring = datetime.today()
                        # calculating end date by adding 365 days
                        Enddate = Begindatestring + timedelta(days=365)
                        print("             ")
                        print("You have to pay a Total Amount: Rs. 2,000")
                        P1 = input("To pay press Y: ")
                        
                        if P1 == 'Y':
                            print("             ")
                            mycursor.execute("INSERT INTO vehicle(ID,Year,Model,Color,Mileage,VINNumber,VehicleNumberPlate,VehicleRegisteredState,Vehicletype,VehicleInsuranceType) VALUES({},{},'{}','{}',{},'{}','{}','{}','Bike','First Party Insurance')".format(User_id,YeaR,ModeL,ColoR,MileagE,VIN,VNP,VRS))
                            mydb.commit()
                            print("             ")
                            print("Vehicle Detail Saved!!")
                            
                            print("             ")
                            print("Payment Done")
                            mycursor.execute("INSERT INTO Policy(Policy_ID,PolicyEffecttiveDate,PolicyExpireDate,PolicyTimePeriod,TotalAmount,TypeOfPolicy) VALUES({},'{}','{}','1 Year','2000','First Party Insurance')".format(User_id,Begindatestring,Enddate))
                            mydb.commit()
                            print("             ")
                            print("Policy Registered!!!!!")

                            print("             ")
                            mycursor.execute("select * from policy where Policy_ID = {}".format(User_id))
                            PP = mycursor.fetchone()
                            print("Policy ID: ",PP[0])
                            print("Policy Number: ",PP[1])
                            print("Policy Effective Date: ",PP[2])
                            print("Policy Expire Date: ",PP[3])
                            print("Policy Duration: ",PP[4])
                            print("Amout: Rs.",PP[5])
                            print("Type of Policy: ",PP[6])

                            print("             ")
                            mycursor.execute("select * from vehicle where ID = {}".format(User_id))
                            PV = mycursor.fetchone()
                            print("Vehicle ID: ",PV[0])
                            print("Vehicle Manufacture Year: ",PV[2])
                            print("Vehicle Model: ",PV[3])
                            print("Vehicle Colour: ",PV[4])
                            print("Vehicle Mileage: ",PV[5])
                            print("Vehicle VIN Number: ",PV[6])
                            print("Vehicle Number Plate: ",PV[7])
                            print("Vehicle Registered State: ",PV[8])
                            print("Vehicle Type: ",PV[9])
                        else:
                            print("Payment Not Done")
                            pass
                        
                    elif TPI ==2:
                        print("             ")
                        YeaR = input("Enter Vehicle Manufacture Year: ")
                        ModeL = input("Enter Vehicle Model: ")
                        ColoR = input("Enter Vehicle Color: ")
                        MileagE = input("Enter Vehicle Mileage: ")
                        VIN = input("Enter Vehicle VIN Number: ")
                        VNP = input("Enter Vehicle Plate Number: ")
                        VRS = input("Enter Vehicle Registered State: ")
                        print("             ")
                        # class in datetime module
                        Begindatestring = datetime.today()
                        # calculating end date by adding 365 days
                        Enddate = Begindatestring + timedelta(days=730)
                        print("             ")
                        print("You have to pay a Total Amount: Rs. 3,580")
                        P1 = input("To pay press Y: ")
                        
                        if P1 == 'Y':
                            print("             ")
                            mycursor.execute("INSERT INTO vehicle(ID,Year,Model,Color,Mileage,VINNumber,VehicleNumberPlate,VehicleRegisteredState,Vehicletype,VehicleInsuranceType) VALUES({},{},'{}','{}',{},'{}','{}','{}','Bike','First Party Insurance')".format(User_id,YeaR,ModeL,ColoR,MileagE,VIN,VNP,VRS))
                            mydb.commit()
                            print("             ")
                            print("Vehicle Detail Saved!!")
                            
                            print("             ")
                            print("Payment Done")
                            mycursor.execute("INSERT INTO Policy(Policy_ID,PolicyEffecttiveDate,PolicyExpireDate,PolicyTimePeriod,TotalAmount,TypeOfPolicy) VALUES({},'{}','{}','2 Year','3580','First Party Insurance')".format(User_id,Begindatestring,Enddate))
                            mydb.commit()
                            print("             ")
                            print("Policy Registered!!!!!")

                            print("             ")
                            mycursor.execute("select * from policy where Policy_ID = {}".format(User_id))
                            PP = mycursor.fetchone()
                            print("Policy ID: ",PP[0])
                            print("Policy Number: ",PP[1])
                            print("Policy Effective Date: ",PP[2])
                            print("Policy Expire Date: ",PP[3])
                            print("Policy Duration: ",PP[4])
                            print("Amout: Rs.",PP[5])
                            print("Type of Policy: ",PP[6])

                            print("             ")
                            mycursor.execute("select * from vehicle where ID = {}".format(User_id))
                            PV = mycursor.fetchone()
                            print("Vehicle ID: ",PV[0])
                            print("Vehicle Manufacture Year: ",PV[2])
                            print("Vehicle Model: ",PV[3])
                            print("Vehicle Colour: ",PV[4])
                            print("Vehicle Mileage: ",PV[5])
                            print("Vehicle VIN Number: ",PV[6])
                            print("Vehicle Number Plate: ",PV[7])
                            print("Vehicle Registered State: ",PV[8])
                            print("Vehicle Type: ",PV[9])
                        else:
                            print("Payment Not Done")
                            pass

                #Third Party Insurance Bike
                elif NiC == 2:
                    print("Select Time Period Of Insurance")
                    print("1. 1 year Plan")
                    print("2. 2 Year Plan")
                    print("             ")

                    TPI = int(input("Enter Choice: "))

                    if TPI == 1:
                        print("             ")
                        YeaR = input("Enter Vehicle Manufacture Year: ")
                        ModeL = input("Enter Vehicle Model: ")
                        ColoR = input("Enter Vehicle Color: ")
                        MileagE = input("Enter Vehicle Mileage: ")
                        VIN = input("Enter Vehicle VIN Number: ")
                        VNP = input("Enter Vehicle Plate Number: ")
                        VRS = input("Enter Vehicle Registered State: ")
                        print("             ")
                        # class in datetime module
                        Begindatestring = datetime.today()
                        # calculating end date by adding 365 days
                        Enddate = Begindatestring + timedelta(days=365)
                        print("             ")
                        print("You have to pay a Total Amount: Rs. 1,595")
                        P1 = input("To pay press Y: ")
                        
                        if P1 == 'Y':
                            print("             ")
                            mycursor.execute("INSERT INTO vehicle(ID,Year,Model,Color,Mileage,VINNumber,VehicleNumberPlate,VehicleRegisteredState,Vehicletype,VehicleInsuranceType) VALUES({},{},'{}','{}',{},'{}','{}','{}','Bike','Third Party Insurance')".format(User_id,YeaR,ModeL,ColoR,MileagE,VIN,VNP,VRS))
                            mydb.commit()
                            print("             ")
                            print("Vehicle Detail Saved!!")
                            
                            print("             ")
                            print("Payment Done")
                            mycursor.execute("INSERT INTO Policy(Policy_ID,PolicyEffecttiveDate,PolicyExpireDate,PolicyTimePeriod,TotalAmount,TypeOfPolicy) VALUES({},'{}','{}','1 Year','1595','Third Party Insurance')".format(User_id,Begindatestring,Enddate))
                            mydb.commit()
                            print("             ")
                            print("Policy Registered!!!!!")

                            print("             ")
                            mycursor.execute("select * from policy where Policy_ID = {}".format(User_id))
                            PP = mycursor.fetchone()
                            print("Policy ID: ",PP[0])
                            print("Policy Number: ",PP[1])
                            print("Policy Effective Date: ",PP[2])
                            print("Policy Expire Date: ",PP[3])
                            print("Policy Duration: ",PP[4])
                            print("Amout: Rs.",PP[5])
                            print("Type of Policy: ",PP[6])

                            print("             ")
                            mycursor.execute("select * from vehicle where ID = {}".format(User_id))
                            PV = mycursor.fetchone()
                            print("Vehicle ID: ",PV[0])
                            print("Vehicle Manufacture Year: ",PV[2])
                            print("Vehicle Model: ",PV[3])
                            print("Vehicle Colour: ",PV[4])
                            print("Vehicle Mileage: ",PV[5])
                            print("Vehicle VIN Number: ",PV[6])
                            print("Vehicle Number Plate: ",PV[7])
                            print("Vehicle Registered State: ",PV[8])
                            print("Vehicle Type: ",PV[9])
                        else:
                            print("Payment Not Done")
                            pass
                        
                    elif TPI == 2:
                        print("             ")
                        YeaR = input("Enter Vehicle Manufacture Year: ")
                        ModeL = input("Enter Vehicle Model: ")
                        ColoR = input("Enter Vehicle Color: ")
                        MileagE = input("Enter Vehicle Mileage: ")
                        VIN = input("Enter Vehicle VIN Number: ")
                        VNP = input("Enter Vehicle Plate Number: ")
                        VRS = input("Enter Vehicle Registered State: ")
                        print("             ")
                        # class in datetime module
                        Begindatestring = datetime.today()
                        # calculating end date by adding 365 days
                        Enddate = Begindatestring + timedelta(days=730)
                        print("             ")
                        print("You have to pay a Total Amount: Rs. 3,000")
                        P1 = input("To pay press Y: ")
                        
                        if P1 == 'Y':
                            print("             ")
                            mycursor.execute("INSERT INTO vehicle(ID,Year,Model,Color,Mileage,VINNumber,VehicleNumberPlate,VehicleRegisteredState,Vehicletype,VehicleInsuranceType) VALUES({},{},'{}','{}',{},'{}','{}','{}','Bike','Third Party Insurance')".format(User_id,YeaR,ModeL,ColoR,MileagE,VIN,VNP,VRS))
                            mydb.commit()
                            print("             ")
                            print("Vehicle Detail Saved!!")
                            
                            print("             ")
                            print("Payment Done")
                            mycursor.execute("INSERT INTO Policy(Policy_ID,PolicyEffecttiveDate,PolicyExpireDate,PolicyTimePeriod,TotalAmount,TypeOfPolicy) VALUES({},'{}','{}','2 Year','3000','Third Party Insurance')".format(User_id,Begindatestring,Enddate))
                            mydb.commit()
                            print("             ")
                            print("Policy Registered!!!!!")

                            print("             ")
                            mycursor.execute("select * from policy where Policy_ID = {}".format(User_id))
                            PP = mycursor.fetchone()
                            print("Policy ID: ",PP[0])
                            print("Policy Number: ",PP[1])
                            print("Policy Effective Date: ",PP[2])
                            print("Policy Expire Date: ",PP[3])
                            print("Policy Duration: ",PP[4])
                            print("Amout: Rs.",PP[5])
                            print("Type of Policy: ",PP[6])

                            print("             ")
                            mycursor.execute("select * from vehicle where ID = {}".format(User_id))
                            PV = mycursor.fetchone()
                            print("Vehicle ID: ",PV[0])
                            print("Vehicle Manufacture Year: ",PV[2])
                            print("Vehicle Model: ",PV[3])
                            print("Vehicle Colour: ",PV[4])
                            print("Vehicle Mileage: ",PV[5])
                            print("Vehicle VIN Number: ",PV[6])
                            print("Vehicle Number Plate: ",PV[7])
                            print("Vehicle Registered State: ",PV[8])
                            print("Vehicle Type: ",PV[9])
                        else:
                            print("Payment Not Done")
                            pass

            #Commercial Vehicle   
            elif NI == 3:
                print("             ")
                print("Choice Type of Insurance")
                print("1. First Party Insurance")
                print("2. Third Party Insurance")
                print("             ")

                NiC = int(input("Enter Choice: "))

                #First Party Insurance Commercial Vehicle
                if NiC == 1:
                    print("Select Time Period Of Insurance")
                    print("1. 1 year Plan")
                    print("2. 2 Year Plan")
                    print("             ")
                    TPI = int(input("Enter Choice: "))

                    if TPI == 1:
                        print("             ")
                        YeaR = input("Enter Vehicle Manufacture Year: ")
                        ModeL = input("Enter Vehicle Model: ")
                        ColoR = input("Enter Vehicle Color: ")
                        MileagE = input("Enter Vehicle Mileage: ")
                        VIN = input("Enter Vehicle VIN Number: ")
                        VNP = input("Enter Vehicle Plate Number: ")
                        VRS = input("Enter Vehicle Registered State: ")
                        print("             ")
                        # class in datetime module
                        Begindatestring = datetime.today()
                        # calculating end date by adding 365 days
                        Enddate = Begindatestring + timedelta(days=365)
                        print("             ")
                        print("You have to pay a Total Amount: Rs. 3,000")
                        P1 = input("To pay press Y: ")
                        
                        if P1 == 'Y':
                            print("             ")
                            mycursor.execute("INSERT INTO vehicle(ID,Year,Model,Color,Mileage,VINNumber,VehicleNumberPlate,VehicleRegisteredState,Vehicletype,VehicleInsuranceType) VALUES({},{},'{}','{}',{},'{}','{}','{}','Commercial Vehicle','First Party Insurance')".format(User_id,YeaR,ModeL,ColoR,MileagE,VIN,VNP,VRS))
                            mydb.commit()
                            print("             ")
                            print("Vehicle Detail Saved!!")
                            
                            print("             ")
                            print("Payment Done")
                            mycursor.execute("INSERT INTO Policy(Policy_ID,PolicyEffecttiveDate,PolicyExpireDate,PolicyTimePeriod,TotalAmount,TypeOfPolicy) VALUES({},'{}','{}','1 Year','3000','First Party Insurance')".format(User_id,Begindatestring,Enddate))
                            mydb.commit()
                            print("             ")
                            print("Policy Registered!!!!!")

                            print("             ")
                            mycursor.execute("select * from policy where Policy_ID = {}".format(User_id))
                            PP = mycursor.fetchone()
                            print("Policy ID: ",PP[0])
                            print("Policy Number: ",PP[1])
                            print("Policy Effective Date: ",PP[2])
                            print("Policy Expire Date: ",PP[3])
                            print("Policy Duration: ",PP[4])
                            print("Amout: Rs.",PP[5])
                            print("Type of Policy: ",PP[6])

                            print("             ")
                            mycursor.execute("select * from vehicle where ID = {}".format(User_id))
                            PV = mycursor.fetchone()
                            print("Vehicle ID: ",PV[0])
                            print("Vehicle Manufacture Year: ",PV[2])
                            print("Vehicle Model: ",PV[3])
                            print("Vehicle Colour: ",PV[4])
                            print("Vehicle Mileage: ",PV[5])
                            print("Vehicle VIN Number: ",PV[6])
                            print("Vehicle Number Plate: ",PV[7])
                            print("Vehicle Registered State: ",PV[8])
                            print("Vehicle Type: ",PV[9])
                        else:
                            print("Payment Not Done")
                            pass
                        
                    elif TPI ==2:
                        print("             ")
                        YeaR = input("Enter Vehicle Manufacture Year: ")
                        ModeL = input("Enter Vehicle Model: ")
                        ColoR = input("Enter Vehicle Color: ")
                        MileagE = input("Enter Vehicle Mileage: ")
                        VIN = input("Enter Vehicle VIN Number: ")
                        VNP = input("Enter Vehicle Plate Number: ")
                        VRS = input("Enter Vehicle Registered State: ")
                        print("             ")
                        # class in datetime module
                        Begindatestring = datetime.today()
                        # calculating end date by adding 365 days
                        Enddate = Begindatestring + timedelta(days=730)
                        print("             ")
                        print("You have to pay a Total Amount: Rs. 5,000")
                        P1 = input("To pay press Y: ")
                        
                        if P1 == 'Y':
                            print("             ")
                            mycursor.execute("INSERT INTO vehicle(ID,Year,Model,Color,Mileage,VINNumber,VehicleNumberPlate,VehicleRegisteredState,Vehicletype,VehicleInsuranceType) VALUES({},{},'{}','{}',{},'{}','{}','{}','Commercial Vehicle','First Party Insurance')".format(User_id,YeaR,ModeL,ColoR,MileagE,VIN,VNP,VRS))
                            mydb.commit()
                            print("             ")
                            print("Vehicle Detail Saved!!")
                            
                            print("             ")
                            print("Payment Done")
                            mycursor.execute("INSERT INTO Policy(Policy_ID,PolicyEffecttiveDate,PolicyExpireDate,PolicyTimePeriod,TotalAmount,TypeOfPolicy) VALUES({},'{}','{}','2 Year','5000','First Party Insurance')".format(User_id,Begindatestring,Enddate))
                            mydb.commit()
                            print("             ")
                            print("Policy Registered!!!!!")

                            print("             ")
                            mycursor.execute("select * from policy where Policy_ID = {}".format(User_id))
                            PP = mycursor.fetchone()
                            print("Policy ID: ",PP[0])
                            print("Policy Number: ",PP[1])
                            print("Policy Effective Date: ",PP[2])
                            print("Policy Expire Date: ",PP[3])
                            print("Policy Duration: ",PP[4])
                            print("Amout: Rs.",PP[5])
                            print("Type of Policy: ",PP[6])

                            print("             ")
                            mycursor.execute("select * from vehicle where ID = {}".format(User_id))
                            PV = mycursor.fetchone()
                            print("Vehicle ID: ",PV[0])
                            print("Vehicle Manufacture Year: ",PV[2])
                            print("Vehicle Model: ",PV[3])
                            print("Vehicle Colour: ",PV[4])
                            print("Vehicle Mileage: ",PV[5])
                            print("Vehicle VIN Number: ",PV[6])
                            print("Vehicle Number Plate: ",PV[7])
                            print("Vehicle Registered State: ",PV[8])
                            print("Vehicle Type: ",PV[9])
                        else:
                            print("Payment Not Done")
                            pass

                #Third Party Insurance Commercial Vehicle
                elif NiC == 2:
                    print("Select Time Period Of Insurance")
                    print("1. 1 year Plan")
                    print("2. 2 Year Plan")
                    print("             ")
                    TPI = int(input("Enter Choice: "))

                    if TPI == 1:
                        print("             ")
                        YeaR = input("Enter Vehicle Manufacture Year: ")
                        ModeL = input("Enter Vehicle Model: ")
                        ColoR = input("Enter Vehicle Color: ")
                        MileagE = input("Enter Vehicle Mileage: ")
                        VIN = input("Enter Vehicle VIN Number: ")
                        VNP = input("Enter Vehicle Plate Number: ")
                        VRS = input("Enter Vehicle Registered State: ")
                        print("             ")
                        # class in datetime module
                        Begindatestring = datetime.today()
                        # calculating end date by adding 365 days
                        Enddate = Begindatestring + timedelta(days=365)
                        print("             ")
                        print("You have to pay a Total Amount: Rs. 2,000")
                        P1 = input("To pay press Y: ")
                        
                        if P1 == 'Y':
                            print("             ")
                            mycursor.execute("INSERT INTO vehicle(ID,Year,Model,Color,Mileage,VINNumber,VehicleNumberPlate,VehicleRegisteredState,Vehicletype,VehicleInsuranceType) VALUES({},{},'{}','{}',{},'{}','{}','{}','Commercial Vehicle','Third Party Insurance')".format(User_id,YeaR,ModeL,ColoR,MileagE,VIN,VNP,VRS))
                            mydb.commit()
                            print("             ")
                            print("Vehicle Detail Saved!!")
                            
                            print("             ")
                            print("Payment Done")
                            mycursor.execute("INSERT INTO Policy(Policy_ID,PolicyEffecttiveDate,PolicyExpireDate,PolicyTimePeriod,TotalAmount,TypeOfPolicy) VALUES({},'{}','{}','1 Year','1595','Third Party Insurance')".format(User_id,Begindatestring,Enddate))
                            mydb.commit()
                            print("             ")
                            print("Policy Registered!!!!!")

                            print("             ")
                            mycursor.execute("select * from policy where Policy_ID = {}".format(User_id))
                            PP = mycursor.fetchone()
                            print("Policy ID: ",PP[0])
                            print("Policy Number: ",PP[1])
                            print("Policy Effective Date: ",PP[2])
                            print("Policy Expire Date: ",PP[3])
                            print("Policy Duration: ",PP[4])
                            print("Amout: Rs.",PP[5])
                            print("Type of Policy: ",PP[6])

                            print("             ")
                            mycursor.execute("select * from vehicle where ID = {}".format(User_id))
                            PV = mycursor.fetchone()
                            print("Vehicle ID: ",PV[0])
                            print("Vehicle Manufacture Year: ",PV[2])
                            print("Vehicle Model: ",PV[3])
                            print("Vehicle Colour: ",PV[4])
                            print("Vehicle Mileage: ",PV[5])
                            print("Vehicle VIN Number: ",PV[6])
                            print("Vehicle Number Plate: ",PV[7])
                            print("Vehicle Registered State: ",PV[8])
                            print("Vehicle Type: ",PV[9])
                        else:
                            print("Payment Not Done")
                            pass
                        
                    elif TPI ==2:
                        print("             ")
                        YeaR = input("Enter Vehicle Manufacture Year: ")
                        ModeL = input("Enter Vehicle Model: ")
                        ColoR = input("Enter Vehicle Color: ")
                        MileagE = input("Enter Vehicle Mileage: ")
                        VIN = input("Enter Vehicle VIN Number: ")
                        VNP = input("Enter Vehicle Plate Number: ")
                        VRS = input("Enter Vehicle Registered State: ")
                        print("             ")
                        # class in datetime module
                        Begindatestring = datetime.today()
                        # calculating end date by adding 365 days
                        Enddate = Begindatestring + timedelta(days=730)
                        print("             ")
                        print("You have to pay a Total Amount: Rs. 3,985")
                        P1 = input("To pay press Y: ")
                        
                        if P1 == 'Y':
                            print("             ")
                            mycursor.execute("INSERT INTO vehicle(ID,Year,Model,Color,Mileage,VINNumber,VehicleNumberPlate,VehicleRegisteredState,Vehicletype,VehicleInsuranceType) VALUES({},{},'{}','{}',{},'{}','{}','{}','Commercial Vehicle','Third Party Insurance')".format(User_id,YeaR,ModeL,ColoR,MileagE,VIN,VNP,VRS))
                            mydb.commit()
                            print("             ")
                            print("Vehicle Detail Saved!!")
                            
                            print("             ")
                            print("Payment Done")
                            mycursor.execute("INSERT INTO Policy(Policy_ID,PolicyEffecttiveDate,PolicyExpireDate,PolicyTimePeriod,TotalAmount,TypeOfPolicy) VALUES({},'{}','{}','2 Year','3985','Third Party Insurance')".format(User_id,Begindatestring,Enddate))
                            mydb.commit()
                            print("             ")
                            print("Policy Registered!!!!!")

                            print("             ")
                            mycursor.execute("select * from policy where Policy_ID = {}".format(User_id))
                            PP = mycursor.fetchone()
                            print("Policy ID: ",PP[0])
                            print("Policy Number: ",PP[1])
                            print("Policy Effective Date: ",PP[2])
                            print("Policy Expire Date: ",PP[3])
                            print("Policy Duration: ",PP[4])
                            print("Amout: Rs.",PP[5])
                            print("Type of Policy: ",PP[6])

                            print("             ")
                            mycursor.execute("select * from vehicle where ID = {}".format(User_id))
                            PV = mycursor.fetchone()
                            print("Vehicle ID: ",PV[0])
                            print("Vehicle Manufacture Year: ",PV[2])
                            print("Vehicle Model: ",PV[3])
                            print("Vehicle Colour: ",PV[4])
                            print("Vehicle Mileage: ",PV[5])
                            print("Vehicle VIN Number: ",PV[6])
                            print("Vehicle Number Plate: ",PV[7])
                            print("Vehicle Registered State: ",PV[8])
                            print("Vehicle Type: ",PV[9])
                        else:
                            print("Payment Not Done")
                            pass
            
        elif C == 3:
            ID = int(input("Enter Your Customer ID: "))
            if ID == User_id:
                try:
                    print("     ")  
                    PNum = int(input("Enter Policy Number: "))
                    
                    mycursor.execute("select * from policy where PolicyNumber = '{}'".format(PNum))
                    pp = mycursor.fetchone()
                    
                    print("Total Amount to Pay: Rs.",pp[5])
                    P = input("To pay Enter YES: ")
                    if P == 'YES':
                        if pp[4] == '1 Year':
                            Begindatestring = datetime.today()
                            Enddate = Begindatestring + timedelta(days=365)
                            mycursor.execute("update policy set PolicyEffecttiveDate = '{}' where PolicyNumber='{}'".format(Begindatestring,PNum))
                            mydb.commit()
                            print("     ")
                            mycursor.execute("update policy set PolicyExpireDate = '{}' where PolicyNumber='{}'".format(Enddate,PNum))
                            mydb.commit()
                            print("Payment Done!!!")
                            print("     ")
                            print("Policy Renewed")
                            
                            mycursor.execute("select * from policy where PolicyNumber = '{}'".format(PNum))
                            l = mycursor.fetchone()
                            print("     ")
                            print("Policy ID: ",l[0])
                            print("Policy Number: ",l[1])
                            print("Policy Effective Date: ",l[2])
                            print("Policy Expire Date: ",l[3])
                            print("Policy Duration: ",l[4])
                            print("Amout: Rs.",l[5])
                            print("Type of Policy: ",l[6])
                            
                        elif pp[4] == '2 Year':
                            Begindatestring = datetime.today()
                            Enddate = Begindatestring + timedelta(days=730)
                            mycursor.execute("update policy set PolicyEffecttiveDate = '{}' where PolicyNumber ='{}'".format(Begindatestring,PNum))
                            mydb.commit()
                            print("     ")
                            mycursor.execute("update policy set PolicyExpireDate = '{}' where PolicyNumber ='{}'".format(Enddate,PNum))
                            mydb.commit()
                            print("Payment Done!!!")
                            
                            print("     ")
                            print("Policy Renewed")

                            mycursor.execute("select * from policy where PolicyNumber = '{}'".format(PNum))
                            l = mycursor.fetchone()
                            print("     ")
                            print("Policy ID: ",l[0])
                            print("Policy Number: ",l[1])
                            print("Policy Effective Date: ",l[2])
                            print("Policy Expire Date: ",l[3])
                            print("Policy Duration: ",l[4])
                            print("Amout: Rs.",l[5])
                            print("Type of Policy: ",l[6])
                            
                    else:
                        print("Payment Canceled")
                except:
                    print("This Policy Number does not belong to you")
            else:
                print("Entered Wrong ID")
        elif C == 4:
            print("             ")
            print("1.Update Username")
            print("2.Update Password")
            print("             ")
            
            umcc = int(input("Enter Choise: "))

            if umcc == 1:
                print("             ")
                upunameC = input("New Username: ")
                
                mycursor.execute("update login set Username='{}' where User_role='Customer'".format(upunameC))
                mydb.commit()
                print("             ")
                print("Username Updated!!")
            elif umcc == 2:
                print("             ")
                uppasswordC = input("New Password: ")
                
                mycursor.execute("update login set User_password='{}' where User_role='Customer'".format(uppasswordC))
                mydb.commit()
                print("             ")
                print("Password Updated!!")
        elif C == 5:
            break

def callManger():
    while True:
        print("             ")
        print("1. Add User")
        print("2. Search ")
        print("3. Change Username/Password")
        print("4. Logout")
        print("             ")
        
        cM = int(input("Enter Choice: "))
        
        if cM == 1:
            print("             ")
            print("1. Add Manger User Login ID")
            print("2. Add Agent User Login ID")
            print("3. Add Customer User Login ID")
            
            print("             ")
            
            Ad = int(input("Enter Choice: "))

            if Ad == 1:
                print("             ")
                un = input("Enter UserName: ")
                pwd = input("Enter Password: ")
                nm = input("Enter Name: ")

                mycursor.execute("insert into Login(Username,User_password,Name,User_role) VALUES('{}','{}','{}','Manger')".format(un,pwd,nm))
                mydb.commit()
                print("             ")
                print("Manger Added!!")
            elif Ad ==2:
                print("             ")
                un = input("Enter UserName: ")
                pwd = input("Enter Password: ")
                nm = input("Enter Name: ")

                mycursor.execute("insert into Login(Username,User_password,Name,User_role) VALUES('{}','{}','{}','Agent')".format(un,pwd,nm))
                mydb.commit()
                print("             ")
                print("Agent Added!!")
            elif Ad ==3:
                print("             ")
                un = input("Enter UserName: ")
                pwd = input("Enter Password: ")
                nm = input("Enter Name: ")

                mycursor.execute("insert into Login(Username,User_password,Name,User_role) VALUES('{}','{}','{}','Customer')".format(un,pwd,nm))
                mydb.commit()
                print("             ")
                print("Customer Added!!")

        elif cM == 2:
            print("              ")
            print("1.Search Agent")
            print("2.Search Customer")
            print("3.Search Policy")
            print("4.Search Vehicle")

            SE = int(input("Enter Choise: "))
            
            

            if SE ==1:
                try:
                    print("        ")
                    Agent = input("Enter Agent ID: ")
                    mycursor.execute("select * from agent where Agent_ID = {}".format(Agent))
                    AI = mycursor.fetchone()
                    print("        ")
                    print("Agent ID: ",AI[0])
                    print("Agent Name: ",AI[1])
                    print("Agent Gender",AI[2])
                    print("Agent Date Of Birth: ",AI[3])
                    print("Agent Address: ",AI[4])
                    print("Agent Pincode: ",AI[5])
                    print("Agent Contact Number: ",AI[6])
                    print("Agent Mother's Name: ",AI[7])
                    print("Agent Father's Name: ",AI[8])
                except:
                    print("This is not a Agent ID")
                    

            elif SE == 2:
                try:
                    print("        ")
                    Customer = int(input("Enter Customer ID: "))
                    mycursor.execute("select * from customer where Customer_Num = {}".format(Customer))
                    CI = mycursor.fetchone()
                    print("        ")
                    print("Customer ID Number: ",CI[0])
                    print("Customer Name: ",CI[1])
                    print("Customer Gender",CI[2])
                    print("Customer Date Of Birth: ",CI[3])
                    print("Customer Address: ",CI[4])
                    print("Customer Pincode: ",CI[5])
                    print("Customer Contact Number: ",CI[6])
                    print("Customer Mother's Name: ",CI[7])
                    print("Customer Father's Name: ",CI[8])
                    print("Customer Marital Status: ",CI[9])
                except:
                    print("This is not a Customer ID")
            elif SE == 3:
                try:
                    print("             ")
                    Policy = int(input("Enter Policy ID: "))
                    mycursor.execute("select * from policy where Policy_ID = {}".format(Policy))
                    j = mycursor.fetchall()
                    count = 0
                    for PP in j:
                        print("Policy ID: ",PP[0])
                        print("Policy Number: ",PP[1])
                        print("Policy Effective Date: ",PP[2])
                        print("Policy Expire Date: ",PP[3])
                        print("Policy Duration: ",PP[4])
                        print("Amout: Rs.",PP[5])
                        print("Type of Policy: ",PP[6])
                        print("          ")
                        count = count + 1
                except:
                    print("This is not a Policy ID")
            elif SE == 4:
                try:
                    print("             ")
                    Vehicle = int(input("Enter Vehicle Number: "))
                    mycursor.execute("select * from vehicle where ID = {}".format(Vehicle))
                    i = mycursor.fetchall()
                    count = 0
                    for PV in i:
                        print("Vehicle ID: ",PV[0])
                        print("Vehicle Number: ")
                        print("Vehicle Manufacture Year: ",PV[2])
                        print("Vehicle Model: ",PV[3])
                        print("Vehicle Colour: ",PV[4])
                        print("Vehicle Mileage: ",PV[5])
                        print("Vehicle VIN Number: ",PV[6])
                        print("Vehicle Number Plate: ",PV[7])
                        print("Vehicle Registered State: ",PV[8])
                        print("Vehicle Type: ",PV[9])
                        print("             ")
                        count = count + 1
                except:
                    print("This is not a Vehicle ID")

        elif cM == 3:
            print("             ")
            print("1.Update Username")
            print("2.Update Password")
            print("             ")
            
            umcc = int(input("Enter Choise: "))

            if umcc == 1:
                print("             ")
                upunameC = input("New Username: ")
                
                mycursor.execute("update login set Username='{}' where User_role='Manger'".format(upunameC))
                mydb.commit()
                print("             ")
                print("Username Updated!!")
            elif umcc == 2:
                print("             ")
                uppasswordC = input("New Password: ")
                
                mycursor.execute("update login set User_password='{}' where User_role='Manger'".format(uppasswordC))
                mydb.commit()
                print("             ")
                print("Password Updated!!")

        elif cM == 4:
            break


def callAgent(User_id):
    while True:
        print("       ")
        print("1. Add Personal Details")
        print("2. Add Customer")
        print("3. Search Customer Details")
        print("4. Update Username/Password")
        print("5. Logout")
        
        print("       ")
        CA = int(input("Enter Choice: "))
        if CA == 1:
            print("             ")
            cn = input("Enter Agent Name: ")
            gen =  input("Enter Gender(M/F): ")
            dob = input("Enter DoB(yyyy/mm/dd): ")
            ad =  input("Enter Address: ")
            pc =  int(input("Enter PinCode: "))
            cno =  int(input("Enter Contact Number: "))
            mn =  input("Enter Mother's Name: ")
            fn =  input("Enter Father's Name: ")

            mycursor.execute("INSERT INTO agent(Agent_ID,Name,Gender,DOB,Address,Pincode,Contact_Number,Mother_Name,Father_Name) VALUES({},'{}','{}','{}','{}',{},{},'{}','{}')".format(User_id,cn,gen,dob,ad,pc,cno,mn,fn))
            mydb.commit()
            print("             ")
            print("Agent Detail Added!!")
        elif CA == 2:
            print("             ")
            un = input("Enter UserName: ")
            pwd = input("Enter Password: ")
            nm = input("Enter Name: ")
            mycursor.execute("insert into Login(Username,User_password,Name,User_role) VALUES('{}','{}','{}','Customer')".format(un,pwd,nm))
            mydb.commit()
            print("             ")
            print("Customer Added!!")
        elif CA == 3:
            try:
                print("        ")
                Customer = int(input("Enter Customer ID: "))
                mycursor.execute("select * from customer where Customer_Num = {}".format(Customer))
                CI = mycursor.fetchone()
                print("        ")
                print("Customer ID Number: ",CI[0])
                print("Customer Name: ",CI[1])
                print("Customer Gender",CI[2])
                print("Customer Date Of Birth: ",CI[3])
                print("Customer Address: ",CI[4])
                print("Customer Pincode: ",CI[5])
                print("Customer Contact Number: ",CI[6])
                print("Customer Mother's Name: ",CI[7])
                print("Customer Father's Name: ",CI[8])
                print("Customer Marital Status: ",CI[9])
            except:
                print("This is not a Customer ID")
        elif CA == 4:
             print("1.Update Username")
             print("2.Update Password")
             print("             ")
             umca = int(input("Enter Choice: "))
             if umca == 1:
                 upunameA = input("New Username: ")
                 mycursor.execute("update login set username='{}' where User_role='Agent'".format(upunameA))
                 mydb.commit()
                 print("             ")
                 print("Username Updated!!")
             elif umca == 2:
                 uppasswordA = input("New Password: ")
                 mycursor.execute("update login set User_password='{}' where User_role='Agent'".format(uppasswordA))
                 mydb.commit()
                 print("             ")
                 print("Password Updated!!")

        elif CA == 5:
            break




un = input("Enter UserName: ")
pwd = input("Enter Password: ")

mycursor.execute("select * from Login where Username='{}' and User_password='{}'".format(un, pwd))
udata = mycursor.fetchone()

if udata:
    print("=====Welcome {}======".format(udata[3]))
    if udata[4] == 'Manger':
        callManger()
    elif udata[4] == "Customer":
        callCustomer(udata[0])
    elif udata[4] == "Agent":
        callAgent(udata[0])
else:
    print("Invalid Username or Password!")

