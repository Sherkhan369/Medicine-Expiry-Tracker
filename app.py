from datetime import datetime

class Medicine:
    def __init__(self, name, expiry_date):
        self.name = name
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")

    def days_until_expiry(self):
        return (self.expiry_date - datetime.today()).days

    def is_expired(self):
        return self.days_until_expiry() < 0

    def is_near_expiry(self):
        return 0 <= self.days_until_expiry() <= 7

class MdcnTracker:
    def __init__(self):
        self.medicines = []

    def add_medicine(self, name, expiry_date):
        med = Medicine(name, expiry_date)
        self.medicines.append(med)

    def check_expired(self):
        return [med for med in self.medicines if med.is_expired()]

    def check_near_expiry(self):
        return [med for med in self.medicines if med.is_near_expiry()]

    def display_summary(self):
        for med in self.medicines:
            status = "Expired" if med.is_expired() else "Near Expiry" if med.is_near_expiry() else "Safe"
            print(f"{med.name}: {status} (Expires in {med.days_until_expiry()} days)")

if __name__ == "__main__":
    tracker = MdcnTracker()
    tracker.add_medicine("Paracetamol", "2025-05-15")
    tracker.add_medicine("Cough Syrup", "2025-05-10")
    tracker.add_medicine("Antibiotic", "2025-04-30")
    tracker.add_medicine("Vitamins", "2025-06-01")
    tracker.add_medicine("Pain Reliever", "2025-05-20")
    tracker.add_medicine("Cold Medicine", "2025-05-25")

    print("\n--- Medicine Summary ---")
    tracker.display_summary()

    print("\n--- Expired Medicines ---")
    for med in tracker.check_expired():
        print(med.name)

    print("\n--- Near Expiry Medicines ---")
    for med in tracker.check_near_expiry():
        print(med.name)
