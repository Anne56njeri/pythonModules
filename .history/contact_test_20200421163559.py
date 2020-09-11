import unittest 
from contact import Contact

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

if __name__ == '__main__':
    unittest.main()        