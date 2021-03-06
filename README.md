# Custom Candles

<hr>
## Website Details

### URL
 - The website url is https://aoifem-custom-scents.herokuapp.com/

### Purpose

The brief was to build a full-stack site based around business logic used to control a centrally-owned dataset.The site needed an authentication mechanism and needed to provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

### Further Information

When testing payments in this application, please use the Stripe test card numbers available [here](https://stripe.com/docs/testing#cards) from the Stripe documents. During the testing of the site the card details that I used were:

- <strong>Card number:</strong> 4242 4242 4242 4242
- <strong>Expiry date:</strong> Any date in the future
- <strong>CV2 number:</strong> Any 3 digits
- <strong>ZIP:</strong> 42424
<hr>

### What is Custom Scents?

Custom Scents is a compant that offer a range of environmentally friendly and sustainable scented products that can be purchased on the site and allow users to chose teh scent that they want for any product that they chose. 
<hr>

### User Experience (UX)

### Business Goals:

The business goals of Custom Scents are:
  - To sell high quality, environmentally friendly and sustainable products.
  - To engage, promote and sell across all social media platforms.
  - To generate interest in their company through increased traffic to the site
  - Have customers return to the site and purchase more products.
 
### User Stories:
#### As the developer of the site:
  - I want to be able to showcase my ability to use Django frameworks and  integrate to stripe payments to create an e-commerce website. 
#### As a site customer I want to:
  - I want to be able to quickly understand the function of the site and see what products are on offer. 
  - I want to be able to view the range of products on offer on the site and choose my own scent for each product. 
  - I want to be able to understand the pricing information for the products I want and see the discounts and delivery charges applied. 
  - I want to be able to create a user account so that it will store previous purchase history.
  - Make a purchase on the site by way of card payment.
  - I want to view the site from any device (mobile, tablet, desktop).
  
<hr>

### Design

#### Colour Scheme
There are 4 main colours used for the site. The are: 
  - #f5f3ef - light beige
  - #f0ab20 - yellow
  - #ddcdc0 - darker beige
  - #642714 - brown

#### Typography
Bootstrap fonts are used throughout the site.

#### Imagery

#### Logo
The logo was created in canva.com and it uses the same colours as the site colour scheme. It contains the company name and an image of what the company deems their best selling product,  the candle. To increase brand awareness, teh logo is shown in the navbar and footer throughout the site. 
#### Jumbotron image
The homepage contains a large jumbotron with an image of a candle. The image is designed to invoke a feeling of calm so that the customer can get a feel for the calming nature of the products on offer. 

#### Wireframes
Home Page Wireframe - View
Mobile Wireframe - View


<hr>

### Features
  - Responsive on all device sizes
  - Stripe payment processing 
  - Profile and order management via heroku and django
  - User authentication and account management features
  - Amazon s3 is used to host static files and product images
  - Toasts that pop up when an action is performed and provide useful information to the user. 
  - Heroku was used to host the site and postgres was used to store the database information
  - Technologies Used

<hr>

### Languages Used
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
-   [Jinja](https://palletsprojects.com/p/jinja/)
-   [Json](https://www.json.org/json-en.html)

<hr>

### Frameworks, Libraries & Programs Used
1. [Bootstrap 4.4.1](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
2. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
3. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
4. [MongoDB](https://www.mongodb.com/cloud/atlas):  
    - MongoDB was used to store all data recodred for each user and each users workouts logged. 
5. [Canva:](https://www.canva.com/)
    - Canva was used to create the logo for the website.
7. jQuery:]
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
8. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
9. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
10. [Django:](https://www.djangoproject.com/)
    - Django was used as the web framework for the site.
11. [Heroku:](https://www.heroku.com/)
    - Heroku was used to deploy the site and to host the database
12. [Stripe Payments:](https://stripe.com/)
    - Stripe templates were used for payment processing and order management. 
13.  [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.
14. Other:
    - All other installed packages can be found in the sites [requirements.txt](https://github.com/aoifemurfe/custom_candles/blob/master/requirements.txt) file
  
<hr>

### Site Pages

#### Base Template
 
###### Navbar 
 
- The navbar header contains the main site navigataion links. The brand logo in the top left acts as a home button to bring the user back to the home page. The user can also select the view products link to view the products page with all the products sold.
 
- A logged out user can access the registration page or log in page through the user icon.
 
- A logged in user can access their profile dashboard or log out through the user icon.
 
- The user can view a price summary of their current orders underneath the bag icon. Clicking on the icon will bring them to their bag for a more detailed view.


###### Footer

The Footer contains all contact information for the company incuding email adress and social media links. 

#### Homepage

The home (Index) page is our primary landing page. The hompage is where the user first lands and it is used as the main selling and marketing section of the website. There is a banner just below the navbar with the lastest sales offer where a user can get $5 off their purchase when they buy 3 products. The jumbotron image shows a relaxing candle and contains a call to action button to allow the user to begin shopping the products on offer. 

Below the jumbotron is where they environmental and sustainable features of the products are outlined. This is to reenforce the company message of producing products ethically and sustainably. 

The homepage also contains some customer reviews that again reenforce the message of high quality, customisable and enviromentally friendly products.

#### Products Page

Products in the shop are displayed as thumbnail images with the product title category tag and price broken up by a horizontal line.When the user clicks on a product card, they are taken to the product details page of that selected product.

#### Products Detail Page

This page gives an in depth view of the product. The customer can select the scent and quantity that they would like to buy. The 'Keep Shopping' and 'Add To Bag' buttons are located below the product price and have a hover effect on them. When a user adds an item to their card a toast appears in the top right side of the screen with their bag details. 

#### Shopping Bag

The shopping bag page features a summary of all the items the user has added to their shopping cart.

- There is a line in the table for each item added to the card which lists the product image, product name, scent and price.
- The user has the ability to adjust the quantity in their cart. A user can also remove an item from their cart. When the quantity is updated. the subtotal will reflect the change.
- Cart total, delivery total, discount and grand total of the user's cart are at the bottom of the table. 
- The 'Secure Checkout' button proceedsto take the user to the payment screen operated by Stripe and it includes a lock image to reenforce the mesage of security. 

#### Checkout 

The checkoutpage contains a crispy form to allow the user to enter their billing and payment information. The payment template was taken from stripe. There is also an order summary to remind the user of what they are buying and clearly state how much will be charged to their card. 

#### Stripe

- Users can complete the checkout process by entering their card details.
- Payment is handled though the secure Stripe API.
- Once a user clicks to buy, a custom loader appears while the payment is processing and if a successful payment is made, the user is taken to the checkout success page.

#### Checkout Success

- An order confirmation email is then sent to the email provided by the user which contains all the information of their purchase(s).
- The checkout success page gives the customer all their order information.
- An order number is automatically generated on checkout.
- The user is invited to check out our deals page after checkout.

<hr>
### Features Left to Implement
Below are feature of the site that I would have liked to incorporate into the site had I not been subject to time constraints. 

###### Social Sign Up
I would liked to have used google and facebook information to sign up and register accounts using a customers google or facebook account. This would make it easier for customrs to register and log in. 

###### Create products with 2 scents
I would have liked for users to be able to select 2 scents for their products so that they could mix and match scents and make the products really customisable. 

###### Customer product reviews
I would have liked for customers to be able to leave reviews of products in the customer details page so that other customers could read and get an idea of the scents that are populaar. 

<hr>

### Testing
The lighthouse report at https://web.dev/measure/ was used to assess the website based on 4 categories
1. Performance
2. Accessability
3. Best Practise 
4. SEO

 - Lighthouse report - [Results](https://github.com/aoifemurfe/custom_candles/blob/master/static/images/Lighthouse_Report.pdf)
  
#### Testing User Stories from User Experience (UX) Section
#### As the developer of the site:
1.  I want to be able to showcase my ability to use Django frameworks and  integrate to stripe payments to create an e-commerce website. 
    -The website used django framework and stripe payments to create a functioning ecommerce website.
#### As a site customer I want to:
1.  I want to be able to quickly understand the function of the site and see what products are on offer. 
     - As described in the homepage section, the homepage quickly provides the customer with details about what is on offer and what the company customs scents has to    offer.  The navbar at the top shows the user easily each of the pages available to them and this dynamically changes based on whether the user has signed in or not. 
3.  I want to be able to view the range of products on offer on the site and choose my own scent for each product. 
     -  The homepage contains a call to action in the first card for the use to click the link to the registration page. The product and product details page show the user eash of the products and provide an easy to fill out form to cusomise the scent of the product the user is puchasing. 
5.  I want to be able to understand the pricing information for the products I want and see the discounts and delivery charges applied. 
     - The prices of each product are clearly listed on the products and product details page. There is a banner just below teh navbar with the special offer to entice the customer to buy more. The shopping bag and checkout page provide details of pricing for the products and the delivery and discount prices also.
7.  I want to be able to create a user account so that it will store previous purchase history.
     - The login and register page allow the user to create an account and log into their account. The user profile allows users to see their previous orders. 
9.  Make a purchase on the site by way of card payment.
     - The site used stripe and stripe webhooks to be able to make a payment securly on the website. 
11.  I want to view the site from any device (mobile, tablet, desktop).
     - The site uses bootstrap to be responsive on all devices. 
  

#### Further Testing
The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
A large amount of testing was done to ensure that all pages were linking correctly.
Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.
Known Bugs
 
<hr>

### Heroku
The project was deployed wit Heroku following the instruction detailed here
 
<hr>

### Database Models
 
When each app and its models were created and implemented, python manage.py makemigrations was run in the terminal to create the initial model package and python manage.py migrate was then used to apply the model to the database and create the table.
 
All models were created with Django's ability to auto-assign a Primary Key (ID).
 
###### User Model
 
The User model used is the standard one provided by Django.
 
###### scents Model
 
| Name        | Description | Field Type    |
| :---        |    :----:   |          ---: |
| Sku        | max_length=254, blank=True     | Charfield   |
| Name        | max_length=250     | Charfield   |
| Description       | blank    | TextField  |
 
###### products Model
 
| Name        | Description | Field Type    |
| :---        |    :----:   |          ---: |
| Sku        | max_length=254, blank=True     | Charfield   |
|Name       |max_length=254             | Charfield      |
|Image|blank=True | Image Field      |
| has_scent       | blank    | Many to many field  |
| Price        | max_digits=6, decimal_places=2     | DecimalField   |
 
###### Order Model
 
| Name        | Description | Field Type    |
| :---        |    :----:   |          ---: |
|Order Number|max_length=32, null=False, editable=False| Charfield   |
|User Profile|on_delete=models.SET_NULL,null=True, blank=True, related_name='orders'|ForeignKey|
|Full Name|max_length=50, null=False, blank=False| Charfield   |
|Email|max_length=254, null=False, blank=False|EmailField|
|Phone Number |max_length=20, null=False, blank=False| Charfield   |
|Country|blank_label='Country *', null=False, blank=False|CoutryField|
|Postcode|max_length=20, blank=True| Charfield   |
|Town or City|max_length=40, null=False, blank=False| Charfield      |
|Street Address 1|max_length=80, null=False, blank=False| Charfield   |
|Street Address 2|max_length=80, blank=True| Charfield      |
|County|max_length=80, blank=True| Charfield   |
|Date|auto_now_add=True| DateTimeField |
|Delivery Cost|max_digits=6, decimal_places=2, null=False, default=0| DecimalField   |
|Order Total|max_digits=10, decimal_places=2, null=False, default=0| DecimalField      |
|Grand Total|max_digits=10, decimal_places=2, null=False, default=0	| DecimalField  |
|Original Bag|null=False, blank=False, default=''| TextField|
|Stripe Pid|max_length=254, null=False, blank=False, default=''| Charfield      |
 
###### Order Item Model
 
| Name        | Description | Field Type    |
| :---        |    :----:   |          ---: |
|Order|null=False, blank=False, on_delete=models.CASCADE,related_name='lineitems'| ForeignKey  |
|Product|null=False, blank=False, on_delete=models.CASCADE| ForeignKey |
|Scent_one | max_length=99, blank=True | CharField   |
|Quantity | null=False, blank=False, default=0 | IntegerField |
|Line Item Total| max_digits=6, decimal_places=2, null=False, blank=False, editable=False|Decimal Field|
 

 
<hr>

### Credits
#### Code
Bootstrap4: Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.
Stripe Payments
Django web framework

#### Content
All content was written by the developer.
#### Media
All Images were created by the developer or taken from unsplash.com
#### Acknowledgements
My Mentor for continuous helpful feedback.
Tutor support at Code Institute for their support.
