import unittest 
from unittest.mock import patch
from Mini_Project6 import updating, add_products_to_order, delete_product_from_orders, choose_courier, add_item_to_database, delete_item_in_database


class Test_Mini_Project6(unittest.TestCase):


    @patch("miniproject6_func.input")
    @patch("miniproject6_func.connecting_to_database")
    def test_updating(self, database, input):

        #Assemble
        input.return_value = "Sabela"
        expected = "UPDATE couriers SET name = 'Sabela' WHERE courier_id = '3'"

        #Act
        updating("couriers", "courier", "name", "name", 3)

        #Assert
        database.assert_called_with(expected) 


    @patch("miniproject6_func.display_database")
    @patch("miniproject6_func.input")
    def test_empty_add_products_to_order(self, input, database):
       
        #Assemble
        # input.return_value = 3
        input.return_value = 0
        expected = []


        #Act
        actual = add_products_to_order()

        #Assert
        self.assertEqual(expected, actual)


    @patch("miniproject6_func.display_database")
    @patch("miniproject6_func.input")
    def test_add_products_to_order(self, input, database):
       
        #Assemble
        input.side_effect = [3,0]
        expected = [3]


        #Act
        actual = add_products_to_order()
        
        #Assert
        self.assertEqual(expected, actual)


    @patch("miniproject6_func.display_database")
    @patch("miniproject6_func.input")
    def test_sad_add_products_to_order(self, input, database):
       
        #Assemble
        input.side_effect = ["h",0]
        expected = []

        #Act
        actual = add_products_to_order()
        
        #Assert
        self.assertEqual(expected, actual)


    # @patch("miniproject6_func.input")
    # @patch("miniproject6_func.connecting_to_database")
    # def test_delete_product_from_orders(self, database, input):

    #     #Assemble
    #     input.side_effect = '2'
    #     expected = "DELETE FROM orders_products WHERE product_id = 2 and order_id = '3'"
    #     #Act
    #     delete_product_from_orders(3)

    #     #Assert
    #     database.assert_called_with(expected) 



    # @patch("miniproject6_func.input")
    # @patch("miniproject6_func.display_database")
    # def test_choose_courier(self, database, input):
       
    #     #Assemble
    #     input.side_effect = 1
    #     expected = 1

    #     #Act
    #     actual = choose_courier()
        
    #     #Assert
    #     self.assertEqual(expected, actual)


    @patch("miniproject6_func.input")
    @patch("miniproject6_func.connecting_to_database")
    def test_add_item_to_database(self, database, input):

        #Assemble
        input.side_effect = ["Kat", "78901234567"]
        courier_columns = ["ID","courier", "phone_number"]
        expected = 'INSERT INTO couriers (courier, phone_number) VALUES ("Kat", 78901234567)'

        #Act
        add_item_to_database("couriers", "ID", "courier", "phone_number", courier_columns)

        #Assert
        database.assert_called_with(expected) 



    # @patch("miniproject6_func.input")
    # @patch("miniproject6_func.connecting_to_database")
    # def test_sad_add_item_to_database(self, database, input):

    #     #Assemble
    #     input.side_effect = ["Dates", "fail"]
    #     product_columns = ["ID","product", "price"]
    #     expected = "Invalid price, please enter again"

    #     #Act
    #     actual = add_item_to_database("products", "ID", "product", "price", product_columns)

    #     #Assert
    #     self.assertEquals(expected, actual)



    # @patch("miniproject6_func.input")
    # @patch("miniproject6_func.connecting_to_database")
    # def test_delete_item_in_database(self, database, input):

    #     #Assemble
    #     input.side_effect = [1, "1"]
    #     product_columns = ["ID","product", "price"]
    #     expected = "DELETE FROM products WHERE product_id = 1"

    #     #Act
    #     delete_item_in_database("products", "product", product_columns)

    #     #Assert
    #     database.assert_called_with(expected) 







if __name__ == "__main__":
    unittest.main()   















# test_list = {1,"test1","test2", 
# 2,"test1","test2"




# rows
# ((2, 'Milk', Decimal('1.50')), (3, 'Eggs', Decimal('1.25'))

# headers
# ['ID', 'product', 'price']