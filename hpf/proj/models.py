from locale import currency
from django.db import models

class Address(models.Model):
    address = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=100, blank=False)
    town = models.CharField(max_length=100, blank=False, default="")
    postcode = models.CharField(max_length=55, blank=False)
    
    def __str__(self) -> str:
        return "Address: " + self.address + " City: " + self.city + " Postcode: " + self.postcode

class Donor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=False)
    card_last_four = models.IntegerField(blank=False)
    
    # one to many
    address = models.ForeignKey(Address, blank=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Name: " + self.name + " Email: " + self.email + " Last four digits: " +str(self.card_last_four) + " Address: " + self.address.address

class Project(models.Model):
    project_name = models.CharField(max_length=200, blank=False)
   
    # one to one
    max_goal = models.IntegerField(blank=False)
    so_far = models.IntegerField(blank=False, default=0)

    def __str__(self) -> str:
        return "Project Name: " + self.project_name + " Max goal: " +str(self.max_goal) + "Collected so far: " + str(self.so_far)

class FacilityList(models.Model):
    name = models.CharField(max_length=200, default=False)
    max_amount = models.IntegerField(blank=False)
    current_ammount = models.IntegerField(blank=False)
    project = models.ForeignKey(Project, blank=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Facility name: " + self.name + " Max amount: " + str(self.max_amount) + " Current amount: " + str(self.current_ammount)


class DonorTransactions(models.Model):
    paid = models.IntegerField(blank=False)
    currency = models.CharField(max_length=255, blank=True)
    specific_facilities = models.ForeignKey(FacilityList, blank=True, on_delete=models.CASCADE, null=True)
    anonymous = models.CharField(default=False, max_length=20)

    def __str__(self) -> str:
        # return "Name: " + self.donor.name + " How much paid: " + str(self.paid) + " Facility: " +self.specific_facilities
        return "How much paid: " + str(self.paid) + " Facility: " + str(self.specific_facilities) + " Is Anonymous: " + str(self.anonymous)

class DonorList(models.Model):
    donor = models.ForeignKey(Donor, blank=False, on_delete=models.CASCADE)
    transactions = models.OneToOneField(DonorTransactions, blank=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Donor: " + self.donor.name + " Paid: " + str(self.transactions.paid)


class ProjectTransactions(models.Model):
    project = models.ForeignKey(Project, blank=False, on_delete=models.CASCADE)
    donors = models.OneToOneField(DonorList, blank=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Project name: " + self.project.project_name + " Donor: " + self.donors.donor.name


