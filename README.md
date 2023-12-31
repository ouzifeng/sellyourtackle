![Sell Your Tackle](static/media/sell-your-tackle-logo.png)

# Sell Your Tackle

### Use Case

A large fishing tackle shop chain has approach me to help them solve a business related problem they are facing regarding sales growth. As one of the largest chains, they already have the purchasing power to price new tackle competitively in the market, and have maxed out growth in this area. 

Their executive team has tasked the chief revenue officer to find new avenues for revenue growth. One area she is keen to grow into is the used tackle market. The executive team likes this idea, but they want to protect their brand equity by first testing the model under a different business name "Sell Your Tackle" while they learn the ins and outs of running a C2C business. ALthough they have understood the risk of this model cannibalising their new tackle sales, they believe the used tackle market is big enough so that sales from this segment outweigh any drop off in sales of new tackle.

They believe that the ability to provide their customer base with a more holistic solution will drive sales expodentially in the future, and futher solidify their spot as the numner 1 place to purchase fishign tackle in the UK. Their leadership team has approached me with a clear and well defined scope of exactly what they need, and have asked me to excecute the build for them

![Responsive Image](docs/sellyourtackle-responsive.png)
[Live Site](https://www.sellyourtackle.co.uk/)

## Table of Contents

- [Sell Your Tackle](#sell-your-tackle)
    - [Use Case](#use-case)
  - [Table of Contents](#table-of-contents)
  - [Project Scope](#project-scope)
    - [Site Owner Goals](#site-owner-goals)
    - [User Goals](#user-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
  - [User Stories](#user-stories)
    - [Users](#users)
    - [Selling](#selling)
    - [Buying](#buying)
    - [Admin/Site Owner](#adminsite-owner)
    - [Project Management](#project-management)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Wireframes](#wireframes)
  - [Structure](#structure)
    - [Code Structure](#code-structure)
    - [Environment Variables](#environment-variables)
    - [Product Images](#product-images)
    - [Database Structure](#database-structure)
- [Models Documentation](#models-documentation)
  - [Brand Model](#brand-model)
  - [Category Model](#category-model)
  - [Product Model](#product-model)
  - [ProductImage Model](#productimage-model)
  - [WebhookLog Model](#webhooklog-model)
  - [Address Model](#address-model)
  - [EmailConfirmationToken Model](#emailconfirmationtoken-model)
  - [Order Model](#order-model)
  - [OrderItem Model](#orderitem-model)
  - [PasswordResetToken Model](#passwordresettoken-model)
  - [User Model (CustomUser)](#user-model-customuser)
  - [Features](#features)
    - [Account Creation \& Login](#account-creation--login)
    - [Password Reset](#password-reset)
    - [List item for sale](#list-item-for-sale)
    - [Seller and Account Area](#seller-and-account-area)
    - [Selling Management](#selling-management)
    - [Buying and Selling Emails](#buying-and-selling-emails)
    - [Contact Page](#contact-page)
    - [Delete products](#delete-products)
    - [Buyer Area](#buyer-area)
    - [Cart \& Checkout Page](#cart--checkout-page)
    - [Admin Dashboard](#admin-dashboard)
  - [Technologies Used](#technologies-used)
    - [Languages and Frameworks](#languages-and-frameworks)
    - [Libraries and Tools](#libraries-and-tools)
  - [Validation](#validation)
    - [HTML](#html)
    - [Accessibility](#accessibility)
    - [CSS](#css)
    - [Javascript](#javascript)
    - [Python](#python)
      - [Admin App](#admin-app)
      - [Auth App](#auth-app)
      - [Tackle App](#tackle-app)
  - [Testing](#testing)
    - [Automated unit testing](#automated-unit-testing)
      - [Models Tests](#models-tests)
      - [Form Tests](#form-tests)
      - [View Tests](#view-tests)
      - [CustomUser Model Test](#customuser-model-test)
      - [Stripe Integration Tests](#stripe-integration-tests)
    - [Manual Testing](#manual-testing)
      - [Selling](#selling-1)
      - [Buying](#buying-1)
    - [Admin/Site Owner](#adminsite-owner-1)
    - [Device Testing \& Browser Compatibility](#device-testing--browser-compatibility)
  - [Commission](#commission)  
  - [Security](#security)
  - [Bug Fixes](#bug-fixes)
  - [Database Indexing](#database-indexing)
  - [Planned Improvments For The Next Build](#planned-improvments-for-the-next-build)
  - [Heroku Deployment](#heroku-deployment)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Making a Local Clone](#making-a-local-clone)
  - [Credits](#credits)
    - [Images](#images)
    - [Code](#code)
  - [Testing](#testing-1)
  - [Acknowledgements](#acknowledgements)
    - [Special thanks to the following:](#special-thanks-to-the-following)


## Project Scope

The scope of this project is to build a fully responsive platform which allows users to buy, list and sell fishing tackle to other users. To reduce the complexity of a project which is already complex, it has been agreed that the platform should only allow users to list products one by one. If they want to sell multiple products, they can list their items multiple items, or in a single listing with the amount in the title, i.e. 3x rods

### Site Owner Goals

* To begin with, offer commission free sales. But they want to understand how to add a fee once the platform has hit a critical mass
* To allow users to list, buy and sell tackle
* To grow their business in an area they previously have had no traction in
* To learn how to run a C2C business

### User Goals

* Free up cash by selling fishing tackle they no longer use
* Save money by buying use tackle, instead of brand new

## User Experience

### Target Audience

* The target audience is all of the 1m+ registered anglers in the UK
* This will include customers of their existing, new tackle platform

### User Requirements and Expectations

* Fully responsive
* Funds from sales should be sent directly to users bank accounts
* List tackle quickly and efficiently
* Message buyers and sellers if they have any issue/questions
* Buyer and seller protection from the marketplace owners

## User Stories

The user requirements given are in depth so I have marked each one with an M = must have, or an N = nice to have

### Users

### Selling

| Number | Action                                                   | M/N |
|--------|----------------------------------------------------------|-----|
| 1      | Login and create an account                              | M   |
| 2      | Use Google as an SSO                                     | N   |
| 3      | Change their username                                    | N   |
| 4      | Single form to list tackle                               | N   |
| 5      | Predefined brands and categories to speed up listing     | N   |
| 6      | Ability to upload images to product, regardless of size  | M   |
| 7      | Connect bank account to get paid                         | M   |
| 8      | Message buyers in case of order issues                   | M   |
| 9      | View past sales                                          | M   |
| 10     | See shipping information when an item is sold            | M   |
| 11     | Input tracking details and send to the buyer             | M   |
| 12     | Contact page for order disputes                          | M   |
| 13     | Responsive design for checking listings on the go        | N   |
| 14     | Edit or delete products unless sold                      | M   |
| 15     | Reset password in case of forgetting it                  | M   |
| 16     | Email notification once item is sold                     | M   |
| 17     | Refund orders if unable to ship                          | M   |

### Buying

| Number | Action                                                    | M/N |
|--------|-----------------------------------------------------------|-----|
| 18     | Login and create an account                               | M   |
| 19     | Use Google as an SSO                                      | N   |
| 20     | Reset password in case of forgetting it                   | M   |
| 21     | Area to view past orders                                  | M   |
| 22     | See tracking information once shipped                     | M   |
| 23     | Negate the need for duplicate address inputs at checkout  | N   |
| 24     | Different payment options at checkout                     | N   |
| 25     | Ability to message seller with questions                  | M   |
| 26     | Ability to message site admins for order help             | M   |

### Admin/Site Owner

| Number | Action                                         | M/N |
|--------|------------------------------------------------|-----|
| 27     | View and manage orders in admin dashboard      | M   |
| 28     | View and manage users in admin dashboard       | M   |
| 29     | View and manage products in admin dashboard    | M   |
| 30     | Refund orders on behalf of sellers             | M   |


### Project Management

* User Github Kanban to build the project development framework and timeframe
* Identify Epics and link each user story to an Epic
* Identify milestones and link each user story to a milestone
* Use user stories for each card
* Use backlog, in progress and done as statuses


<details><summary>Epics</summary>
<img src="docs/epics.png" alt="Epics">
</details>


<details><summary>User Stories</summary>
<img src="docs/user_stories.png" alt="User Stories">
</details>

<details><summary>Milestones</summary>
<img src="docs/milestones.png" alt="Milestones">
</details>

<details><summary>Kanban Board</summary>
<img src="docs/kanban.png" alt="Kanban Board">
</details>

## Design

### Colours

Taking inspiration from Reverb, a marketplace for used musical instruments, I wanted a colour theme which reflected calm and traniqulity to reflect the serenity and peacefulness associate with going fishing. I chose a a soft peach colour as the main colour and wanted a few few contrasting colours to go help highlight important areas

![Colour Palette](docs/colors_io.png)

### Fonts 

As the main font I choose the Google font Poppins. Poppins is described as the "geometric shapes keep the type readable in small sizes, while its modern yet timeless curves look striking when blown up on big screens or mobile devices. It's perfect for web and UI designs that demand style, clarity, and legibility".

This description met my criteria for a font. 


### Wireframes

<details>
<summary>404</summary>
<img src="docs/wireframes/404_desktop.png" alt="404 Desktop">
<img src="docs/wireframes/404_tablet.png" alt="404 Tablet">
<img src="docs/wireframes/404_mobile.png" alt="404 Mobile">
</details>

<details>
<summary>Account Settings</summary>
<img src="docs/wireframes/account_settings_desktop.png" alt="Account Settings Desktop">
<img src="docs/wireframes/account_settings_tablet.png" alt="Account Settings Tablet">
<img src="docs/wireframes/account_settings_mobile.png" alt="Account Settings Mobile">
</details>

<details>
<summary>Buyer Order Page</summary>
<img src="docs/wireframes/buyer_order_page_desktop.png" alt="Buyer Order Page Desktop">
<img src="docs/wireframes/buyer_order_page_tablet.png" alt="Buyer Order Page Tablet">
<img src="docs/wireframes/buyer_order_page_mobile.png" alt="Buyer Order Page Mobile">
</details>

<details>
<summary>Buying Selling</summary>
<img src="docs/wireframes/buying_selling_desktop.png" alt="Buying Selling Desktop">
<img src="docs/wireframes/buying_selling_tablet.png" alt="Buying Selling Tablet">
<img src="docs/wireframes/buying_selling_mobile.png" alt="Buying Selling Mobile">
</details>

<details>
<summary>Cart</summary>
<img src="docs/wireframes/cart_desktop.png" alt="Cart Desktop">
<img src="docs/wireframes/cart_tablet.png" alt="Cart Tablet">
<img src="docs/wireframes/cart_mobile.png" alt="Cart Mobile">
</details>

<details>
<summary>Checkout</summary>
<img src="docs/wireframes/checkout_desktop.png" alt="Checkout Desktop">
<img src="docs/wireframes/checkout_tablet.png" alt="Checkout Tablet">
<img src="docs/wireframes/checkout_mobile.png" alt="Checkout Mobile">
</details>

<details>
<summary>Connect Stripe</summary>
<img src="docs/wireframes/connect_stripe_desktop.png" alt="Connect Stripe Desktop">
<img src="docs/wireframes/connect_stripe_tablet.png" alt="Connect Stripe Tablet">
<img src="docs/wireframes/connect_stripe_mobile.png" alt="Connect Stripe Mobile">
</details>

<details>
<summary>Edit Product</summary>
<img src="docs/wireframes/edit_product_desktop.png" alt="Edit Product Desktop View">
<img src="docs/wireframes/edit_product_tablet.png" alt="Edit Product Tablet View">
<img src="docs/wireframes/edit_product_mobile.png" alt="Edit Product Mobile View">
</details>

<details>
<summary>Forgot Password</summary>
<img src="docs/wireframes/forgot_password_desktop.png" alt="Forgot Password Desktop View">
<img src="docs/wireframes/forgot_password_tablet.png" alt="Forgot Password Tablet View">
<img src="docs/wireframes/forgot_password_mobile.png" alt="Forgot Password Mobile View">
</details>

<details>
<summary>Form</summary>
<img src="docs/wireframes/form_desktop.png" alt="Form Desktop View">
<img src="docs/wireframes/form_tablet.png" alt="Form Tablet View">
<img src="docs/wireframes/form_mobile.png" alt="Form Mobile View">
</details>

<details>
<summary>Order Confirmation</summary>
<img src="docs/wireframes/order_confirmation_desktop.png" alt="Order Confirmation Desktop View">
<img src="docs/wireframes/order_confirmation_tablet.png" alt="Order Confirmation Tablet View">
<img src="docs/wireframes/order_confirmation_mobile.png" alt="Order Confirmation Mobile View">
</details>

<details>
<summary>Home</summary>
<img src="docs/wireframes/home_desktop.png" alt="Home Desktop View">
<img src="docs/wireframes/home_tablet.png" alt="Home Tablet View">
<img src="docs/wireframes/home_mobile.png" alt="Home Mobile View">
</details>

<details>
<summary>Login</summary>
<img src="docs/wireframes/login_desktop.png" alt="Login Desktop View">
<img src="docs/wireframes/login_tablet.png" alt="Login Tablet View">
<img src="docs/wireframes/login_mobile.png" alt="Login Mobile View">
</details>

<details>
<summary>Product Page</summary>
<img src="docs/wireframes/product_page_desktop.png" alt="Product Page Desktop View">
<img src="docs/wireframes/product_page_tablet.png" alt="Product Page Tablet View">
<img src="docs/wireframes/product_page_mobile.png" alt="Product Page Mobile View">
</details>

<details>
<summary>Product Sold</summary>
<img src="docs/wireframes/product_sold_desktop.png" alt="Product Sold Desktop View">
<img src="docs/wireframes/product_sold_tablet.png" alt="Product Sold Tablet View">
<img src="docs/wireframes/product_sold_mobile.png" alt="Product Sold Mobile View">
</details>

<details>
<summary>Reset Password</summary>
<img src="docs/wireframes/reset_password_desktop.png" alt="Reset Password Desktop View">
<img src="docs/wireframes/reset_password_tablet.png" alt="Reset Password Tablet View">
<img src="docs/wireframes/reset_password_mobile.png" alt="Reset Password Mobile View">
</details>

<details>
<summary>Sign Up</summary>
<img src="docs/wireframes/signup_desktop.png" alt="Sign Up Desktop View">
<img src="docs/wireframes/signup_tablet.png" alt="Sign Up Tablet View">
<img src="docs/wireframes/signup_mobile.png" alt="Sign Up Mobile View">
</details>

## Structure

### Code Structure

The application is built using the DJango framework, and is broken up into 4 main apps to help with future maintaince, code transparency and further feature building

* admin_app - this houses all the admin dashboard functionality
* auth_app - this houses all the authentication functionality, including login, logout, registration, password reset and allauth for SSO
* sellyourtackle - the houses the main app setting and master URL file 
* tackle - the houses all the functionality related to listing, selling and buying tackle

Within these apps you will find a models.py file, which contains all the models used in the app,a views.py file which contains all the views used in the app, and a urls.py file which contains all the URLs used in the app. When it makes sense to do so, files have been created to silo specific functionality, such as the stripe.py file sound in the auth_app. This file manages the Stripe webhook and user account creation

Within the tackle and auth_app you will also find the relevant templates for each related page. 

Along with the apps, there is a:

* template folder - houses the base template and the landing page template
* verification-files folder- holds the apple pay verificatio file needed for enabling Apple Pay on the checkout
* static folder - houses all the static files, such as site images (but not product images), css and javascript
* Procfile - hosts the gunicorn setting for Heroku
* manage.py - manages the database and the app
* requirements.txt - list of thrid party libraries required to be installed when deployed


### Environment Variables

Enviroment variables are stored in a.env file, which is not tracked by git. This file contains all the sensitive information for the app, such as the database credentials. Once the app is deployed, the.env file is not tracked, and this sensitive information is stored in the Heroku environment variables.

### Product Images

Product images are stored in an AWS S3 bucket. This is to reduce server space and page load times

### Database Structure

The database used is a postgresql db hosted at neon.tech. 

# Models Documentation

The following models were created to represent the database structure for the Tackle application within the website:

## Brand Model

Represents different brands of fishing tackle available within the application.

- **Fields**:
  - `name`: Stores the brand's name.

## Category Model

Represents various categories of fishing tackle.

- **Fields**:
  - `name`: Stores the category's name.
  - `condition_choices`: Enumerates the condition of the tackle (Perfect, Excellent, Good, Fair).
  - `financial_status_choices`: Enumerates the financial status (Unsold, Sold, Draft, Live).

## Product Model

Represents the products being sold on the application.

- **Fields**:
  - `name`: Stores the product's name.
  - `slug`: Stores URL-friendly identifiers for the product.
  - `variation1`: Stores the first variation detail of the product.
  - `variation2`: Stores the second variation detail of the product.
  - `condition`: Stores the condition of the product based on predefined choices.
  - `description`: Stores a detailed description of the product.
  - `created_at`: Records the date and time the product was created.
  - `price`: Stores the price of the product.
  - `shipping`: Stores the shipping cost of the product.
- **Relationships**:
  - `brand`: Links to the Brand model.
  - `category`: Links to the Category model.
  - `user`: Links to the User model from the `auth_app`.
- **Methods**:
  - `is_in_stock()`: Checks if the product is in stock.
  - `save(*args, **kwargs)`: Customizes the save operation.
  - `total_with_shipping()`: Calculates the total price including shipping.

## ProductImage Model

Represents images associated with products.

- **Fields**:
  - `image`: Stores the image file.
- **Relationships**:
  - `product`: Links to the Product model.

## WebhookLog Model

Used for logging webhook events related to orders.

- **Fields**:
  - `payment_intent_id`: Stores the payment intent ID.
  - `received_at`: Records when the event was received.
  - `payload`: Stores the webhook payload.
  - `header`: Stores the webhook header.
  - `status`: Stores the status of the webhook event.
  - `event_type`: Stores the type of the webhook event.
- **Relationships**:
  - `order`: Optionally links to an Order model, can be set to NULL on order deletion.

## Address Model

Represents user addresses.

- **Fields**:
  - `address_type`: Specifies the type of address (e.g., billing or shipping).
  - `first_name`: Stores the user's first name.
  - `last_name`: Stores the user's last name.
  - `email`: Stores the user's email address.
  - `phone_number`: Stores the user's phone number.
  - `address_line1`: Stores the address.
  - `address_line2`: Stores additional address details.
  - `city`: Stores the city.
  - `state`: Stores the state.
  - `postal_code`: Stores the postal code.
- **Relationships**:
  - `user`: Links to the User model.

## EmailConfirmationToken Model

Represents email confirmation tokens for verifying user's email addresses.

- **Fields**:
  - `token`: Stores the email confirmation token.
- **Relationships**:
  - `user`: Links to the User model.

## Order Model

Represents orders placed by users.

- **Fields**:
  - `product_cost`: Stores the cost of the product.
  - `shipping_cost`: Stores the shipping cost.
  - `total_amount`: Stores the total amount of the order.
  - `status`: Stores the order status.
  - `payment_status`: Stores the payment status.
  - `payment_intent_id`: Stores the payment intent ID.
  - `created_at`: Records when the order was created.
  - `updated_at`: Records when the order was updated.
  - `tracking_number`: Stores the tracking number.
  - `tracking_company`: Stores the tracking company.
- **Relationships**:
  - `user`: Links to the User model.
  - `shipping_address`: Links to the Address model for shipping.
  - `billing_address`: Links to the Address model for billing.

## OrderItem Model

Represents items within an order.

- **Fields**:
  - `price`: Stores the price of the item.
  - `quantity`: Stores the quantity of the item.
  - `shipping_cost`: Stores the shipping cost of the item.
- **Relationships**:
  - `order`: Links to the Order model.
  - `product`: Links to the Product model.
  - `seller`: Links to the User model.
- **Methods**:
  - `get_total_item_price()`: Calculates the total price for the item.
  - `get_total_item_price_with_shipping()`: Calculates the total price for the item including shipping.

## PasswordResetToken Model

Represents password reset tokens.

- **Fields**:
  - `token`: Stores the password reset token.
  - `created_at`: Records when the token was created.
  - `is_used`: Indicates if the token has been used.
- **Relationships**:
  - `user`: Links to the User model.
- **Methods**:
  - `is_expired()`: Checks if the token has expired.


## User Model (CustomUser)

Represents users within the application with custom fields and behavior.

- **Fields**:
  - `email`: Stores the user's email and is used as the unique identifier for login.
  - `first_name`: Stores the user's first name.
  - `last_name`: Stores the user's last name.
  - `username`: Stores the user's username.
  - `date_joined`: Records when the user account was created.
  - `is_active`: Indicates whether the user's account is active.
  - `is_staff`: Indicates whether the user can access the admin site.
  - `stripe_account_id`: Stores the Stripe account ID if the user has connected a Stripe account.
  - `is_stripe_verified`: Indicates whether the user's Stripe account has been verified.
  - `balance`: Stores the user's balance for transactions within the application.

- **Methods**:
  - `create_user(email, password, **extra_fields)`: Creates a new user with the given email and password.
  - `create_superuser(email, password, **extra_fields)`: Creates a new superuser with the given email and password.
  - `__str__()`: Returns the user's email.

These models are visually represented by the ERD below:

![ERD](docs/db-schema.png)

Note: The ERD modeling tool only allows up to 10 models to be displayed at a time.

## Features

### Account Creation & Login

* User can create an account via email
* User can create an account using Google SSO
* User can login via email
* User can login via SSO

User stories: 1, 2, 18, 20, 19


[Watch the Video](https://www.loom.com/share/f1c2cc65b1fa42708041394d23f55129?sid=ff9d6956-d7fc-4e7a-84fd-ce820427d003)

### Password Reset

* Users can reset their password if they forget it

[Watch the Video](https://www.loom.com/share/92aaceb7549b47d29293fe0cf1489d43?sid=81db6b9f-f566-404f-bafd-73592ba47017)

User stories 15, 21

### List item for sale

* Users have to have an account to list a product
* Users have to have connected a Stripe account to list a porduct or they will not be able to get paid
* Users have to choose spefic categories and brands from a predetermined data set
* Users just need a single form to list

User stories 4, 5, 6, 7, 

[Watch the Video](https://www.loom.com/share/aaa662167d904660adce13185f4ae45f?sid=dab718ef-ffb9-49d1-832d-26ebae015893)

### Seller and Account Area

* View products listed for sale
* Check is product has been sold
* View past sales

User stories 3, 9, 13

[Watch the Video](https://www.loom.com/share/59607f5e429a433cbe7823561ace51a5?sid=22dc6d67-e707-40cb-b3ce-2bbbb201679c)

### Selling Management

* See where to ship an order
* Input tracking information
* Mark order as dispatched
* Contact buyer in case of an issue
* Refund order if necessary
* Edit products if not sold

User stories 8, 10, 11, 14, 17

[Watch the Video](https://www.loom.com/share/f6206b4b263e41b7a3e95c7eabdf345a?sid=07440ff6-bc11-407b-b3b1-ea82bd1ab509)

### Buying and Selling Emails

* Once an order has been placed, the buyer receives an email notification
* Once an order has been placed, the seller receives an email notification

User story 16

[Watch the Video](https://www.loom.com/share/5f0b661b46374919abed97fe4908aa33?sid=77631aca-9043-4c0d-ac48-9df026ad0f13)



### Contact Page

* Buyers or sellers can contact sell your tackle to help solve any order related or platform related issues

[Watch the Video](https://www.loom.com/share/c11fb73716ce4c689ab3dcf8ceb5447e?sid=a62784c1-ee4e-4d01-a2bb-242b7b18cc80)

User stories 12, 26

### Delete products

* I can delete a product as a seller if it has not been sold
* Double optin for delete so as to not delete a product my accident

[Watch the Video](https://www.loom.com/share/5a7a15dc706047f993ec7add82b1d0d7?sid=d125b8c8-d8c8-4420-bdc8-af6f015e034e)

User story 14

### Buyer Area

* View purchases
* See tracking once shipped

[Watch the Video](https://www.loom.com/share/ef4a6378aafa448bbdfdbf43345ff0d0?sid=9001265e-fa55-4e1e-93fd-bc7271649b2a)

User stories 21, 22, 25

### Cart & Checkout Page

* View items in cart and shipping totals before purchasing
* Input shipping and billing address. If addresses are the same then no need to input twice
* If you are logged in it will retrieve last shipping & billing information
* Different payment options - Apple Pay, Google Pay, Credit Card, Paypal

[Watch the Video](https://www.loom.com/share/986b065b59f944dfb213efb137805c6b?sid=61381892-48cc-4770-97bd-f41e36ea3a79)

User Stories 23, 24

### Admin Dashboard

* View and manage orders
* View and manage users
* View and manage products
* Refund orders on behalf of sellers

[Watch the Video](https://www.loom.com/share/c874b54711c64f5fb0ed2b222d345d3a?sid=b4553a6b-a614-46f6-abbe-e24af9ec36ed)

User Stories 27, 28, 29 30


## Technologies Used

### Languages and Frameworks

* HTML
* CSS
* Javascript
* Python
* Django

### Libraries and Tools

- **Am I Responsive**: Tool for checking responsiveness of web designs across different devices.
- **AWS S3 Bucket**: Cloud storage for storing files and assets on Amazon Web Services.
- **Balsamiq**: Rapid wireframing tool for working faster and smarter in design.
- **Bootstrap**: Front-end framework for developing responsive and mobile-first websites.
- **Cloudinary**: Cloud-based image and video management service.
- **Favicon.io**: Tool for creating website favicons.
- **Chrome Dev Tools**: Built-in Google Chrome browser tools for web developers.
- **Font Awesome**: Font and icon toolkit based on CSS and Less.
- **Git**: Distributed version control system for tracking source code changes.
- **GitHub**: Hosting and version control service using Git.
- **Google Fonts**: Library of free licensed font families.
- **Heroku Platform**: Cloud platform as a service supporting various programming languages.
- **jQuery**: Fast, small, and feature-rich JavaScript library.
- **Postgres via neon.tech**: Powerful, open-source object-relational database system.
- **Stripe**: Online payment processing platform.
- **AWS SES**: Amazon Simple Email Service for cloud-based email sending.
- **Django Allauth**: Integrated Django applications for authentication and social account integration.
- **Django Crispy Forms**: Django app for DRY rendering of forms.
- **Django CSP**: Adds Content Security Policy headers to Django applications.
- **Django Messages**: Framework for displaying one-time notification messages to users.
- **Pillow**: Python Imaging Library adding image processing capabilities.
- **Psycopg2**: PostgreSQL adapter for Python.
- **Python-dotenv**: Reads key-value pairs from `.env` file and sets them as environment variables.
- **Requests**: Elegant and simple HTTP library for Python.
- **Requests OAuthlib**: OAuthlib implementation for Python Requests.
- **Whitenoise**: Static file serving for Python web apps.
- **Boto3**: Library for direct access to AWS services.
- **Gunicorn**: Python WSGI HTTP Server for UNIX.
- **Mailjet REST**: Tool for sending, tracking, and delivering emails.
- **Babel**: Toolchain for converting ECMAScript 2015+ code into a backward-compatible version of JavaScript.
- **Crispy-Bootstrap5**: Integrates Django Crispy Forms with Bootstrap 5.


## Validation

### HTML

Using The W3C Markup Validation Service

* <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fwww.sellyourtackle.co.uk%2F">Index</a>
* <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fwww.sellyourtackle.co.uk%2Fauth%2Flogin%2F">Login</a>
* <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fwww.sellyourtackle.co.uk%2Fauth%2Fsignup%2F">Sign Up</a>
* <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fwww.sellyourtackle.co.uk%2Fauth%2Fabout-us">About Us</a>
* <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fwww.sellyourtackle.co.uk%2Fauth%2Fcontact%2F">Contact Us</a>
* <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fwww.sellyourtackle.co.uk%2Fauth%2Fprivacy%2F">Privacy</a>
* <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fwww.sellyourtackle.co.uk%2Fauth%2Fterms%2F">Terms</a>
* <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fwww.sellyourtackle.co.uk%2Fauth%2Freset-password%2F#l330c17">Reset Password</a>
* <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fwww.sellyourtackle.co.uk%2Fproduct%2Fkorda-ajcket">Product Page</a>

<details>
<summary>Buying</summary>
<img src="docs/validation/buying-html-validation.png" alt="Buying HTML Validation">
</details>

<details>
<summary>Selling</summary>
<img src="docs/validation/selling-html-validation.png" alt="Selling HTML Validation">
</details>

<details>
<summary>Account Settings</summary>
<img src="docs/validation/account-settings-html-validation.png" alt="Account Settings HTML Validation">
</details>

<details>
<summary>Cart</summary>
<img src="docs/validation/cart-html-validation.png" alt="Cart HTML Validation">
</details>

<details>
<summary>Checkout</summary>
<img src="docs/validation/checkout-html-validation.png" alt="Checkout HTML Validation">
</details>

<details>
<summary>Order Page Buyer</summary>
<img src="docs/validation/buyer-order-html-validation.png" alt="Order Page Buyer HTML Validation">
</details>

<details>
<summary>List Product</summary>
<img src="docs/validation/list-product-html-validation.png" alt="List Product HTML Validation">
</details>

<details>
<summary>Seller Product Page Not Sold</summary>
<img src="docs/validation/seller-product-page-not-sold-html-validation.png" alt="Seller Product Page Not Sold HTML Validation">
</details>

<details>
<summary>Seller Product Page Sold</summary>
<img src="docs/validation/seller-product-page-sold-html-validation.png" alt="Seller Product Page Sold HTML Validation">
</details>

<details>
<summary>Shop</summary>
<img src="docs/validation/seller-product-page-sold-html-validation.png" alt="Shop HTML Validation">
</details>



### Accessibility

Accessibility of the website was tested using the WAVE web accessibility evaluation tool.

<details>
<summary>Index</summary>
<img src="docs/validation/index-accessibility.png" alt="Index Accessibilty Score">
</details>

<details>
<summary>Login</summary>
<img src="docs/validation/login-accessibility.png" alt="Login Accessibility Score">
</details>

<details>
<summary>Sign Up</summary>
<img src="docs/validation/signup-accessibility.png" alt="Sign Up Accessibility Score">
</details>

<details>
<summary>About Us</summary>
<img src="docs/validation/aboutus-accessibility.png" alt="About Us Accessibility Score">
</details>

<details>
<summary>Contact Us</summary>
<img src="docs/validation/contactus-accessibility.png" alt="Contact Us Accessibility Score">
</details>

<details>
<summary>Privacy</summary>
<img src="docs/validation/privacy-accessibility.png" alt="Privacy Accessibility Score">
</details>

<details>
<summary>Terms</summary>
<img src="docs/validation/terms-accessibility.png" alt="Terms Accessibility Score">
</details>

<details>
<summary>Reset Password</summary>
<img src="docs/validation/resetpassword-accessibility.png" alt="Reset Password Accessibility Score">
</details>
<details>

<summary>Buying</summary>
<img src="docs/validation/buying-accessibility.png" alt="Buying Accessibility Score">
</details>

<details>
<summary>Selling</summary>
<img src="docs/validation/selling-accessibility.png" alt="Selling Accessibility Score">
</details>

<details>
<summary>Account Settings</summary>
<img src="docs/validation/account-settings-accessibility.png" alt="Account Settings Accessibility Score">
</details>

<details>
<summary>Cart</summary>
<img src="docs/validation/cart-accessibility.png" alt="Cart Accessibility Score">
</details>

<details>
<summary>Checkout</summary>
<img src="docs/validation/checkout-accessibility.png" alt="Checkout Accessibility Score">
</details>

<details>
<summary>Order Page Buyer</summary>
<img src="docs/validation/buyer-order-accessibility.png" alt="Order Page Buyer Accessibility Score">
</details>

<details>
<summary>List Product</summary>
<img src="docs/validation/list-product-accessibility.png" alt="List Product Accessibility Score">
</details>

<details>
<summary>Seller Product Page Not Sold</summary>
<img src="docs/validation/seller-product-page-not-sold-accessibility.png" alt="Seller Product Page Not Sold Accessibility Score">
</details>

<details>
<summary>Seller Product Page Sold</summary>
<img src="docs/validation/seller-product-page-sold-accessibility.png" alt="Seller Product Page Sold Accessibility Score">
</details>

<details>
<summary>Product Page</summary>
<img src="docs/validation/product-page-accessibility.png" alt="Product Page Accessibility Score">
</details>

<details>
<summary>Shop</summary>
<img src="docs/validation/shop-accessibility.png" alt="Shop Accessibility Score">
</details>


### CSS

Tested using the W3C Css Validation Service tool.

<details>
<summary>CSS Validation</summary>
<img src="docs/validation/css-validation.png" alt="CSS Validation">
</details>

### Javascript

Tested using the JSHint JS Validation Service.

checkout.js - the undefined Stripe variable is called using the <script src="https://js.stripe.com/v3/"></script> tag in the HTML of the checkout page. The unused 'moveToPaymentStep' is used in the move to payment button in the HTML of the checkout page:

  <!-- <button type="button" class="btn btn-outline-main mt-3" onclick="moveToPaymentStep()">Move to
      Payment</button> !-->

<details>
<summary>Checkout JS</summary>
<img src="docs/validation/checkout-js-validation.png" alt="Checkout JS">
</details>

<details>
<summary>General JS</summary>
<img src="docs/validation/general-js-validation.png" alt="General JS">
</details>

<details>
<summary>List Products JS</summary>
<img src="docs/validation/listProducts-js-validation.png" alt="List Products JS">
</details>

<details>
<summary>Signup JS</summary>
<img src="docs/validation/signup-js-validation.png" alt="Signup JS">
</details>

### Python

CI Python Linter was used to check for PEP8 compliance.

#### Admin App

<details>
<summary>admin.py</summary>
<img src="docs/validation/admin_pep.png" alt="Admin.py PEP">
</details>


#### Auth App

<details>
<summary>email.py</summary>
<img src="docs/validation/email_pep.png" alt="email.py PEP">
</details>

<details>
<summary>forms.py</summary>
<img src="docs/validation/forms_auth_pep.png" alt="forms.py PEP">
</details>

<details>
<summary>models.py</summary>
<img src="docs/validation/models_auth_app_pep.png" alt="models.py PEP">
</details>

<details>
<summary>stripe.py</summary>
<img src="docs/validation/stripe_pep.png" alt="stripe.py PEP">
</details>

<details>
<summary>views.py</summary>
<img src="docs/validation/views_auth_app_pep.png" alt="views.py PEP">
</details>

<details>
<summary>test.py</summary>
<img src="docs/validation/test_auth_app_pep.png" alt="test.py PEP">
</details>

<details>
<summary>urls.py</summary>
<img src="docs/validation/urls_auth_app_pep.png" alt="urls.py PEP">
</details>


#### Tackle App

<details>
<summary>forms.py</summary>
<img src="docs/validation/forms_tackle_pep.png" alt="forms.py PEP">
</details>


<details>
<summary>models.py</summary>
<img src="docs/validation/models_tackle_pep.png" alt="models.py PEP">
</details>

<details>
<summary>test.py</summary>
<img src="docs/validation/test_tackle_pep.png" alt="test.py PEP">
</details>

<details>
<summary>urls.py</summary>
<img src="docs/validation/urls_tackle_pep.png" alt="urls.py PEP">
</details>

<details>
<summary>views.py</summary>
<img src="docs/validation/views_tackle_pep.png" alt="views.py PEP">
</details>

## Testing

### Automated unit testing

* Testing using Django unittest
* Two test files can be found in the tackle and auth app
* To run call python manage.py test in the terminal

#### Models Tests
- **CategoryModelTest**
  - Tests the creation of a Category instance.

#### Form Tests
- **CheckoutFormTest**
  - Validates the Checkout form with correct data input.
- **ContactSellerFormTest**
  - Validates the Contact Seller form with correct data input.
- **CustomUserSignupFormTest**
  - Validates the Custom User Signup form with both valid and invalid data input.
- **ContactFormTest**
  - Validates the Contact form with correct data input.
- **PasswordResetRequestFormTest**
  - Validates the Password Reset Request form with correct data input.
- **SetNewPasswordFormTest**
  - Validates the Set New Password form with correct data input.

#### View Tests
- **SearchViewTest**
  - Tests the search view for correct HTTP response.
- **ShopViewTest**
  - Tests the shop view for correct HTTP response.
- **ConfirmEmailViewTest**
  - Tests email confirmation process and user activation.
- **BuyingViewTest**
  - Tests the buying view for correct HTTP response and template usage.

#### CustomUser Model Test
- **CustomUserModelTest**
  - Tests the creation of a CustomUser instance.

#### Stripe Integration Tests
- **StripeIntegrationTest**
  - Tests the Stripe integration, including account link creation, account retrieval, and user Stripe verification.


<details>
<summary>Unit Test Results</summary>
<img src="docs/testing/unittests.png" alt="unit testing">
</details>

All tests pass with "OK" status

### Manual Testing

#### Selling

1. **Login and create an account**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Navigate to 'Login/Register' | Registration/Login page loads | Works as expected |
   | Attempt to register a new account | Account is created and user is logged in | Works as expected |

[Watch the Video](https://www.loom.com/share/5111b3286f41424c909dab23e112ffe5?sid=e8e7b1e4-bdbb-43a4-bd91-04a5e0e2d012)   

2. **Use Google as an SSO**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Click on 'Login with Google' | Google SSO process initiates | Works as expected |
   | Complete Google SSO process | User is logged in through Google account | Works as expected |

[Watch the Video](https://www.loom.com/share/4fa3f6b627804ec7abef1d0bd66f2886?sid=5ee134e2-010d-4f78-bd35-51a6d9c0ffee)   

3. **Change their username**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Navigate to user profile/settings | Profile/Settings page loads | Works as expected |
   | Update username and save changes | Username is updated successfully | Works as expected |

[Watch the Video](https://www.loom.com/share/79e922e803904514978cd5e15f4b9cf2?sid=101cadf8-5db2-40be-8fd8-27b267ddd7d7)  

4. **Single form to list tackle**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Navigate to 'List New Tackle' form | Tackle listing form loads | Works as expected |
   | Fill out the form and submit | New tackle listing is created | Works as expected |

[Watch the Video](https://www.loom.com/share/932bfbed8093427684ffc94ecef667bb?sid=02c86b23-9d8c-4e45-8175-8c67c3780e6d)    

5. **Predefined brands and categories to speed up listing**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Open the listing form | Form with predefined options for brands and categories is visible | Works as expected |
   | Select options from predefined lists and submit | Listing is created with selected predefined options | Works as expected |

[Watch the Video](https://www.loom.com/share/50563ea829b8451fac8f7f24baf06925?sid=86f13c63-5e6b-4a9e-bf4f-ca5a5513fa11)    

6. **Ability to upload images to product, regardless of size**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Navigate to product listing form | Product listing form is accessible | Works as expected |
   | Upload image of any size and submit | Image is uploaded successfully | Works as expected |

[Watch the Video](https://www.loom.com/share/2098f23e82934bd99cdd1fa41f43578e?sid=966e507b-ed15-4471-bb87-290b12589e02)     

7. **Connect bank account to get paid**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Navigate to payment settings | Payment settings page loads | Works as expected |
   | Connect a bank account | Bank account is connected successfully | Works as expected |


[Watch the Video from the 1:07 mark](https://www.loom.com/share/aaa662167d904660adce13185f4ae45f?sid=dab718ef-ffb9-49d1-832d-26ebae015893)   

8. **Message buyers in case of order issues**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Navigate to the order page | Order details page loads | Works as expected |
   | Send message to buyer | Message is sent successfully | Works as expected |

[Watch the Video from the 1:35 mark](https://www.loom.com/share/f6206b4b263e41b7a3e95c7eabdf345a?sid=8a1d7d43-120b-40cc-b73b-09f42e889908)    

9. **View past sales**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Navigate to sales history | Sales history page loads | Works as expected |
   | View list of past sales | Past sales are displayed correctly | Works as expected |

[Watch the Video](https://www.loom.com/share/336b03df9b6d4e7786a85e33d6282b83?sid=cab484de-e734-490f-9023-13194c5b736b)   


10. **See shipping information when an item is sold**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Navigate to sold item details | Sold item details page loads | Works as expected |
   | View shipping information | Shipping information is displayed correctly | Works as expected |

[Watch the Video](https://www.loom.com/share/c5814322472241e98bc2dfc3ffc41c5b?sid=4b59c7fa-cef5-4e90-bfae-05ef99d64198)   

11. **Input tracking details**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Navigate to sold item details | Sold item details page loads | Works as expected |
   | Input tracking details and update | Tracking details are updated and are visible to the buyer | Works as expected |

[Watch the Video](https://www.loom.com/share/c5814322472241e98bc2dfc3ffc41c5b?sid=4b59c7fa-cef5-4e90-bfae-05ef99d64198)   

12. **Contact page for order disputes**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Navigate to the contact page | Contact page loads | Works as expected |
   | Submit an order dispute | Order dispute is submitted successfully | Works as expected |

[Watch the Video](https://www.loom.com/share/c11fb73716ce4c689ab3dcf8ceb5447e?sid=34162feb-4ad9-470f-8c85-ba32dc75de6b)      

13. **Responsive design for checking listings on the go**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Access website on a mobile device | Website is responsive and usable on mobile | Works as expected |

[Watch the Video](https://www.loom.com/share/b6be86fdff7f462b9db37cff8bd073a3?sid=fdcf432b-d28a-47e9-bfd1-10c369439d6c)     

14. **Edit or delete products unless sold**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Navigate to product details | Product details page loads | Works as expected |
   | Edit or delete the product | Product is edited or deleted successfully | Works as expected |

[Watch the Video](https://www.loom.com/share/5b41f0d5bc8e430fb6bed9e7e07cb8e9?sid=267da2b9-a440-462b-83f4-af0887665280)   

15. **Reset password in case of forgetting it**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Click on 'Forgot Password' | Password reset form/page loads | Works as expected |
   | Submit email for password reset | Password reset instructions are sent to email | Works as expected |

[Watch the Video](https://www.loom.com/share/92aaceb7549b47d29293fe0cf1489d43?sid=f5628ae3-3e37-4296-88f7-e600933402810)    

16. **Email notification once item is sold**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Sell an item | Email notification about the sale is received | Works as expected |

[Watch the Video](https://www.loom.com/share/5f0b661b46374919abed97fe4908aa33?sid=d8864154-9a8b-4df3-aaab-63a316bbb9f5)   

17. **Refund orders if unable to ship**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Navigate to sold item details | Sold item details page loads | Works as expected |
   | Initiate a refund | Refund is processed successfully | Works as expected |

The refund process sends a notification to Stripe, once Stripe has refunded the amount requested it sends a webhooks back to the database with an updated financial status to "refunded". Once that webhook is received the order status is updated to "refunded".

[Watch the Video](https://www.loom.com/share/178bbcea24d549eba988d421c594dc9b?sid=136bc6ab-0e93-431f-96a2-86d2d816fde3)   

#### Buying

18. **Login and create an account**
   
   *Same steps as in Selling section.*

19. **Use Google as an SSO**
   
   *Same steps as in Selling section.*

20. **Reset password in case of forgetting it**
   
   *Same steps as in Selling section.*

21. **Area to view past orders**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Navigate to user profile | Profile page with order history loads | Works as expected |
   | View order history | List of past orders is displayed | Works as expected |

[Watch the Video](https://www.loom.com/share/4541245c92a4482ebcf15c3d00ef39f2?sid=5ed4da74-9605-477e-92f9-5a7e701d918f)     

22. **See tracking information once shipped**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Navigate to purchased item details | Purchased item details page loads | Works as expected |
   | View tracking information | Tracking information is displayed correctly | Works as expected |

[Watch the Video](https://www.loom.com/share/c8f59eca66e94f9fb24378e4bcb62d4b?sid=5d2ad7fa-53dd-41d2-bf57-1759d1a0f8c5)   

23. **Negate the need for duplicate address inputs at checkout**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Proceed to checkout | Checkout page loads with pre-filled address details | Works as expected |

[Watch the Video](https://www.loom.com/share/7da6cd8373d64ab0b51c8cb7dc85f7a6?sid=32221143-f9b8-4325-98c3-39a3f32ee8cd)      

24. **Different payment options at checkout**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Navigate to checkout | Checkout page loads | Works as expected |
   | Select different payment options | Payment options are selectable and functional | Works as expected |

[Watch the Video](https://www.loom.com/share/c0292c72c53d4b058726082b8a3db1af?sid=f5d7d738-4874-4afe-84b7-ef208d33113c) 


25. **Ability to message seller with questions**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Navigate to a product page | Product page loads | Works as expected |
   | Send a message to the seller | Message is sent successfully | Works as expected |

  [Watch the Video](https://www.loom.com/share/d0bfd89e6f6c474fba7f6b27ddd25fc3?sid=b4bea4e1-51e7-4282-b3be-069be34a8329)  

26. **Ability to message site admins for order help**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Navigate to the contact page | Contact page loads | Works as expected |
   | Send a message to site admins | Message is sent successfully | Works as expected |

Same as point 12   

### Admin/Site Owner

All of these tests can be viewed in one video below

[Watch the Video](https://www.loom.com/share/8cb5e1767a2741b3aa68ca36ef6ce812?sid=d7e130ee-92cd-413a-8c5b-2e9200727704)  

27. **View and manage orders in admin dashboard**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Access admin dashboard | Admin dashboard is accessible | Works as expected |
   | View and manage orders | Orders are viewable and manageable | Works as expected |

28. **View and manage users in admin dashboard**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Access admin dashboard | Admin dashboard is accessible | Works as expected |
   | View and manage user accounts | User accounts are viewable and manageable | Works as expected |

29. **View and manage products in admin dashboard**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Access admin dashboard | Admin dashboard is accessible | Works as expected |
   | View and manage products | Products are viewable and manageable | Works as expected |

30. **Refund orders on behalf of sellers**
   
   **Step** | **Expected Result** | **Actual Result**
   ---------|---------------------|----------------
   | Access admin dashboard, navigate to orders | Orders section in admin dashboard loads | Works as expected |
   | Initiate a refund for an order | Refund is processed successfully | Works as expected |

### Device Testing & Browser Compatibility

Using the Chrome extension "Mobile simulator, responsive testing tool" the platform has been tested on:

* Samsung Galaxy S20
* Galaxy Z flip
* Apple iPhone 5
* Apple iPhone 11
* Apple iPhone 13 pro
* iPad Mini
* iPad Pro 11
* Microsoft Surface Duo
* Galaxy S7 Tab
* Macbook Air

and the following browsers

* Chrome
* Firefox
* Safari
* Bing


## Commission

A variable has been added to the settings.py "STRIPE_COMMISSION_RATE". This is current set to 10% but is not called. To implement this the function handle_payment in the stripe.py file inthe auth_app needs to be changed from:

        for item in cart:
            order_item = OrderItem.objects.create(
                order=order,
                product_id=item["product_id"],
                price=item["price"],
                quantity=item["quantity"],
                seller=item["product"].user,
            )

            stripe.Transfer.create(
                amount=int(order.total_amount * 100),
                currency="gbp",
                destination=order_item.seller.stripe_account_id,
                metadata={
                    "user_email": user.email,
                    "user_first_name": user.first_name,
                    "user_last_name": user.last_name,
                },
            )

to:

        for item in cart:
            # Calculate the commission and the amount to be transferred
            commission_amount = item['price'] * item['quantity'] * settings.STRIPE_COMMISSION_RATE
            seller_amount = int(item['price'] * item['quantity'] * 100 * (1 - settings.STRIPE_COMMISSION_RATE))

            # Create the order item and save the commission
            order_item = OrderItem.objects.create(
                order=order,
                product_id=item['product_id'],
                price=item['price'],
                quantity=item['quantity'],
                seller=item['product'].user,
                commission=commission_amount
            )

            # Create a Stripe Transfer to the seller
            stripe.Transfer.create(
                amount=seller_amount,
                currency='gbp',
                destination=order_item.seller.stripe_account_id,
                metadata={
                    'user_email': user.email,
                    'user_first_name': user.first_name,
                    'user_last_name': user.last_name
                }
            )

This will take into account the numerical value set in the commission variable and transfer the commission amount to the admin's Stripe account.      




## Security

The following security measures are in place:

1. All passwords and security keys are stored as environment variable in Heroku
2. GitGuardian monitors the Github repo for security issues
3. OAuth callback urls and authorised Javascript origins for SSO are setup to only accept requests from *.sellyourtackle.co.uk
4. Passwords are stored as hashes in the database, to prevent password leaks in the event of a database hack
5. Certain pages are only accessible to logged in users, relative to their account i.e. buying and selling pages, listing tackle for sale
6. Admin area is only accessible to Django super users

## Bug Fixes

| **Bug** | **Fix** |
| ------- | ------- |
| Checkout issue where `client_secret` was not being passed to Stripe | Modified the checkout process to correctly pass the `client_secret` to Stripe for secure transactions |
| Edit product image upload issue where `process_image` function returned a tuple | Updated the `process_image` function to handle image processing correctly and return the appropriate data format |
| Undefined user request in the buying view | Implemented a check to ensure user requests are defined and valid in the buying view |
| Image upload on list tackle returning a tuple | Modified the image upload function to correctly handle and return image data, resolving the tuple return issue |
| No defined key for paginating orders on selling and buying page | Implemented pagination keys to correctly handle order lists on both selling and buying pages |
| Blank condition for product status on seller product page | Added checks to handle blank conditions and display appropriate product status |
| Set empty condition statement on list product page | Established condition statements to handle and display content correctly when the list is empty |
| JavaScript issue where it could not find address element on checkout page | Corrected the JavaScript code to properly locate and interact with the address element during checkout |
| Image upload to product RGB(A) issue and messaging when product is deleted | Fixed the image upload function to support RGB(A) formats and added user feedback for product deletions |
| Bug where user password was not being saved on signup | Modified the user registration process to ensure passwords are correctly saved and encrypted |
| Sold/unsold URL redirects not working in the selling area | Corrected URL routing to ensure proper redirection between sold and unsold product views in the selling area |
| Issue with custom username not being created when user doesn't exist | Implemented a fallback mechanism to create custom usernames when default user data is unavailable |

Console Errors:

The checkout page dispays these errors and warnings in the console:

<details>
<summary>Console Errors</summary>
<img src="docs/validation/checkout-js-errors.png" alt="Console Errors">
</details>

This is due to the Stripe being set to test mode within the account. To fix these, it the settings would have to be changed to live mode.

## Database Indexing

The column for the product name has been indexed to improve serach result speeds

## Planned Improvements For The Next Build

1. More email notifications, i.e. for when an order is refunded notify buyer
2. Have the tracking on the actual order page as well as the order table
3. Offer partial refunds for orders


## Heroku Deployment

For the official Heroku deployment documentation, please visit <a href="https://devcenter.heroku.com/articles/git">here</a> 

1. Step One

Make sure your github repo for the build is up to update. You will be automatically deploying the latest code from your github repo. Items to confirm:

* Your requirement.txt file contains all the dependencies needed for the project. Run pip freeze > requirements.txt in the terminal if unsure
* You have migrated all changed to the database before deploying. Run python manage.py makemigrations and python manage.py migrate in the terminal
* Check all passwords and other sensitive information are stored in a .env file and are called throughout the build as environment variables, not hardcoded anywhere
* You have a Procfile in the root of the project with the following content: web: gunicorn sellyourtackle.wsgi 
* You are connected to an external postgres database and have the necessary environment variables set in the settings.py file for connecting to it. This build is using a Serverless Postgres DB hosted at www.neon.tech 
* Ensure debug is set to "FALSE" in the settings.py file


2. Step Two

Visit <a href="https://id.heroku.com/login">Heroku</a> and login. If you do not have an account create one.

<details>
<summary>Login</summary>
<img src="docs/heroku/login.png" alt="Heroku Login">
</details>

3. Step 3

Create a new app, choose a name and the region closest to where the majority of your users will sit


<details>
<summary>Create App</summary>
<img src="docs/heroku/create-app.png" alt="Heroku create app">
</details>


4. Step 4

Within the new app, go to the Settings tab and navigate to Config Vars. Add the necessary environment variables from the .env file here


<details>
<summary>Set Config Vars</summary>
<img src="docs/heroku/config_vars.png" alt="Heroku config vars">
</details>


5. Next go to the "Deploy" tab. Click on "Connect to GitHub" and select your repo. Click on "Enable Automatic Deploys" and then "Deploy Branch"

<details>
<summary>Deployment</summary>
<img src="docs/heroku/config_vars.png" alt="Heroku deployment">
</details>

6. Monitor logs

The application will then attempt to build and deploy using the Github sourcecode. You can monitor the logs by going to the "More" tab in the top right and clicking on "View logs". If it fails for any reason you will be able to debug from there

<details>
<summary>Logs</summary>
<img src="docs/heroku/logs.png" alt="Heroku logs">
</details>

### Forking the GitHub Repository

1. Go to the GitHub repository https://github.com/ouzifeng/sellyourtackle
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.
   
### Making a Local Clone

1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <span>https://</span>github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

## Credits

### Images

Images used were sourced from www.tackletarts.uk 

### Code

* Bootstrap was used wherever possible to speed up development. Examples of this are the navigation menu
* AWS S3 bucket is used to store and serve product images
* Cloudflare is being used as a CDN and for security monitoring
* Mailjet is being used as the SMTP service provider
* Stripe is being used as the payment facilitator 

## Testing

For testing the checkout, use the following credit card details to make a purchase:

When testing interactively, use a card number, such as 4242 4242 4242 4242. Enter the card number in the Dashboard or in any payment form.

Use a valid future date, such as 12/34.
Use any three-digit CVC (four digits for American Express cards).
Use any value you like for other form fields.

Thus is Stripe's default test payment credit card. While Google and Paypal will allow checkout, they do not function the same unless the Stripe account is set to live mode.

## Acknowledgements

### Special thanks to the following:
- My Mentor Mo Shami