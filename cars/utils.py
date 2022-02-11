import uuid

def expense_transaction_id():
    uniqueid = str(uuid.uuid4()).replace('-','')
    transid = "EX"+str(uniqueid)
    return transid

def revenue_transaction_id():
    uniqueid = str(uuid.uuid4()).replace('-','')
    transid = "EX"+str(uniqueid)
    return transid