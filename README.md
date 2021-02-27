# Custom Candles

<hr>


### Code Institute / Full Stack Frameworks with Django Milestone Project

The brief was to build a full-stack site based around business logic used to control a centrally-owned dataset.The site needed an authentication mechanism and needed to provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

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
  - HTML5
  - CSS3
  - Javascript
  - Python
  - Json

<hr>

### Frameworks, Libraries & Programs Used
  - Bootstrap 4.4.1:
  Bootstrap was used to assist with the responsiveness and styling of the website.
  - jQuery:
  jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
  - Git:
  Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
  - GitHub:
  GitHub is used to store the project's code after being pushed from Git.
  - Django:
  Django was used as the web framework for the site.
  - Heroku: <br>
  Heroku was used to deploy the site and to host the database
  - Stripe Payments:
  Stripe templates were used for payment processing and order management. 
  - Canva:
  Canva was used to create the logo for the website.
  - Balsamiq:
  Balsamiq was used to create the wireframes during the design process.
  
<hr>

### Testing
  The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.
  W3C Markup Validator - Results
  W3C CSS Validator - Results
  
#### Testing User Stories from User Experience (UX) Section
User experience testing was documented here.

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
