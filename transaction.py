from functions import csv_fields

class Transaction:
    def __init__(self, transID, post, effDate, transType, amt, check, ref, desc, cat, typ, bal, memo, ext):
        self.transID = transID
        self.post = post
        self.effDate = effDate
        self.transType = transType
        self.amt = round(float(amt), 2)
        self.check = check
        self.ref = ref
        self.desc = desc
        self.cat = cat
        self.type = typ
        self.bal = bal
        self.memo = memo
        self.ext = ext
    
    def __init__(self, reader):
        self.transID = reader[csv_fields['trans_id']]
        self.post = reader[csv_fields['post']]
        self.effDate = reader[csv_fields['effective']]
        self.transType = reader[csv_fields['trans_type']]
        self.amt = reader[csv_fields['amt']]
        self.check = reader[csv_fields['chk_num']]
        self.ref = reader[csv_fields['ref_num']]
        self.desc = reader[csv_fields['desc']]
        self.cat = reader[csv_fields['trans_cat']]
        self.type = reader[csv_fields['type']]
        self.bal = reader[csv_fields['balance']]
        self.memo = reader[csv_fields['memo']]
        self.ext = reader[csv_fields['ext_desc']]

    def getAmt(self):
        return self.amt

    def display(self):
        print('{0} {1} {2} {3} {4} {5} {6} {7}'.format(self.transID, self.post, self.effDate, self.transType, self.amt, self.ref, self.desc, self.cat))
        print('===================================================================================================')


    def set_desc(self, newDesc):
        self.desc = newDesc