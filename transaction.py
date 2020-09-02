import functions

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
        self.transID = reader[functions.csv_fields['trans_id']]
        self.post = reader[functions.csv_fields['post']]
        self.effDate = reader[functions.csv_fields['effective']]
        self.transType = reader[functions.csv_fields['trans_type']]
        self.amt = reader[functions.csv_fields['amt']]
        self.check = reader[functions.csv_fields['chk_num']]
        self.ref = reader[functions.csv_fields['ref_num']]
        self.desc = reader[functions.csv_fields['desc']]
        self.cat = reader[functions.csv_fields['trans_cat']]
        self.type = reader[functions.csv_fields['type']]
        self.bal = reader[functions.csv_fields['balance']]
        self.memo = reader[functions.csv_fields['memo']]
        self.ext = reader[functions.csv_fields['ext_desc']]

    def get_amt(self):
        return self.amt

    def display(self):
        print('{0} {1} {2} {3} {4} {5} {6} {7}'.format(self.transID, self.post, self.effDate, self.transType, self.amt, self.ref, self.desc, self.cat))
        print('===================================================================================================')


    def set_desc(self, newDesc):
        self.desc = newDesc