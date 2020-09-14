from datetime import datetime
class Log:
    def __init__(self):
        pass

    def saveConversations(self, sessionID, cust_reason,intent,db,cust_email,cust_name,cust_phone):

        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")

        #db = dbConn['User_details']  # connecting to the database called crawlerD
        mydict = {"sessionID":sessionID,"Date": str(self.date) + "/" + str(self.current_time),"User Name": cust_name,"User Email": cust_email,"User Phone Number": cust_phone,"User Intent" : intent ,"Problem": cust_reason}

        #table = db[sessionID]
        records = db.chat_record
        records.insert_one(mydict)

        #table.insert_one(mydict)

