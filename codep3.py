from tkinter import * 
from tkinter import ttk
import sqlite3
from datetime import date

root = Tk()
root.title("CAR RENTAL SYSTEM")





def lw1():
    w= Toplevel(root)
    w.title('Add new customer')
    w.geometry('600x600')
    top_frame = Frame(w)
    bottom_frame =Frame(w) 

    cname_label = Label(top_frame, text = 'Customer name')
    cname_entry = Entry(top_frame,)
    cph_label = Label(top_frame, text = 'Customer phone')
    cph_entry = Entry(top_frame)

    cname_label.grid(row = 0, column=0)
    cname_entry.grid(row = 0, column=1)
    cph_label.grid(row = 1, column=0)
    cph_entry.grid(row = 1, column=1)

    top_frame.grid(row=0)
    bottom_frame.grid(row=1)

    def addCustomer():
        submit_conn = sqlite3.connect('car-rental.db')
        submit_curr = submit_conn.cursor()
        #passing in user defined input
        submit_curr.execute("INSERT INTO CUSTOMER (`Name`,`Phone`) VALUES (:name, :phone)", 
        {
            'name': cname_entry.get(),
            'phone': cph_entry.get(),
        })
        Label(bottom_frame, text='Thank you ' + cname_entry.get() +', You have been added as a Customer!').grid(row = 1)
        submit_conn.commit()
        submit_conn.close()

    addCustomerButton = Button(top_frame, text = 'Add Customer', command=addCustomer)
    addCustomerButton.grid(row = 6, column=0, columnspan=2, pady=10, ipadx=100)


def lw2():
    w = Toplevel(root)
    w.title('Add new vehicle')
    w.geometry('600x600')
    top_frame = Frame(w)
    bottom_frame =Frame(w) # for sql query output

    #label and entry boxes below this

    vid_label = Label(top_frame, text = 'Vehicle ID')
    vid_entry = Entry(top_frame,)
    vdesc_label = Label(top_frame, text = 'Vehicle Description')
    vdesc_entry = Entry(top_frame)
    vyear_label = Label(top_frame, text = 'Year')
    vyear_entry = Entry(top_frame,)
    vtype_label = Label(top_frame, text = 'Type')
    vtype_entry = Entry(top_frame)
    vcat_label = Label(top_frame, text = 'Category')
    vcat_entry = Entry(top_frame,)
    

    vid_label.grid(row=0,column=0)
    vid_entry.grid(row=0,column=1)
    vdesc_label.grid(row=1,column=0)
    vdesc_entry.grid(row=1,column=1)
    vyear_label.grid(row=2,column=0)
    vyear_entry.grid(row=2,column=1)
    vtype_label.grid(row=3,column=0)
    vtype_entry.grid(row=3,column=1)
    vcat_label .grid(row=4,column=0)
    vcat_entry .grid(row=4,column=1)


    top_frame.grid(row=0)
    bottom_frame.grid(row=1)

    def addVehicle():
        submit_conn = sqlite3.connect('car-rental.db')
        submit_curr = submit_conn.cursor()
        #passing in user defined input
        submit_curr.execute("INSERT INTO VEHICLE VALUES (:vehicleID, :description, :year, :typeV, :category)", 
        {
            'vehicleID': vid_entry.get(),
            'description': vdesc_entry.get(),
            'year': vyear_entry.get(),
            'typeV': vtype_entry.get(),
            'category': vcat_entry.get(),
        })
        submit_conn.commit()
        submit_conn.close()
        printMess = Label(bottom_frame, text='The vehicle with:\n ID: ' + vid_entry.get() +' \nDescription: ' + vdesc_entry.get() + '\nYear: ' + vyear_entry.get() + ' \nType: ' + vtype_entry.get() + ' \nCategory: ' + vcat_entry.get() + ' has been successfully added!')
        printMess.grid(row = 1)

    addCustomerButton = Button(top_frame, text = 'Add Vehicle', command=addVehicle)
    addCustomerButton.grid(row = 6, column=0, columnspan=2, pady=10, ipadx=100)

def getCategory():
    cat = sqlite3.connect('car-rental.db')
    cat_cur = cat.cursor()
    cat_cur.execute('SELECT DISTINCT Category FROM RATE')
    cat_list = cat_cur.fetchall()
    print(cat_list)
    cat.close() 
    return cat_list

def getType():
    type = sqlite3.connect('car-rental.db')
    type_cur = type.cursor()
    type_cur.execute('SELECT DISTINCT Type FROM RATE')
    type_list = type_cur.fetchall()
    print(type_list)
    type.close() 
    return type_list

def lw3():
    w = Toplevel(root)
    w.title('Add new reservation')
    w.geometry('600x600')
    top_frame = Frame(w)
    bottom_frame =Frame(w) # for sql query output
    catList = getCategory()
    typeList = getType()



    catListInt = []
    for cat in catList:
        catListInt.append(int(cat[0]))
    print(catListInt)

    typeListInt = []
    for typ in typeList:
        typeListInt.append(int(typ[0]))
    print(typeListInt)

    sdate_label = Label(top_frame, text = 'Start Date')
    sdate_entry = Entry(top_frame,)

    edate_label = Label(top_frame, text='End Date')
    edate_entry = Entry(top_frame, )

    rtype_label = Label(top_frame, text = 'Vehicle Type')
    type_dropdown = StringVar(root)
    typepopupMenu = OptionMenu(top_frame, type_dropdown, *typeListInt)

    category_label = Label(top_frame, text='Vehicle Category')
    category_dropdown = StringVar(root)
    category_popupMenu = OptionMenu(top_frame, category_dropdown, *catListInt)

    order_date_label = Label(top_frame, text='Order Date')
    order_date_entry = Entry(top_frame, )

    cust_id_label = Label(top_frame, text= 'Customer ID')
    cust_id_entry = Entry(top_frame, )


    cust_id_label.grid(row=0, column=0)
    cust_id_entry.grid(row=0, column=1)

    sdate_label.grid(row=1,column=0)
    sdate_entry.grid(row=1,column=1)
    
    edate_label.grid(row=2,column=0)
    edate_entry.grid(row=2,column=1)
    
    rtype_label.grid(row=3,column=0)
    typepopupMenu.grid(row = 3, column =1)
    
    category_label.grid(row=4,column=0)
    category_popupMenu.grid(row = 4, column =1)
    
    order_date_label.grid(row = 5, column=0)
    order_date_entry.grid(row = 5, column=1)

    top_frame.grid(row=0)
    bottom_frame.grid(row=1)

    
    def bookReservation():
        iq = sqlite3.connect('car-rental.db')
        iq_cur = iq.cursor()

        startDate = sdate_entry.get()
        endDate = edate_entry.get()

        print(type_dropdown.get(), category_dropdown.get(),startDate, endDate, startDate, endDate)
        iq_cur.execute('''SELECT DISTINCT V.VehicleID, Description, Year FROM VEHICLE AS V 
                WHERE V.Type=? AND V.Category=? AND V.VehicleID NOT IN (SELECT R.VehicleID 
                FROM RENTAL AS R WHERE (R.StartDate Between ? AND ?) OR (R.ReturnDate Between ? AND ?))
                         ''', (type_dropdown.get(), category_dropdown.get(), startDate, endDate, startDate, endDate))

        startDateRaw = startDate.split("-")
        endDateRaw = endDate.split("-")
        dateDiff = (date(int(endDateRaw[0]), int(endDateRaw[1]), int(endDateRaw[2])) - date(int(startDateRaw[0]), int(startDateRaw[1]), int(startDateRaw[2]))).days
        records = iq_cur.fetchall()
        print(records)
        iq.commit()
        iq.close()


        quantity_label = Label(top_frame, text='Quantity')
        if dateDiff % 7 == 0:
            dateDiff/=7
            quantity_entry = Label(top_frame, text = str(int(dateDiff)) + 'weeks')
            rentalType = 7
        else:
            quantity_entry = Label(top_frame, text = str(int(dateDiff)) + 'days')
            rentalType = 1

        rental_type_label = Label(top_frame, text= 'Rental type')
        rental_type_entry = Label(top_frame, text= str(rentalType))

        rental_type_label.grid(row=10,column=0)
        rental_type_entry.grid(row=10, column=1)

        #TODO: change the positioning
        quantity_label.grid(row=11, column=0)
        quantity_entry.grid(row=11, column=1)
    
        storeVehicleDetails = StringVar()
        # vehicleName = tuple(map(tuple, records[:,1]))
        ttk.Label(top_frame, text= "Select the vehicles").grid(column=0, row=12)
        vehicleComboBox = ttk.Combobox(top_frame, width=15, text=storeVehicleDetails)
        vehicleComboBox['values'] = [records[i][1] for i in range(0, len(records))]
        # vehicleComboBox['values'] = vehicleName; 
        vehicleComboBox.grid(column=1, row=12)
        
        def addReservation():
            queryPayment = sqlite3.connect('car-rental.db')
            paymentCur = queryPayment.cursor()
            if rentalType == 7:
                paymentCur.execute('''SELECT Weekly FROM RATE WHERE Type = ? AND Category = ?''', (
                type_dropdown.get(), category_dropdown.get(),))
            elif rentalType == 1:
                paymentCur.execute('''SELECT Daily FROM RATE WHERE Type = ? AND Category = ?''', (
                type_dropdown.get(), category_dropdown.get(),))
            else:
                print("ERROR")

            print(type_dropdown.get(), category_dropdown.get())


            rates = paymentCur.fetchall()
            print(rates[0][0])
            Label(top_frame, text="total amount: ").grid(row=14, column=0)
            amountToPay = (dateDiff*rates[0][0])
            Label(top_frame, text=str(amountToPay)).grid(row=14, column=1)
            queryPayment.commit()
            queryPayment.close()

            c_v1=BooleanVar()
            c1 = Checkbutton(top_frame,text='Pay Now',variable=c_v1,
	        onvalue=1,offvalue=0)
            c1.grid(row=15,column=1) 

            def finalAddReservation():
                add_to_rental = sqlite3.connect('car-rental.db')
                add_to_rental_curr = add_to_rental.cursor()
                pDate = 'NULL'
                returnStatus = 0
                if c_v1.get() == True:
                    pDate = order_date_entry.get()

                else: 
                    pDate = 'NULL'


                add_to_rental_curr.execute("INSERT INTO RENTAL VALUES(:custID, :vID, :s_d, :or_date, :rental_type, :qty, :ret_date, :tot_amt, :payment_date, :returned)",
                {
                    'custID': cust_id_entry.get(),
                    'vID': records[vehicleComboBox.current()][0],
                    's_d' : sdate_entry.get(),
                    'or_date': order_date_entry.get(),
                    'rental_type': rentalType,
                    'qty': dateDiff,
                    'ret_date': edate_entry.get(),
                    'tot_amt': amountToPay,
                    'payment_date': pDate,
                    'returned': returnStatus
                }
                )
                add_to_rental.commit()
                add_to_rental.close()

                getCustomerName = sqlite3.connect('car-rental.db')
                getCustCur = getCustomerName.cursor()
                getCustCur.execute('''SELECT Name FROM CUSTOMER WHERE CustID = ?''', (int(cust_id_entry.get()), ))
                nameofCust = getCustCur.fetchall()
                getCustomerName.commit()
                getCustomerName.close()
                
                printThanks = Label(bottom_frame, text = 'Thank you ' + str(nameofCust[0][0]) + ' for making the reservation\nYou may now close the window.')
                printThanks.grid(row = 1)
                # print(c_v1.get())

            addToReservation = Button(top_frame, text='Confirm Reservation', command=finalAddReservation)
            addToReservation.grid(row=16, column=1)

        getToPayment = Button(top_frame, text='Payment: ', command=addReservation)
        getToPayment.grid(row = 13, column=1)  
                           

    searchReservationButton = Button(top_frame, text = 'Show results', command=bookReservation)
    searchReservationButton.grid(row=9, column=1, padx=10)

    # def insertReservation():



def lw4():
    w = Toplevel(root)
    w.title('Return Rental')
    w.geometry('600x600')
    top_frame = Frame(w)
    bottom_frame =Frame(w) # for sql query output

    #label and entry boxes below this

    

    edate_label = Label(top_frame, text='Return Date')
    edate_entry = Entry(top_frame )
    cname_label = Label(top_frame, text = 'Customer Name')
    cname_entry = Entry(top_frame)
    vin_label = Label(top_frame, text = 'VIN')
    vin_entry = Entry(top_frame)


    edate_label.grid(row=0,column=0)
    edate_entry.grid(row=0,column=1)
    cname_label.grid(row=1,column=0)
    cname_entry.grid(row=1,column=1)
    vin_label.grid(row=2,column=0)
    vin_entry.grid(row=2,column=1)

    def getRental():
        getRental_conn = sqlite3.connect('car-rental.db')
        getRental_curr = getRental_conn.cursor()
        #passing in user defined input
        getRental_curr.execute('''SELECT R.TotalAmount FROM RENTAL AS R, CUSTOMER AS C WHERE
        R.ReturnDate = ? AND R.CustID = C.CustID AND C.Name = ? AND R.VehicleID = ?''',(edate_entry.get(),cname_entry.get(),vin_entry.get(),) 
        )
        records = getRental_curr.fetchall()
        getRental_conn.commit()
        getRental_conn.close()

        def returnRental():
            returnRental_conn = sqlite3.connect('car-rental.db')
            returnRental_curr = returnRental_conn.cursor()
            returnRental_curr.execute('''SELECT R.Returned FROM RENTAL AS R, CUSTOMER AS C WHERE
            R.ReturnDate = ? AND R.CustID = C.CustID AND C.Name = ? AND R.VehicleID = ?''',(edate_entry.get(),cname_entry.get(),vin_entry.get(),)) 


            status = returnRental_curr.fetchall()
            status_text=""            

            returnRental_conn.commit()
            returnRental_conn.close()

            if int(status[0][0]) == 1:
                status_text = "This car has already been returned. Thank You"
                status_label =Label(top_frame,text=status_text)
                status_label.grid(row=6,column=0)
                
            elif int(status[0][0]) == 0:
                RRental_conn = sqlite3.connect('car-rental.db')
                RRental_curr = RRental_conn.cursor()
                RRental_curr.execute('''SELECT C.Name, C.CustID FROM CUSTOMER AS C WHERE C.Name = ?''',(cname_entry.get(),))


                result = RRental_curr.fetchall()
                print(result)
                RRental_conn.commit()
                RRental_conn.close()
                # print("hello")

                Rental_conn = sqlite3.connect('car-rental.db')
                Rental_cur = Rental_conn.cursor()                
                Rental_cur.execute('''UPDATE Rental SET Returned = 1, 
                PaymentDate = CASE WHEN PaymentDate = 'NULL' THEN ReturnDate ELSE PaymentDate END 
                WHERE VehicleID = ? AND CustID = ? AND ReturnDate = ?''',(str(vin_entry.get()),int(result[0][1]),str(edate_entry.get()))) 

                printThanks = Label(bottom_frame, text = 'Thank you ' + cname_entry.get() + '. Your car was returned.\nYou may now close the window.')
                printThanks.grid(row = 1)                

                Rental_conn.commit()
                Rental_conn.close()

        
        #make a label to display the query
        total_label = Label (top_frame,text='Total Amount Due:').grid(row = 4, column=0)
        tamt_label = Label(top_frame, text = records)
        tamt_label.grid(row = 4, column=1)

  
        getRentalDetails_btn = Button(top_frame, text = 'Make Payment & Return Rental', command=returnRental)
        getRentalDetails_btn.grid(row = 5, column=0,columnspan=2, pady=5, ipadx=100)
            

    getRentalDetails_btn = Button(top_frame, text = 'Get Total Amount', command=getRental)
    getRentalDetails_btn.grid(row = 3, column=0, columnspan=2, pady=10, ipadx=100)

    top_frame.grid(row=0)
    bottom_frame.grid(row=1)

def lw5():
    w = Toplevel(root)
    w.title('Get Customer Details')
    w.geometry('600x600')
    top_frame = Frame(w)
    bottom_frame =Frame(w) # for sql query output

    #label and entry boxes below this
    cname_label = Label(top_frame, text = 'Customer name')
    cname_entry = Entry(top_frame)
    cid_label = Label(top_frame, text = 'Customer ID')
    cid_entry = Entry(top_frame)

   
    cid_label.grid(row = 0, column=0)
    cid_entry.grid(row = 0, column=1)
    cname_label.grid(row = 1, column=0)
    cname_entry.grid(row = 1, column=1)
    res =[]

    def searchCustomer():
        search_conn = sqlite3.connect('car-rental.db')
        search_cur = search_conn.cursor()

        if(cid_entry.get()!=''):
            search_cur.execute('''
            SELECT CustomerName,CustomerID,'$' || printf("%.2f", SUM(RentalBalance)) AS RentalBalance FROM vRentalInfo WHERE 
            CustomerID= ? GROUP BY CustomerID
            
            UNION 

            SELECT Name,CustID, '$0.00' AS RentalBalance FROM CUSTOMER WHERE CustID=  ? AND CustID NOT IN (SELECT DISTINCT CustomerID FROM vRentalInfo )
            ''',(cid_entry.get(),cid_entry.get()))

        elif cname_entry.get() != '':

            search_cur.execute('''
            SELECT CustomerName,CustomerID,'$' || printf("%.2f", SUM(RentalBalance)) AS RentalBalance FROM vRentalInfo WHERE 
            CustomerName LIKE ? GROUP BY CustomerID
            
            UNION 

            SELECT Name,CustID, '$0.00' AS RentalBalance FROM CUSTOMER WHERE Name LIKE ? AND CustID NOT IN (SELECT DISTINCT CustomerID FROM vRentalInfo )
            ''',(str('%'+cname_entry.get()+'%'),str('%'+cname_entry.get()+'%')))


        else:
            search_cur.execute('''
            SELECT CustomerName,CustomerID, '$'|| printf("%.2f", SUM(RentalBalance)) AS RentalBalance FROM vRentalInfo 
            
            GROUP BY CustomerID
            UNION 

            SELECT Name,CustID, '$0.00' AS RentalBalance FROM CUSTOMER WHERE CustID NOT IN (SELECT DISTINCT CustomerID FROM vRentalInfo )
            ''')

        res = search_cur.fetchall()
        print_text = ''
        lengthOfRecords = len(res)
        for r in res:
            print_text += str((str(r[0])) + " | " + str(r[1]) + " | " + str(r[2]) + "\n")
            
        result_label = Label(bottom_frame,text= "Customer ID | Customer Name | Remaining Balance\n\n"+print_text)
        countLabel = Label(bottom_frame, text='Total Count of Records Returned: ' + str(lengthOfRecords))
        result_label.grid(row=1)
        countLabel.grid(row=2)
        print(res)
        

        search_conn.commit()
        search_conn.close()
    

    search_btn = Button(top_frame, text = 'Search', command=searchCustomer)
    search_btn.grid(row = 6, column=0, columnspan=2, pady=10, ipadx=100)


    top_frame.grid(row=0)
    bottom_frame.grid(row=1)

def lw6():
    w = Toplevel(root)
    w.title('Get Vehicle Details')
    w.geometry('600x600')
    top_frame = Frame(w)
    bottom_frame =Frame(w) # for sql query output

    #label and entry boxes below this

    vin_label = Label(top_frame, text = 'VIN')
    vin_entry = Entry(top_frame)
    vdesc_label = Label(top_frame, text = 'Veicle Description')
    vdesc_entry = Entry(top_frame)

   
    vin_label.grid(row = 0, column=0)
    vin_entry.grid(row = 0, column=1)
    vdesc_label.grid(row = 1, column=0)
    vdesc_entry.grid(row = 1, column=1)

    def car_search():

        search_conn = sqlite3.connect('car-rental.db')
        search_curr = search_conn.cursor()


        if vin_entry.get() != '':
            search_curr.execute(
                '''SELECT VIN, Vehicle, '$' || printf("%.2f", (ROUND(CAST(SUM(OrderAmount) AS float)/SUM(TotalDays), 2))) as'Avg Daily Price' FROM vRentalInfo WHERE VIN = ?
                GROUP BY VIN
                UNION
                SELECT VehicleID,Description, 'Not Applicable 'as 'Avg Daily Price'
                FROM VEHICLE 
                WHERE VehicleID = ? AND VEHICLE.VehicleID NOT IN (SELECT DISTINCT VIN FROM vRentalInfo)
                
                ''', (vin_entry.get(),vin_entry.get(),))
        
        elif vdesc_entry.get() != '':
            search_curr.execute(
                '''SELECT VIN, Vehicle, '$' || printf("%.2f", (ROUND(CAST(SUM(OrderAmount) AS float)/SUM(TotalDays), 2))) as 'Avg Daily Price' 
                    FROM vRentalInfo 
                    WHERE Vehicle LIKE ? GROUP BY VIN 
                    UNION
                    SELECT  VehicleID,Description, 'Not Applicable' as 'Avg Daily Price' 
                    FROM VEHICLE 
                    WHERE VEHICLE.Description LIKE ? AND VehicleID NOT IN (SELECT DISTINCT VIN FROM vRentalInfo)
                

                ''', (str('%'+vdesc_entry.get()+'%'),str('%'+vdesc_entry.get()+'%'),))
        else:
            search_curr.execute(
                '''SELECT VIN, Vehicle, '$' || printf("%.2f", (ROUND(CAST(SUM(OrderAmount) AS float)/SUM(TotalDays), 2))) AS Avg_Daily_Price FROM vRentalInfo GROUP BY VIN 
                UNION
                    SELECT  VehicleID,Description, 'Not Applicable' as Avg_Daily_Price 
                    FROM VEHICLE 
                    WHERE VehicleID NOT IN (SELECT DISTINCT VIN FROM vRentalInfo)

                    ORDER BY Avg_Daily_Price ASC
                ''')

        res = search_curr.fetchall()
        print_text = ''

        lengthOfRecords = len(res)
        for r in res:
            print_text += str((str(r[0])) + " | " + str(r[1]) + " | " + str(r[2]) + "\n")


        result_label = Label(bottom_frame,text= "VIN | Vehicle | Average Daily price\n\n"+print_text)
        countLabel = Label(bottom_frame, text='Total Count of Records Returned: ' + str(lengthOfRecords))

        result_label.grid(row=1)
        countLabel.grid(row = 2)
        print(res)
        

        search_conn.commit()
        search_conn.close()

    

    top_frame.grid(row=0)
    bottom_frame.grid(row=1)

    search_btn = Button(top_frame, text = 'Search', command=lambda:car_search())
    search_btn.grid(row = 6, column=0, columnspan=2, pady=10, ipadx=100)


# buttons are  numbered in order of tasks 1 to 5a) 6 is 5b)
btn1 = Button(root,  text= 'Add new customer', command=lw1,width= 20,height=7,padx=5,pady=5).grid (row = 0, column=0)
btn2 = Button(root,  text= 'Add new vehicle', command=lw2,width= 20,height=7,padx=5,pady=5).grid (row = 0, column=1)
btn3 = Button(root,  text= 'Add new reservation', command=lw3,width= 20,height=7,padx=5,pady=5).grid (row = 1, column=0)
btn4 = Button(root,  text= 'Return Rental', command=lw4,width= 20,height=7,padx=5,pady=5).grid (row = 1, column=1)
btn5 = Button(root,  text= 'Get Customer Details', command=lw5,width= 20,height=7,padx=5,pady=5).grid (row = 2, column=0)
btn6 = Button(root,  text= 'Get Vehicle Details', command=lw6,width= 20,height=7,padx=5,pady=5).grid (row = 2, column=1)



# run the program
root.mainloop()