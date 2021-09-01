import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("firestorekey.json")
firebase_admin.initialize_app(cred)

def data_base(collection):
    try:
        db = firestore.client()
        return db.collection(collection)
    except Exception as e:
        print(e)