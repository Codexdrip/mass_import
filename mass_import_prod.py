import json
import sys
from openpyxl import Workbook
from helper_func import find_val

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
        self.thread_count       = self.prod_code[:3]
        self.type               = self.prod_code[3:5]
        self.size               = self.prod_code[5:7]
        self.color              = self.prod_code[7:10]
        self.prod_name          = self.prod_code[10:]
        self.ex_color           = find_val("program\\color_code.xlsx", self.color)
        self.ex_size            = find_val("program\\size.xlsx", self.size)
        self.ex_type            = find_val("program\\category.xlsx", self.type)
        self.ex_threads         = find_val("program\\thread_count.xlsx", self.thread_count)
        self.description        = "{0} {1} {2} {3}".format(self.ex_threads, self.prod_name, self.ex_size, self.ex_color)
        self.thmb_img           = 'Bedding/{0}/{1}/{2}.jpg'.format(self.ex_type, self.prod_name, self.ex_color)  
        self.lrg_img            = 'Bedding/{0}/{1}/{2}_lg.jpg'.format(self.ex_type, self.prod_name, self.ex_color)  
        self.images             = 'Bedding/{0}/{1}/{2}_lg.jpg,Bedding/{0}/{1}/{2}.jpg'.format(self.ex_type, self.prod_name, self.ex_color)  # large_img, thmb_img
        
        print('[*] Setting properties')
        

    

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
        try: 
            p1 = Person(prod, category_name) 
        except:
            print("[X] Unexpected error:", sys.exc_info()[0])
            raise
        else:
            # p1.clean_up()
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
    try:
        workbook.save(filename="hello_world.xlsx")
    except:
        print("[X] Unexpected Error! Is the file open? ", sys.exc_info()[0])
        raise
    else:
        print('[!] Done')




if __name__ == '__main__':
    main()
