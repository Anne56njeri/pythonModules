class Contact:
    """
    Class that generates new instances of contacts
    """
    contact_list = []
    def __init__(self,first_name,last_name,phone_number,email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number 
        self.email = email 
    def save_contact(self):
        '''
        save_contact method saves objects into contact list
        '''   
        Contact.contact_list.append(self)
    def delete_contact(self):
        Contact.contact_list.remove(self) 
    '''
    
    ''' 
    @classmethod
    def find_by_number(cls,phone_number):
        '''
        Args: phone number to search for then returns 
        contact of person that matches the number
        ''' 
        for contact in cls.contact_list:
            if contact.phone_number == phone_number:
                return contact
    @classmethod
    def contact_exist(cls,phone_number):
        '''
        method that we use to check whether a contact exists 
        '''
        for contact in cls.contact_list:
            if contact.phone_number == phone_number:
                return True 
        return False    


