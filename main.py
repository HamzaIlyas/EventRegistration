import json


ContactsList = []
LeadsList = []


class Contacts:
    contactscount = 0

    def __init__(self, name, email, phone):
        self.Name = name
        self.Email = email
        self.Phone = phone
        Contacts.contactscount += 1

    def getcontactscount(self):
        print("Total Contacts %d" % Contacts.contactscount)

    def displaycontact(self):
        print("Name : ", self.Name, ", Email : ", self.Email, ", Phone : ", self.Phone)


class Leads:
    leadscount = 0

    def __init__(self, name, email, phone):
        self.Name = name
        self.Email = email
        self.Phone = phone
        Leads.leadscount += 1

    def getleadscount(self):
        print("Total Leads %d" % Leads.leadscount)

    def displaylead(self):
        print("Name : ", self.Name, ", Email : ", self.Email, ", Phone : ", self.Phone)


def addregistrant(registrant):
    if registrant.Email or registrant.Phone:
        contact_phones = {contact.Phone for contact in ContactsList}
        contact_emails = {contact.Email for contact in ContactsList}
        lead_phones = {lead.Phone for lead in LeadsList}
        lead_emails = {lead.Email for lead in LeadsList}

        if registrant.Phone in contact_phones and registrant.Phone:
            print("Registrant already exists in ContactsList phone matched")
            for contact in ContactsList:
                if contact.Phone == registrant.Phone and contact.Phone:
                    if contact.Email:
                        registrant.Phone = contact.Phone
                        registrant.Email = contact.Email
                    else:
                        registrant.Phone = contact.Phone
                    ContactsList.remove(contact)
            ContactsList.append(Contacts(registrant.Name, registrant.Email, registrant.Phone))
        elif registrant.Email in contact_emails and registrant.Email:
            print("Registrant already exists in ContactList email matched")
            for contact in ContactsList:
                if contact.Email == registrant.Email and contact.Email:
                    if contact.Phone:
                        registrant.Phone = contact.Phone
                        registrant.Email = contact.Email
                    else:
                        registrant.Email = contact.Email
                    ContactsList.remove(contact)
            ContactsList.append(Contacts(registrant.Name, registrant.Email, registrant.Phone))
        elif registrant.Phone in lead_phones and registrant.Phone:
            print("Registrant exists in Leadslist phone matched, moved to ContactsList")
            for lead in LeadsList:
                if lead.Phone == registrant.Phone and lead.Phone:
                    if lead.Email:
                        registrant.Phone = lead.Phone
                        registrant.Email = lead.Email
                    else:
                        registrant.Phone = lead.Phone
                    LeadsList.remove(lead)
            ContactsList.append(Contacts(registrant.Name, registrant.Email, registrant.Phone))
        elif registrant.Email in lead_emails and registrant.Email:
            print("Registrant exists in Leadslist email matched, moved to ContactsList")
            for lead in LeadsList:
                if lead.Email == registrant.Email and lead.Email:
                    if lead.Phone:
                        registrant.Phone = lead.Phone
                        registrant.Email = lead.Email
                    else:
                        registrant.Email = lead.Email
                    LeadsList.remove(lead)
            ContactsList.append(Contacts(registrant.Name, registrant.Email, registrant.Phone))
        else:
            ContactsList.append(Contacts(registrant.Name, registrant.Email, registrant.Phone))
            print("Registrant not exists in ContactList or Leadslist, new contact added to ContactsList")


# Registration form starts ---------------
# print('Webinar Registration Form')
# name = input('Enter your name : ')
# email = input('Enter your email : ')
# phone = input('Please input your 10 digit phone no. : ')
# while len(phone) != 10 or not phone.isdigit():
#     print('You have not entered a 10 digit value! Please try again.')
#     phone = input('Please input your 10 digit phone no. : ')
# Registration form ends ---------------


# Given Contacts
ContactsList.append(Contacts('Alice Brown', None, 1231112223))
ContactsList.append(Contacts('Bob Crown', 'bob@crowns.com', None))
ContactsList.append(Contacts('Carlos Drew', 'carl@drewess.com', 3453334445))
ContactsList.append(Contacts('Doug Emerty', None, 4564445556))
ContactsList.append(Contacts('Egan Fair', 'eg@fairness.com', 5675556667))

# Given Leads
LeadsList.append(Leads(None, 'kevin@keith.com', None))
LeadsList.append(Leads('Lucy', 'lucy@liu.com', 3210001112))
LeadsList.append(Leads('Mary Middle', 'mary@middle.com', 3331112223))
LeadsList.append(Leads(None, None, 4442223334))
LeadsList.append(Leads(None, 'ole@olson.com', None))

# Given Registrants
registrant1 = Contacts("Lucy Liu", "lucy@liu.com", None)
registrant2 = Contacts("Doug", "doug@emmy.com", 4564445556)
registrant3 = Contacts("Uma Thurman", "uma@thurs.com", None)


Data = {
    "registrant1":
        {
            "name": registrant1.Name,
            "email": registrant1.Email,
            "phone": registrant1.Phone,
        },
    "registrant2":
        {
            "name": registrant2.Name,
            "email": registrant2.Email,
            "phone": registrant2.Phone,
        },
    "registrant3":
        {
            "name": registrant3.Name,
            "email": registrant3.Email,
            "phone": registrant3.Phone,
        }
}

jsonStr = json.dumps(Data)
with open('data.json', 'w') as file:
    json.dump(jsonStr, file)
# Read JSON file
# with open('data.json', 'r') as j:
#     print(json.load(j))


print("\nContacts in the Starting ContactsList :\n")
for contact in ContactsList:
    print(contact.Name, contact.Email, contact.Phone)

print("\nLeads in the Starting LeadsList :\n")
for lead in LeadsList:
    print(lead.Name, lead.Email, lead.Phone)

print("\nAdding First Registrant...")
addregistrant(registrant1)
print("\nAdding Second Registrant...")
addregistrant(registrant2)
print("\nAdding Third Registrant...")
addregistrant(registrant3)

print("\nContacts in the Final ContactsList :\n")
for contact in ContactsList:
    print(contact.Name, contact.Email, contact.Phone)

print("\nLeads in the Final LeadsList :\n")
for lead in LeadsList:
    print(lead.Name, lead.Email, lead.Phone)
