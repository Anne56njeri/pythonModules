#!/usr/bin/env python3.6 
from contact.contact import Contact 

def create_contact(fname,lname,phone,email):
    new_contact = Contact(fname,lname,phone,email)
    return new_contact 
def save_contacts(contact):
    contact.save_contacts()
def delete_contact(contact):
    contact.delete_contact()
def find_contact(number):
    return Contact.find_by_number(number)
def display_contacts():
    return Contact.display_contacts()
def  copy_email(number):

    return  Contact.           