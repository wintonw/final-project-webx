### Name: 
# **the Neighborhood Eatery -by WebX **

## Team Member and Roles: 
#### Winton Wong: 
- Backend, deployment

#### Julio Gonzalez Gonzalez: 
- Frontend interactive, UI design, html/css, database designs and implementations

## Deployable Website
> http://eateryx.wintonw.com

### User Story/Use Case
> **Customers** views the menu online, order and pay for pickup, and checks order status and detail when logged in. 

> **Manager** can see, accept/reject, change status, cancel, and edit the order of customers and menu items.

> **Manager/restaurant associates** can see, accept/reject, and change order status of the order of customers

### Functionality
- A open source website platform for restaurants to accept and manage orders for pickup, tools to analyze sales, and managing account users
- Customers can create accounts managed by cookies to place, pay, and view orders
- Analyze sales and use google analytics in order to show website performance with customer base
- sales are made through a paypal api(sandbox) that is controled by cookies and generate CSRF Tokens to confirm payment



### Technical Design
- Customers' cart are managed by cookies
- Customer log in is managed by sessions
- Restaurant accounts (manager, restaurant staff) can be reassigned by the superuser or manager
- Customer can track their order status (order accepted, order preparing, order ready, canceled), logged in (full detail) and logged out (partial detail)
- Manager accounts can change and edit each order and have access to the admin page where users and database is controlled
- Restaurant Staff accounts have access to the dashboard where they can can change order status (order accepted, order preparing, order ready) and update on the customers account
- PayPal, ID of payer is recorded into database and posts the order to the dashboard

### Tools/Libraries/Frameworks/Languages
- Backend: Django, Python, JavaScript
- Frontend: Bootstrap, JQuery, HTML, CSS
- Database: SQLite
- Payment: PayPal
- Whitenoise: A middleware that help serve static files in deployment