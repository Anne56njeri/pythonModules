#!/usr/bin/env python3.6 
from contact.contact import Contact 

def create_contact(fname,lname,phone,email):
    new_contact = Contact(fname,lname,phone,email)
    return new_contact 
def save_contacts(contacts):
    contacts.save_contacts()