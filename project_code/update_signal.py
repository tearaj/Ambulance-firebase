import firebase_admin
from firebase_admin import credentials, db
from enum import Enum
from google.auth.exceptions import TransportError #to throw connection error
cred = credentials.Certificate("../project_code/firebase_db/firebase_sdk.json")

firebase_admin.initialize_app(cred,{
    "databaseURL":"https://signals-b2e76-default-rtdb.firebaseio.com"
})

db.reference("/Signal")


#used by the controller on the traffic lights to control the signal
def update_status_manually(id,signal_status):
    try:
        ref=db.reference(f"/Signal/Signal_{id}")

        stat={"Status":signal_status}
        ref.update(stat)
    except TransportError:
        print("Connection problem")
        return

def get_signal_status_by_id(id:int):
    db_ref=db.reference(f"/Signal/Signal_{id}/Status")
    return db_ref.get()


# def update_status_to_red(id):
#     try:
#         ref=db.reference(f"/Signal/Signal_{id}")
#         stat={"Status":signal_status.red}
#         m=ref.update(stat)
#         print("update returns ",m)
#     except TransportError:
#         print("Connection problem")
#         return

# def update_status_to_green(id):
#     try:
#         ref=db.reference(f"/Signal/Signal_{id}")
#         stat={"Status":signal_status.red}
#         m=ref.update(stat)
#         print("update returns ",m)
#     except TransportError:
#         print("Connection problem")
#         return

# def update_status(id):
#     try:
#         ref=db.reference(f"/Signal/Signal_{id}")
#         prev_status= ref.get()
#         stat={}
#         if(prev_status['Status'] == signal_status.red): stat = {"Status":signal_status.yellow}
#         elif(prev_status['Status'] == signal_status.yellow): stat =  {"Status":signal_status.green}
#         elif(prev_status['Status'] == signal_status.green): stat = {"Status":signal_status.red}
#         elif(prev_status['Status'] == None): 
#             print("id does not exist")
#             return
#         m=ref.update(stat)
#         print("update returns ",m)
#     except TransportError:
#         print("Connection problem")
#         return
