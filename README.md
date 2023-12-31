# Retail Management System
## 1. Abstract 
The Retail Management System (RMS) project is a comprehensive software solution designed to streamline and enhance various aspects of managing a retail business. It enables the salesperson and the manager of the Retail store to manage the information of customer, employees, suppliers, Products and product many reports. It is developed by `Django framework` and MySQL to manage database.
## 2.Introduction
The aim of this project is the development of a sample centralized relational Retail store application. This application has to store information of customers and employees and suppliers with their products. In this context the functionality is to update, delete and add records for the different entities. It also produces many reports are `stock report`, `item status report`, `purchase report`, `sales report` and `profit report`. It provides the functionality to print barcodes that are generated by python-barcode package using item id. 
### 2.1. Key Features and Modules:
1.	**Stock Management:** Efficiently manage stock levels, monitor product availability.
3.	**Sales Management:** Enable smooth and accurate sales entry, apply discounts, and generate customer receipts.
5.	**Purchase Management:** Handle procurement processes, generate purchase report, manage supplier relationships, and update inventory accordingly.
7.	**Generating Reports:** Provide reports on sales trends, item status and sales profit reports.
9.	**Employee Management:** Manage staff details, their passwords and limited the accessibility of the sectors.
11.	**Generating Barcode:** It generates barcodes for the purchased items based on the item id.
13.	**Security and Access Control:** Implement user roles, authentication, and authorization to ensure data security and compliance.
14.	**Producing product id:** It separates the product into three categories. That are product classification, product and item classification.
### 2.2. Technologies Used
1.	 **Frontend:** HTML, CSS, JavaScript, Bootstrap5
2.	 **Backend:** Python, Django
3.	 **Database:** MySQL
4.	**Version Control:** Git and GitHub

## 3. Architecture
This section illustrates the architecture of the database using an `Entity Relationship Diagram (ERD)` and a Relational Schema Definition. The ERD shows the overall structure and communication of the Retail management system in the database. The Relational Schema Definition describes the tables to be created in the database.
### 3.1 Entity Relationship Diagram
The Entity Relationship Diagram (Figure 1) describes the entities Customer, Product, product classification, item classification, stock and Supplier, employee, sales items, purchase item etc. A product has product name, product id, product classification id. The attributes of each entity are given in a circle with purple color, entities are given in a rectangle with blue color and relationships are given in a diamond with green color. The  relationships such as created by, has, supplied by, part of and buys connect the entities in a structured and simple manner.

![final customer](https://github.com/divyaganesh1104/Retail-Management-System/assets/132454689/1854bbba-46f2-4cae-a493-37ec4b3a7799)
<p align='center'>Figure 1: Entity Relationship Diagram</p>



### 3.2 Relational Table definition
This definition is the base for creating the tables in the database. In general it gives the same information as the ERD but in a more specific way.

 <img alt="YOUR-ALT-TEXT" src="https://github.com/divyaganesh1104/Retail-Management-System/assets/132454689/2f64a6ff-e743-430f-b933-3cdef626ec72E" height=800px>
<p align='center'>Figure 2: Database Schema Diagram</p>

## 4. User Documentation
The User Documentation provides step-by-step instructions for various user roles to effectively utilize the Retail Management System. This section aims to empower users with the knowledge required to navigate and perform key tasks within the system.

### 4.1. User Roles and Access
The system supports multiple user roles, each with specific permissions and access levels. 
The main user roles include:
-	Salesperson
-	Manager
-	Administrator
#### 4.1.1. Salesperson
**User Role:** Salesperson

**Access Level:**
1.	**Customer management:** Salespersons can obtain the details of customer and view their records. 
2.	**Sales entry:** Salespersons have access to the sales entry module, enabling them to process sales, add items to carts, and calculate totals.
3.	**Generates Receipt:** Cashiers can initiate the printing of customer receipts after sales entry.
4.	**View Sales History:** he has the access to view sales history & reports for reference purposes.
#### 4.1.2. Administrator
 **User Role:** Administrator (Admin)
 
 **Access Level:**
1.	**User Management:** Administrators have full control over user accounts, including creating, modifying, and deleting user profiles.
2.	**Access Control:** Administrators can assign roles and access levels to other users, granting or revoking permissions as needed.
3.	**System Monitoring:** They can access logs and monitor system health, identifying and resolving issues promptly.
4.	**Customization:** Administrators can customize the system's appearance, layout.
5.	**Reports and Analytics:** Full access to comprehensive reports, analytics, and insights for informed decision-making.
6.	**Backup and Restore:** Administrators can initiate data backups and perform restores if data loss occurs.
#### 4.1.3. Manager
 **User Role:** Manager
 
 **Access Level:**
1.	**Product Management:** Managers have the ability to add new products to the system and update existing product details.
2.	**Item Stock Monitoring:** They can view current stock levels for each product.
3.	**Restocking:** Managers are authorized to generate purchase orders to replenish low stock items.
4.	**Category Management:** They can create, edit, and manage product categories to organize inventory effectively.
5.	**View Reports:** Manager have access to view inventory reports, including stock movement and product sales data.

### 4.2. Logging in to the System
1.	Open your web browser and navigate to [System URL].
2.	Choose which alternate user you are. if you are a manager, close manager panel it will redirect to the salesperson login page.
   
 ![image-20230816-115157](https://github.com/divyaganesh1104/Retail-Management-System/assets/132454689/98813c9c-a171-4e14-9c72-8bfc444fb618)
<p align='center'>Figure 3: Login User Choices</p>

1.	Enter your username and password provided by your administrator.
2.	Click the "Login" button to access the system or if you want to exit click the ‘Exit’ button.

 ![image-20230816-115729](https://github.com/divyaganesh1104/Retail-Management-System/assets/132454689/1a6e6af4-a00d-4899-b744-dedcc61e35aa)
<p align='center'>Figure 4: Login Page</p>

### 4.3. Dashboard Overview
Upon logging in, you will be directed to the Retail management system home page. The `dashboard` provides an overview of key metrics, about this system, and quick links to different sections of the system. There is an logout button to logged out of the system.

 ![image-20230816-120303](https://github.com/divyaganesh1104/Retail-Management-System/assets/132454689/8b6b0468-1a76-4d6a-9aac-d2f026ccacf7)
<p align='center'>Figure 5: Retail Dashboard</p>

### 4.4. Actors Management
This section includes many operations like `View All Customer` , `Insert New Customer`, `Update Customer Details`, `Search by Customer ID`, `Clear Filter`, `Delete Customer` and `Exit`. Figure 6 shows a list of all customers (View All Customer) and Figure 7 shows a form to `Add Customer`. All attributes of the customers are listed. It is possible to select one and delete or change the customer details. The same is applies to the other actors are `Employee Registration`, `Supplier Management`.

 ![image-20230816-120909](https://github.com/divyaganesh1104/Retail-Management-System/assets/132454689/14f96839-dc7b-481a-8303-c94647e06b49)
<p align='center'>Figure 6: Customer Management</p>

For adding a new customer, the salesperson has to choose the sub-item `Add customer` which opens a new window.

 ![image-20230816-120951](https://github.com/divyaganesh1104/Retail-Management-System/assets/132454689/c1774fe7-ba5f-402e-b44d-7a67dc931a3a)
<p align='center'>Figure 7: Add Customer</p>

### 4.5. Product ID Creation
`Product` has the same overall structure as the `Customer`. This includes `View All Products`, `Add New Product`, `Change Product Details`, `Delete Product` and so on. Figure 8 shows a screenshot of `View All Products` and Figure 9 display the form for `Add New Product`. The same is applies to the other id creation sections are `Product Classification ID`, `Item Classification ID`, `Packed Difference ID`. The most important thing is thus Id’s are interconnected with each other by Django’s foreign key. Additionally, there is a three types of product items. That are `Packed Same`, `Packed Different`, `Unpacked` items. Packed same and unpacked items are stored in item classification table. Packed different items are stored in another table with its specification.

![image-20230816-134535](https://github.com/divyaganesh1104/Retail-Management-System/assets/132454689/39665c7e-345b-4c08-9bd0-8c8464d36528)
<p align='center'>Figure 8: Product Management</p>

 ![image-20230816-134606](https://github.com/divyaganesh1104/Retail-Management-System/assets/132454689/510d6c61-f1e7-4b98-a7b9-f27f8c482e55)
<p align='center'>Figure 9: Add New Product</p>

### 4.6. Purchase Module
The Purchase Management module within the Retail Management System empowers authorized users to efficiently handle procurement processes, ensuring a smooth and organized workflow for acquiring products and maintaining optimal inventory levels. which includes selecting supplier to purchasing from that supplier, add items to purchase list and save data by `Save` button. Figure 10 shows a screenshot of `Purchase Items`. In Purchase entry page, we will not directly select item classification id. It’s a `Chained drop-down`. That means the options in one dropdown menu change based on the selection made in another dropdown.

 ![image-20230816-180240](https://github.com/divyaganesh1104/Retail-Management-System/assets/132454689/ca3accce-9978-49ce-82d7-3c163d379e65)
<p align='center'>Figure 10: Purchase Entry</p>

### 4.7. Sales Module
As we discussed before, there are three types of categories in product. So, sale entry will be committed by different ways based on the product category. when the sale product will come in the category of unpacked item then it's not necessary to enter quantity because unpacked items are the single item. so, there is no quantity. it takes quantity 1 by default. At the same time when packed product will come to sale, it’s necessary to give quantity. The price of the product is updated in item update report. And there is more then 10 warning will occur due to wrong commit. The situations like invalid item id, out of stock, already sold item, some values are missing etc. When a product is sold, a certain change will be implemented in item status and item stock table. The item stock quantity is subtracted by sold quantity on a specific sold item. In item status table, the item status of that item is changed into `sold`.

![image-20230816-181358](https://github.com/divyaganesh1104/Retail-Management-System/assets/132454689/90326d08-a5a7-415d-b05e-9063adb08832)
<p align='center'>Figure 11: Sales Entry</p>
 
The system generates a receipt containing customer and sold item details that provided to the customer.

 ![image-20230816-182202](https://github.com/divyaganesh1104/Retail-Management-System/assets/132454689/bc0dfe6b-1802-4658-8319-b39ed9ce9f3f)
 <p align='center'>Figure 12: Sales Receipt</p>
 
### 4.8. Generating Reports
This report includes features ‘`ilter by Sales id`, `Filter by Date`, `Search item id`, `Clear Filter`, `View Total Amount`, `Update discounts`, `Change Images`, and `Change Cost Price`. Figure 13 shows the `Stock Report`. The same is applies to the other report generation sections are `Item Status Report`, `Item Status Report`, `Item Profit Report`, `Sales Report`, `Purchase Report`, `Sales Profit Report`. 
 
 ![image-20230816-184245](https://github.com/divyaganesh1104/Retail-Management-System/assets/132454689/43acb803-b9ca-47b4-bfd7-30c770a90ccf)
 <p align='center'>Figure 13: Item Stock Report</p>
 
### 4.9. Printing Barcodes
This will happen when products are purchased. The Barcode Printing feature in the Retail Management System provides users with the ability to create and print barcode labels for products, enabling efficient stock management, accurate sales tracking, and streamlined checkout processes. With this functionality, we can enhance the speed and accuracy of various retail operations. This page includes selecting the purchase id to get the purchased item classification id. We can select multiple item classification id or click a `select all` check box to display the barcodes of that id. Finally, `Print Barcode` button print and download as PDF Document format.

 ![image-20230816-185610](https://github.com/divyaganesh1104/Retail-Management-System/assets/132454689/680351e5-5e21-41e5-af68-d646d6423104)
<p align='center'>Figure 14: Barcode Printer</p>

## 5. Test Scenarios
Presenting two test scenarios will test and explain the usage of the database. These scenarios are chosen to create a real-world situation. There are two test scenarios, first scenario is about the sales entry. Second scenario is about purchase entry.
### 5.1. Test scenario 1
**Use Case Title:** Purchase Entry

**Brief Description:** The manager enters purchase records into the system, ensuring accurate tracking of procured products, prices, and supplier information.

**Participating Actors:** Manager

**Preconditions:**
-	The manager is logged into the system.
-	Supplier information is available in the system.
-	Products are created in ‘generating id’ with unique ID.

**Main Flow:**
1.	**Manager initiates a purchase:**
	-	The manager selects the ‘purchasing from supplier’ from the main menu.
	-	The manager needs to select the supplier id and fill the bill no, other things purchase id and date is already placed by the system.
2.	**Product selection:**
	-	The manager selects a product classification, the associated products are fetched based on the product classification object and displayed in the second dropdown. 
	-	Then the manager selects the product from the second dropdown, the associated item classifications are fetched based on the product and choose the item classification.
	-	Further, the manager needs to specify the quantity and rate of the item.
	-	If the selected item classification is the packed different product, then the manager has to declare the specifications and quantity of each item difference. 
3.	**Adding products to the purchase:**
	-	The manager adds each selected product to the purchase list by clicking the "Add" button.
	-	The system calculates the subtotal based on the added items.
4.	**Completing the purchase:**
	-	The manager confirms the selected product items and the total amount.
	-	Finally, the manager saves the selected item by clicking ‘Save’ button.

**Postconditions:**
-	The purchase details are recorded in the ‘Purchase’ table.
-	Stock table is updated.
-	In item status, the barcodes and item ids are generated.
-	A receipt is generated, and barcodes are printed and pasted to each purchased item.

### 5.2. Test scenario 2

**Use Case Title:** Sales Entry

**Brief Description:** The salesperson enters sales records into the system, ensuring accurate recording of products sold, prices, and payment details.

**Participating Actors:** Salesperson

**Preconditions:**
-	The salesperson is logged into the system.
-	items are available in the stock.

**Main Flow:**
1.	**Adding customer:**
	-	The salesperson selects the main menu ‘customer management’ from dashboard.-	The salesperson entries the customer details.
	-	The application is generating a new customer.
2.	**Salesperson initiates a sale:**
	-	The salesperson selects the ‘sales entry’ from the main menu.
	-	The salesperson needs to select the customer id, other things sales id and date is already placed by the system.
3.	**Product selection:**
	-	The salesperson scans by barcode scanner or search the ‘Item ID’ the customer wishes to purchase.
	-	The system retrieves product information like price and availability in stock and displays it on the screen.
4.	**Adding products to the sale:**
	-	The salesperson adds each selected product to the sale by clicking the "Add" button.
	-	The system calculates the subtotal based on the added items.
5.	**Completing the sale:**
	-	The customer confirms the selected product items and the total amount.
	-	Finally, the salesperson saves the selected item by clicking ‘Save’ button.
6.	**Updating completion:**
	-	The system updates the item stock by reducing the quantities of sold items.
	-	And also, if that item fully sold then item status is changed into ‘Sold’. if the item partially sold then item status is changed into ‘Partially sold’.
	-	The system generates a receipt containing customer and sold item details.
	-	The cashier provides the receipt to the customer.
 
**Postconditions:**
-	The sales details are recorded in the system.
-	Stock quantities are updated.
-	A receipt is generated and provided to the customer.

## 6. Conclusion
The core functionality was reached in the following parts. It is possible to insert a new customer, change the details of a customer and delete a customer as well as employee and supplier. Also, the product part is implemented in the same way. A new product can be inserted, changed and deleted. Further the sales and purchase sections were completely implemented. It is possible to generates receipt and gives to the customer. The application also provides error checking: this means every input is tested and if an error occur gives warnings. This gives a better knowledge of `Python programming and Django` during project development.




