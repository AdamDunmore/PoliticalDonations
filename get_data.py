class recDonations:
    def __init__(self, ecRef, EntityName, EntityType, Value, AcceptedDate, AccountingUnitName, DonorName, AccountingUnitsAsCentralParty, IsSponsorship, DonorStatus, DoneeType, CompanyRegNumber, PostCode, DonationType, NatureOfDonation, PurposeOfVisit, DonationAction, ReceivedDate, ReportedDate, IsReportedPrePoll, ReportingPeriodName, IsBequest, IsAggregation, RegulatedEntityId, AccountingUnitId, DonorId, CampaigningName, RegisterName, IsIrishSource):
        self.ecRef = ecRef
        self.EntityName = EntityName
        self.EntityType = EntityType
        self.Value = Value
        self.AcceptedDate = AcceptedDate
        self.AccountingUnitName = AccountingUnitName
        self.DonorName = DonorName
        self.AccountingUnitsAsCentralParty = AccountingUnitsAsCentralParty
        self.IsSponsorship = IsSponsorship
        self.DonorStatus = DonorStatus
        self.DoneeType = DoneeType
        self.CompanyRegNumber = CompanyRegNumber
        self.PostCode = PostCode
        self.DonationType = DonationType
        self.NatureOfDonation = NatureOfDonation
        self.PurposeOfVisit = PurposeOfVisit
        self.DonationAction = DonationAction
        self.ReceivedDate = ReceivedDate
        self.ReportedDate = ReportedDate
        self.IsReportedPrePoll = IsReportedPrePoll
        self.ReportingPeriodName = ReportingPeriodName
        self.IsBequest = IsBequest
        self.IsAggregation = IsAggregation
        self.RegulatedEntityId = RegulatedEntityId
        self.AccountingUnitId = AccountingUnitId
        self.DonorId = DonorId
        self.CampaigningName = CampaigningName
        self.RegisterName = RegisterName
        self.IsIrishSource = IsIrishSource

class Data:
    def __init__(self) -> None:
        self.data = []
        self.format_file()
        self.data = self.read_file()

    def get(self) -> list:
        return self.data

    def format_file(self) -> None:
        data = ""
        with open("./donations.csv", "r") as myFile:
            data = myFile.read()
        with open("./donations.csv.bak", "w") as myFile:
            myFile.write(data)
        
        in_quotes = False
        new_data = ""
        for char in data:
            if (char == '"'):
                in_quotes = not in_quotes

            if (char == "," and in_quotes):
                pass
            else:
                new_data += char 
        with open("./donations.csv", "w") as myFile:
            myFile.write(new_data)

    def read_file(self) -> list:
        donations = []
        with open("./donations.csv", "r") as myFile:
            for line in myFile:
                items = line.rstrip("\n").split(",")
                donations.append(recDonations(
                    items[0], #ecRef
                    items[1], #Entity Name
                    items[2], #Entity Type
                    float(items[3].strip('"').lstrip('£')), #Value
                    items[4], #Accepted Date
                    items[5], #Accounting Unit Name
                    items[6], #Donor Name
                    items[7] == "True", # Accounding Units As Central Party
                    items[8] == "True", # Is Sponsorship
                    items[9], #Donor Status
                    items[10], #Donee Type
                    items[11], #Company Reg Number
                    items[12], #Postcode
                    items[13], #Donation Type
                    items[14], #Nature Of Donation
                    items[15], #Purpose Of Visit
                    items[16], #Donation Action
                    items[17], #Received Date
                    items[18], #Reported Date
                    items[19] == "True", #Is Reported Pre Poll
                    items[20], #Reporting Period Name
                    items[21] == "True", #Is Bequest
                    items[22] == "True", #Is Aggregation
                    items[23], #Regulated Entity Id
                    items[24], #Accounting Unit Id
                    items[25], #Donor Id
                    items[26], #Campaigning Name
                    items[27], #Register Name
                    items[28] == "True", #Is Irish Source
                ))
            return donations
