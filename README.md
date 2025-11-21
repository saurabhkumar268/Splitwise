# Splitwise
Term End project on Python Essentials through VITyarthi platform on topic Splitwise Management.
# 💡 Core Structure & Data
 * friends Dictionary (The Ledger): Stores each friend's Net Balance (float).
   * Positive Balance: Friend is owed money.
   * Negative Balance: Friend owes money.
 * history List (The Log): Chronological record of all transactions.
# 💰 Key Features & Logic
1. Expense Calculation (Core Logic)
Updates balances in two steps when a payment is made:
 * Total amount is added to the Payer's balance (full credit).
 * The Equal Split Amount (Total / Group Size) is subtracted from every friend's balance (including the Payer's).
   * Effect: Payer gets credit for payment minus their own share; others are charged only their share.
 * Transaction is recorded in history.
2. Balances (Settlement View)
Shows who needs to pay whom:
 * Positive: Friend gets back.
 * Negative (Absolute): Friend needs to pay.
 * Zero: Settled.
3. View History
Displays the list of all recorded expenses.
4. Add New Friend
Adds a new member with a 0 balance.
> Note: New members only share future expenses (not past ones).
 
# ⚙ General Structure
 * Starts with initial group setup.
 * Runs in an infinite loop driven by a main menu (5 options).
 * Includes basic error handling (valid payer/amount).
 * Exits only via Option 5.

