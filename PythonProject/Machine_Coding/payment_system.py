import base64
import json
from datetime import datetime, timezone

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, card_number, balance):
        if card_number in self.accounts:
            return f"Account with card number {card_number} already exists"
        self.accounts[card_number] = balance

    def close_account(self, card_number):
        if card_number not in self.accounts:
            return f"Account with card number {card_number} does not exist"
        remaining_bal = self.accounts[card_number]
        print(f"Account closed. Remaining balance: {remaining_bal}")
        del self.accounts[card_number]

class Payments(Bank):
    def __init__(self, card_number, exp_date, amount, txn_type, to_card_number):
        super().__init__()
        self.card_number = card_number
        self.exp_date = exp_date
        self.amount = amount
        self.txn_type = txn_type
        self.to_card_number = to_card_number
        self.ref_id = self._create_ref_id(card_number, exp_date, amount, txn_type, to_card_number)  # to_card_number will be set during sale or refund

    @staticmethod
    def _create_ref_id(from_card_number, exp_date, amount, txn_type, to_card_number):
        payload = {
            "from_card_number": from_card_number,
            "exp_date": exp_date,
            "amount": amount,
            "txn_type": txn_type,
            "to_card_number": to_card_number,
            "gmt_time_hhmmss": datetime.now(timezone.utc).strftime("%H%M%S")
        }
        encoded_payload = json.dumps(payload, separators=(",", ":"))
        return base64.urlsafe_b64encode(encoded_payload.encode("utf-8")).decode("utf-8")

    @staticmethod
    def _decode_ref_id(ref_id):
        try:
            decoded_payload = base64.urlsafe_b64decode(ref_id.encode("utf-8")).decode("utf-8")
            return json.loads(decoded_payload)
        except Exception as exc:
            return f"Invalid ref id: {exc}"

    def sale(self, sale_amount):
        if self.card_number not in self.accounts:
            return f"Your account:{self.card_number} does not exist"
        if self.accounts[self.card_number] < sale_amount:
            return f"Insufficient balance in your account: {self.card_number}"
        if self.to_card_number not in self.accounts:
            return f"Recipient account: {self.to_card_number} does not exist"
        self.accounts[self.card_number] -= sale_amount
        self.accounts[self.to_card_number] += sale_amount
        return f"Sale successful. Ref ID: {self.ref_id}"

    def refund(self, refund_amount):
        if self.card_number not in self.accounts:
            return f"Your account:{self.card_number} does not exist"
        if self.to_card_number not in self.accounts:
            return f"Recipient account: {self.to_card_number} does not exist"
        if self.accounts[self.to_card_number] < refund_amount:
            return f"Insufficient balance in your account: {self.to_card_number}"
        self.accounts[self.to_card_number] -= refund_amount
        self.accounts[self.card_number] += refund_amount
        return f"Refund successful. Ref ID: {self.ref_id}"
    
    def void(self, ref_id):
        decoded_payload = self._decode_ref_id(ref_id)
        if isinstance(decoded_payload, str):
            return decoded_payload
        from_card_number = decoded_payload["from_card_number"]
        to_card_number = decoded_payload["to_card_number"]
        amount = decoded_payload["amount"]
        payment_type = decoded_payload["txn_type"]
        if from_card_number not in self.accounts:
            return f"Account:{from_card_number} does not exist"
        if to_card_number not in self.accounts:
            return f"Account:{to_card_number} does not exist"
        if payment_type == "sale":
            if self.accounts[to_card_number] < amount:
                return f"Insufficient balance in account: {to_card_number} to void the sale"
            self.accounts[to_card_number] -= amount
            self.accounts[from_card_number] += amount
        elif payment_type == "refund":
            if self.accounts[from_card_number] < amount:
                return f"Insufficient balance in account: {from_card_number} to void the refund"
            self.accounts[from_card_number] -= amount
            self.accounts[to_card_number] += amount
        return f"Void successful. Ref ID: {ref_id}"


if __name__ == "__main__":
    # Testing data and simple usage examples
    bank = Bank()

    # Create two test accounts
    bank.create_account("1111222233334444", 1000)
    bank.create_account("5555666677778888", 500)

    # Payments instance for the first account
    p = Payments(card_number="1111222233334444", exp_date="12/25", amount=0, txn_type="sale", to_card_number="5555666677778888")
    p.accounts = bank.accounts

    print("Initial accounts:", p.accounts)

    # Perform a sale from 1111... -> 5555... for 150
    sale_result = p.sale(150)
    print("Sale result:", sale_result)
    print("Accounts after sale:", p.accounts)

    # # Perform a refund: create a Payments instance representing recipient (1111...)
    p_refund = Payments(card_number="1111222233334444", exp_date="12/25", amount=0, txn_type="refund", to_card_number="5555666677778888")
    p_refund.accounts = p.accounts
    refund_result = p_refund.refund(50)
    print("Refund result:", refund_result)
    print("Accounts after refund:", p_refund.accounts)

    # Void using the ref_id from the original payment
    ref_id = p.ref_id
    print("Void result:", p.void(ref_id))

    # Decode an invalid ref id to demonstrate error handling
    print("Decode invalid ref id:", Payments._decode_ref_id("invalid_ref"))

    # Close test accounts
    bank.close_account("1111222233334444")
    bank.close_account("5555666677778888")
        

        