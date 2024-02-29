
import unittest
import bank

class TestBank(unittest.TestCase):
    def setUp(self):
        bank.bank_accounts_money = [100, 0, 0, 0]

    def test_check_not_negative_or_zero(self):
        #test case1: possitive number and check_not_negative_or_zero function should return true
        self.assertTrue(bank.check_not_negative_or_zero(100))
        # test case2:  zero and check_not_negative_or_zero function should return false
        self.assertFalse(bank.check_not_negative_or_zero(0))
        # test case1: negative number and check_not_negative_or_zero function  should return false
        self.assertFalse(bank.check_not_negative_or_zero(-5))



    def test_convert_to_number(self):
        #test case1 : valid numeric string input that will be integer after converting it
        self.assertEqual(bank.convert_to_number("123"), 123)
        # test case2 : valid integer input
        self.assertEqual(bank.convert_to_number(456), 456)
        # test case3: non valid input (letters string) for int() function
        self.assertIsNone(bank.convert_to_number("abc"))
        # test case4: non valid input (None) for int() function
        self.assertIsNone(bank.convert_to_number(None))

    def test_deposit(self):
        #test case 1: valid deposit with valid amount of money and will work successfully
        initial_amount= bank.bank_accounts_money[0]
        deposit_amount = 50
        bank.deposit(deposit_amount)
        expected_balance =  initial_amount + deposit_amount - 1  # 1$ fee
        self.assertEqual(bank.bank_accounts_money[0], expected_balance)  #the money in the account will be less with 50(deposit)+1(fee) $
        #test case2: none integer input  of amount the deposit function will not make the operation and the amount of money will stay with no change
        initial_amount1 = bank.bank_accounts_money[0]
        deposit_amount = "ab"
        bank.deposit(deposit_amount)
        expected_balance = initial_amount1  # expected to no change happen since the deposit value is not integer
        self.assertEqual(bank.bank_accounts_money[0], expected_balance)

        #test case3: tryig to deposit negative amount of money will be unsuccessfully
        initial_amount2 = bank.bank_accounts_money[0]
        deposit_amount = -10
        bank.deposit(deposit_amount)
        expected_balance = initial_amount2  # expected to no change happen since the deposit value is not integer
        self.assertEqual(bank.bank_accounts_money[0], expected_balance)
    def test_withdraw(self):
        #test case 1: withdraw 30 from the account and the operation should be done successfully
        initial_balance = bank.bank_accounts_money[0]
        withdraw_amount = 30
        bank.withdraw(withdraw_amount)
        expected_balance = initial_balance - withdraw_amount - 1  # 1$ fee
        self.assertEqual(bank.bank_accounts_money[0], expected_balance)
        # test case 2: where we  trying to withdraw with amount that is larger than the amount in the account for now there is 69 in the account
        withdraw_amount = 100
        bank.withdraw(withdraw_amount)
        expected_balance = 69   # the amount should still the same case the withdraw must not be done
        self.assertEqual(bank.bank_accounts_money[0], expected_balance)
        #test case 3: we trying to withdraw with negative number and the operation will not be done
        withdraw_amount = -10  # trying to withdraw with negative number
        bank.withdraw(withdraw_amount)
        expected_balance = 69  # the amount should still the same case the withdraw must not be done
        self.assertEqual(bank.bank_accounts_money[0], expected_balance)

    def test_transfer(self):
        #test case 1: normal transfer with valid amount and to valid account
        initial_balance = bank.bank_accounts_money[0]
        transfer_amount = 20
        to_account = 1
        expected_to_balance = bank.bank_accounts_money[to_account] + transfer_amount
        bank.transfer(to_account, transfer_amount)
        expected_from_balance = initial_balance - transfer_amount - 1  # 1$ fee
        self.assertEqual(bank.bank_accounts_money[0], expected_from_balance)
        self.assertEqual(bank.bank_accounts_money[to_account], expected_to_balance)

        #test case 2: trying to transfer money to self-account this test will fall
        initial_balance2 = bank.bank_accounts_money[0]
        transfer_amount = 20
        to_account = 0
        bank.transfer(to_account, transfer_amount)
        self.assertEqual(bank.bank_accounts_money[0], initial_balance2) #the function should refuse to transfer
        # the monet and the money in the account should stay with no change but this test case will fail the function transfer allow self transfer and so the fee will be tacken from the main account


        #test case 3 : trying to transfer money to non-exist account
        initial_balance3 = bank.bank_accounts_money[0]
        transfer_amount = 20
        to_account = 10
        bank.transfer(to_account, transfer_amount)
        self.assertEqual(bank.bank_accounts_money[0], initial_balance3) # the transfer will not be done sucssefully since the account is not exist so the money amount will remain the same

        #test case 4: trying to transfer negative amount of money
        initial_balance4 = bank.bank_accounts_money[0]
        transfer_amount = -20
        to_account = 2
        bank.transfer(to_account, transfer_amount)
        self.assertEqual(bank.bank_accounts_money[to_account], 0) # the money will not be transfered so the amount will stary the same = 0
        self.assertEqual(bank.bank_accounts_money[0], initial_balance4)# the money will not be transfered so the amount will stary the same

    def test_withdraw_check_balance(self):
        initial_balance = bank.bank_accounts_money[0]
        enough_balance = initial_balance - 1  # 1$ fee
        not_enough_balance = initial_balance + 5

        self.assertTrue(bank.withdraw_check_balance(enough_balance))# the withdraw_check_balance function should return true since enough_balance <
        self.assertFalse(bank.withdraw_check_balance(not_enough_balance)) # the withdraw_check_balance should return false since there is no 101 in the account to withdraw
if __name__ == '__main__':
    unittest.main()
