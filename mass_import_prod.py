import json
from openpyxl import Workbook

# Site ID(req)	Product Code(req) CP Category Name(req)	Display as Featured	Can be Sold Online	Description(req)	Long Desc.	Search Words	Thumbnail Img.	  Large Img.	B.L.P	Drop Ship Online	Low Quantity	Images
# CustPortal	400DSTW102HMST	HEMSTITCH SOLID DUVET SET	No	                  Yes	      Hemstitch Twin Ivory			                   small_bamboo.jpg	  all_seasons.jpg		Yes		


class Person:
    
    # Setup initial static properties 
    def __init__(self, prod_code, cp_cat_name, ):
        self.site_id            = 'CustPortal'
        self.prod_code          = prod_code   
        self.cp_cat_name        = cp_cat_name
        self.featured           = 'No'
        self.sold_online        = 'Yes'
        self.long_description   = ''
        self.search_words       = ''
        self.blp                = ''
        self.drop_ship          = 'Yes'
        self.low_quantity       = 0

    # If a key isn't in my dictionary, this will update the dict with the new value
    # It takes the keyError as the argument
    def update_keys(self, e):
        data = ''
        print('[!] Attempting to update key.')
        # Open dict file and update the value
        with open('dict.json') as json_file:
            data = json.load(json_file)
            #print(data['color_trans'])
            print('[?] What needs to be added? [T]type, [S]size, [C]color & the key is: ' + e)
            key = input('> ')
            print('[?] What is the value?')
            val = input('> ')
            
            if key.lower() == 't':
                data['type_trans'][e] = val
            elif key.lower() == 's':
                data['size_trans'][e] = val
            elif key.lower() == 'c':
                data['color_trans'][e] = val
            else:
                print('[X] Exiting because of invalid input.')
                quit() # Exit program if an unknow val is given
        
        # Return the dict object to json format and re-save the file
        with open('dict.json', 'w') as writer:
            js = json.dumps(data)
            print(js)
            writer.write(js)
            print('[!] Update Success.')

    # This continues the setup process, but confirms if a key exist
    def clean_up(self):
        self.thread_count       = self.prod_code[:3]
        self.type               = self.prod_code[3:5]
        self.size               = self.prod_code[5:7]
        self.color              = self.prod_code[7:10]
        self.prod_name          = self.prod_code[10:]
        
        # Open dict file and get data
        with open('dict.json') as json_file:
            data = json.load(json_file)
            #print(data.size_trans)
            
            try:
                if self.thread_count.isnumeric():
                    if self.thread_count == '999':
                        self.description        = "{0} {1} {2}".format(self.prod_name, data['size_trans'][self.size], data['color_trans'][self.color])
                    
                    else:
                        self.description        = "{0} thread count {1} {2} {3}".format(self.thread_count, self.prod_name, data['size_trans'][self.size], data['color_trans'][self.color])
                else:
                    self.description            = "{0} {1} {2}".format(self.prod_name, data['size_trans'][self.size], data['color_trans'][self.color])
                
                #self.description        = "{0} thread count {1} {2} {3}".format(self.thread_count, self.prod_name, data['size_trans'][self.size], data['color_trans'][self.color]) if self.thread_count.isnumeric() else "{0} {1} {2}".format(self.prod_name, data['size_trans'][self.size], data['color_trans'][self.color])
                
                self.thmb_img           = 'Bedding/{0}/{1}/{2}.jpg'.format(data['type_trans'][self.type], self.prod_name, data['color_trans'][self.color])
                
                self.lrg_img            = 'Bedding/{0}/{1}/{2}_lg.jpg'.format(data['type_trans'][self.type], self.prod_name, data['color_trans'][self.color])
                
                self.images             = 'Bedding/{0}/{1}/{2}_lg.jpg,Bedding/{0}/{1}/{2}.jpg'.format(data['type_trans'][self.type], self.prod_name, data['color_trans'][self.color])  # large_img, thmb_img
                print('[*] Clean up completed successfully.')
            
            # If the code jumps here, it's more than likely because a key was encountered that doesn't exist in my dict
            # We'll pass that new key to the update_keys funct and add it to my dict for future use
            except KeyError as e:
                print('[!] There was a key error: {0}'.format(e))
                error = str(e).strip('\'')
                self.update_keys(error)
                self.clean_up()


def main():
    # Get cat name from user
    print('What is the category name?')
    category_name = input('> ')
    
    # This gets all the products from a file
    products = ''
    with open('products.txt', 'r') as reader:
        # Note: readlines doesn't trim the line endings
        products = reader.read().splitlines()
        print(products)
        
    # This opens a new excel sheet and makes it editable
    workbook = Workbook()
    sheet = workbook.active

    # Iterate through all the products and add them to the sheet
    for num, prod in enumerate(products, start=1):
        print('[*] Adding product: {0} of {1}'.format(num, len(products)))
        # Pop off class func
        p1 = Person(prod, category_name) 
        p1.clean_up()
        sheet["A{0}".format(num)] = p1.site_id
        sheet["B{0}".format(num)] = p1.prod_code
        sheet["C{0}".format(num)] = p1.cp_cat_name
        sheet['D{0}'.format(num)] = p1.featured
        sheet['E{0}'.format(num)] = p1.sold_online
        sheet['F{0}'.format(num)] = p1.description
        sheet['G{0}'.format(num)] = p1.long_description
        sheet['H{0}'.format(num)] = p1.search_words
        sheet['I{0}'.format(num)] = p1.thmb_img
        sheet['J{0}'.format(num)] = p1.lrg_img
        sheet['K{0}'.format(num)] = p1.blp
        sheet['L{0}'.format(num)] = p1.drop_ship
        sheet['M{0}'.format(num)] = p1.low_quantity
        sheet['N{0}'.format(num)] = p1.images
        del p1 # Delete class instance

    # Save workbook
    print('[*] Saving File')
    workbook.save(filename="hello_world.xlsx")
    print('[!] Done')




if __name__ == '__main__':
    main()
