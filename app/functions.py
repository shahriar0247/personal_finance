import sqlite3

def get_all_balance():
    all_accounts = get_balance_with_accounts()

    all_balance = 0
    all_bank_balance = 0
    all_credit_balance = 0
    all_cash_balance = 0

    for a in all_accounts:

        all_balance = int(a[3]) + all_balance

        if a[2] == "Bank":
            all_bank_balance = int(a[3]) + all_bank_balance
        
        if a[2] == "Credit":
            all_credit_balance = int(a[3]) + all_credit_balance

        if a[2] == "Cash":
            all_cash_balance = int(a[3]) + all_cash_balance

    return all_balance, all_bank_balance, all_credit_balance, all_cash_balance
           
def get_balance_with_accounts():
    with sqlite3.connect( "database.db" ) as conn:
        all_accounts = conn.cursor().execute("select * from accounts").fetchall()

        return all_accounts
 
def add_to_account(amount_to_add, account):
    all_accounts = get_balance_with_accounts()

    for a in all_accounts:
        if a[0] == account:
            amount = int(a[3])
            amount = amount + int(amount_to_add)
            with sqlite3.connect("database.db") as conn:
                conn.execute("DELETE FROM accounts WHERE name = \"" + a[0] + "\"")
                conn.cursor().execute("insert into accounts values ( ?,?,?,?,? )",(a[0],  a[1] , a[2] , amount, a[4]))
                conn.commit()

