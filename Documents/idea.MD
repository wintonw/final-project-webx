### Name: 
# **the Neighborhood Eatery -by WebX**

## Team Member and Roles: 
#### Winton Wong: 
- Backend, deployment

#### Julio Gonzalez Gonzalez: 
- Frontend interactive, UI design, html/css, database designs and implementations

### Functionality
> A open source website platform for restaurants to accept manage orders for pickup, and maybe tools to analyze sales
> analyze sales, google analytics 
> CSRF
> Sessions
> Cookies

### User Story/Use Case
> **Customers** views the menu online, order for pickup, with an account. 

> **Manager** can see, accept/reject, change status, cancel, edit, of the order of customers

> **Manager/restaurant associates** can see, accept/reject, change order status, of the order of customers

### Technical Design
- Customers' cart are managed by cookies
- Customer log in is managed by sessions
- Restaurant accounts (manager, restaurant associates) to be reassigned by the superuser or manager
- Customer can track their order status (order accepted, order preparing, order ready, canceled), logged in and logged out
- Manager accounts can change and edit each order
- Restaurant Staff accounts can change order status (order accepted, order preparing, order ready) in the dashboard
- PayPal, ID of payer is recorded

### Tools/Libraries/Frameworks
- Backend: Django
- Frontend: Bootstrap, JQuery
- Database: SQLite
- Payment: PayPal
- Whitenoise: A middleware that help serve static files in deployment