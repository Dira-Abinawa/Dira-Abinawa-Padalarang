from pymongo import MongoClient

client = MongoClient("mongodb+srv://RDGalihRakasiwi:fkSeIRIz0aQ3NfVf@cluster0.ni5ltny.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('dira_abinawa-dkr')
dkr_connection = db.get_collection('dewan_kerja_ranting')