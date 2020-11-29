### Name: 
# **the Neighborhood Eatery -by WebX**

## Team Member and Roles: 
#### Winton Wong: 
- Backend, deployment

#### Julio Gonzalez Gonzalez: 
- Frontend interactive, UI design, html/css, database designs and implementations

### Functionality
> A open source website platform for restaurants to accept manage orders for pickup, and maybe tools to analyze sales

### User Story/Use Case
> **Customers** views the menu online, order for pickup, with or without an account. 

> **Manager** can see, accept/reject, change status, cancel, edit, refund, of the order of customers

> **Manager/restaurant associates** can see, accept/reject, change order status, of the order of customers

### Technical Design
- Customers' cart are managed by sessions or cookies
- **Potentially:** Customer create an account with phone verification required
- Restaurant accounts (manager, restaurant associates) to be created by the superuser
- Customer can track their order status (order accepted, order preparing, order ready, canceled)
- Manager accounts can change and edit each order and refund
- Restaurant accounts can change order status (order accepted, order preparing, order ready)
- Manager accounts can shutdown or open the restaurant to accept/reject orders base on time of business

### Tools/Libraries/Frameworks
- Django: backend
- SQLite
  - Haven't decide yet
- **Potentially:** Twilio: Verify customer is real and have a phone
- Payment: PayPal/Square/Stripe