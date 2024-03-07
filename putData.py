import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("look-inside-view-firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

fileName = "public/list.json"
jsonData = json.load(open(fileName, 'r', encoding="utf-8_sig"))

db.collection('list').document("list").set(jsonData)