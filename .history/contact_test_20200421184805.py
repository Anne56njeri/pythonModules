import unittest 
from contact.contact import Contact

class TestContact(unittest.TestCase):
    def setUp(self):
        '''
        set up method that should run before each test case
        '''
        self.new_contact = Contact("Maryanne","Njeri","071234567","mary.jereh@gmail.com")

    def test_init(self):
        '''
        this is to test whether the objects have been intialized properly
        '''    
        self.assertEqual(self.new_contact.first_name,"Maryanne")
        self.assertEqual(self.new_contact.last_name,"Njeri")
        self.assertEqual(self.new_contact.phone_number,"071234567")
        self.assertEqual(self.new_contact.email,"mary.jereh@gmail.com")
    def test_save_contact(self):
        '''
        tesy whether conatcts are saved succesfully
        '''
        self.new_contact.save_contact() 
        self.assertEqual(len(Contact.contact_list),1)
    def tearDown(self):
        '''
        this does clean up after each test case runs 
        '''  
        Contact.contact_list = []      
    def test_save_multiple_contacts(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)
    def test_delete_contact(self):
        # You've saved two contacts
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
        test_contact.save_contact()
        self.new_contact.delete_contact()
        test_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list),0)
    def test_find_contact_by_number(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
        test_contact.save_contact()
        found_contact = Contact.find_by_number("0712345678")
        self.assertEqual(found_contact.email,test_contact.email)
    def test_contact_exists(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0711223344","test@user.com") # new contact
        test_contact.save_contact()
        contact_exists = Contact.contact_exists("0711223344")
        self.assertTrue(contact_exists)

   
'''
this is just to make sure that everything in this files runs if this is the right file being run
'''
if __name__ == '__main__':
    unittest.main()        