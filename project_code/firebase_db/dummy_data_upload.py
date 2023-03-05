import firebase_admin
from firebase_admin import credentials, db
from models import signal_value
cred = credentials.Certificate("project_code/firebase/firebase_sdk.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"https://signals-b2e76-default-rtdb.firebaseio.com"
})

database=db.reference('/Signal')

signals={}
for i in range(10):
    status = (i%3)
    if(status==0): status=signal_value.red
    elif(status==1): status=signal_value.yellow
    elif(status==2): status=signal_value.green
    signal_details = {f"Signal_{i}":{"Status":status}}
    signals.update(signal_details)


k=database.set(signals)
print("set operations return: ",k)
def get_signal_by_id(id:int):
    #db reference must be set to path of required id before performing get operation
    ref=db.reference(f"/Signal/Signal_{id}")
    return ref.get()

def get_signal_status(id:int):
    ref = db.reference(f"Signal/Signal{id}/Status")
    return ref.get()



