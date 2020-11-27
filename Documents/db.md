**Menu**

`{
    categories: `<br>`
    sub-category-items: [] # by ID of MenuItems
}`

**MenuItems**

`{
    itemsName: 
    price: 
}`

**Users**

`{
    userType: # manager, associates, customers `<br>`
    email: `<br>`
    password: 
    phone: 
    dateCreated: 
}`

**Orders**

`{
    items: [itemsID: #, ]
    status: 
    payment: 
    total: 
    comment: 
    datetime: 
}`

----
Food orders: 
Order ID(foreign key), Food Items(foreign key), Quantity, quantity price(will be a function calculated using menu table)

Customer:
Fist name, Last name, email, phone number, address, customer id(primary key);

menu:
food_id(primary key), food item name, price

orders:
customer id(foreign key), order id(primary key), total price, date of purchase, time, customer comment

* Accounts
Fist name, Last name, email, phone number, address, account id(primary key), is_admin, is_staff;
