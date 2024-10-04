from get_data import Data

class recDonor:
    def __init__(self, donor: str) -> None:
        self.donor = donor 
        self.donations = []

    def add_donation(self, party: str, value: float) -> None:
        donation_found = False
        for donation in self.donations:
           if donation.party == party:
               donation.value += value
               donation_found = True
               break 
        if not donation_found:
            self.donations.append(recDonation(party, value))

    def find_party_donation(self, party: str):
        for donation in self.donations:
            if donation.party == party:
                return donation
        return None

class recDonation:
    def __init__(self, party: str, value: float) -> None:
        self.party = party
        self.value = value

class Program:
    def parse_donations(self, donations: list) -> list:
        donors = []
        for donation in donations:
            donor_found = False
            for donor in donors:
                if donation.DonorName == donor.donor:
                    donor_found = True
                    donor.add_donation(donation.EntityName, donation.Value)
                    break
            if not donor_found:
                x = recDonor(donation.DonorName)
                x.add_donation(donation.EntityName, donation.Value)
                donors.append(x)

        return donors

    def biggest_donor_per_party(self, party, donors, exclude = []):
        max = ""
        max_value = 0
        for donor in donors:
            donation = donor.find_party_donation(party)
            if donation != None and not donor.donor in exclude:
                    if max == "" or donation.value > max_value:
                        max = donor
                        max_value = donation.value
        return max

    def donors_with_donations_over_val(self, donors, val) -> list:
        donors_over_val = []
        for donor in donors:
            for donation in donor.donations:
                if donation.value > val:
                    donors_over_val.append(donor)
        return donors_over_val

    def average_donation_per_party(self, party, donors) -> int:
        value = 0
        count = 0
        for donor in donors:
            donation = donor.find_party_donation(party)
            if donation != None:
                value += donation.value
                count += 1
        return int(value // count)

    def total_donations_per_party(self, party, donors) -> int:
        value = 0
        for donor in donors:
            donation = donor.find_party_donation(party)
            if donation != None:
                value += donation.value
        return int(value)

    def __init__(self) -> None:
        data = Data()
        donations = data.get()
        donors = self.parse_donations(donations)

if __name__ == "__main__":
    p = Program()
