**Pet-Zone Marketplace – Documentation**



---

## Table of Contents

1. Project Overview
2. Key Features
3. Technology Stack & Dependencies
4. Directory and File Structure
5. Data Storage Format (`Pets.txt`)
6. Flask Backend Application Setup
7. Route and Endpoint Documentation
8. HTML Templates Overview
9. Static Assets and File Management
10. Input Validation and Security
11. Testing and Quality Assurance
12. Deployment Instructions
13. SEO Optimization & Keywords

14. Author & License

---

## 1. Project Overview

The **Vendor Pet Marketplace** is a lightweight web platform where pet vendors can upload, showcase, and manage pets for sale. Visitors can browse listings, and administrators can control content from a simple backend panel. Built with **Flask**, the app uses JSON for data storage and HTML/CSS for the frontend. Ideal for startups and small-scale businesses.

---

## 2. Key Features

* **Pet Gallery** with image and description
* **Admin Panel** with upload/remove functionality
* **Login System** (hardcoded credentials)
* **Responsive Frontend** (mobile & desktop friendly)
* **Contact Form**
* **Persistent File-based Storage**

---

## 3. Technology Stack & Dependencies

### Backend

* **Python 3.8+**
* **Flask** (routing, server)
* **Jinja2** (template rendering)
* **OS**, **JSON**, **RE** (Python standard libraries)

### Frontend

* **HTML5/CSS3**
* **Bootstrap** (responsive layout)
* **JavaScript (optional)** for interactive elements

### Python Dependencies

```
Flask
```

---

## 4. Directory and File Structure

```
pet_marketplace/
├── app.py                  # Flask application code
├── Pets.txt                # JSON-like database
├── templates/              # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── amdin.html
│   ├── about.html
│   ├── Sell.html
│   ├── Pets.html
│   └── contact.html
├── static/
│   └── img/
│       └── gallery/        # Uploaded images
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 5. Data Storage Format (`Pets.txt`)

* Stores pet metadata as a stringified dictionary.
* Converted into proper JSON with `json.loads()`.
* Example entry:

```json
{
  "dog1.jpg": {
    "uploader": "Ravi",
    "name": "Bruno",
    "phone": "9876543210",
    "email": "ravi@mail.com",
    "catagory": "Dog",
    "image": "static/img/gallery/dog1.jpg",
    "description": "Labrador, 2 years old",
    "price": "150"
  }
}
```

---

## 6. Flask Backend Application Setup

* Run the application:

```bash
python app.py
```

* Flask runs with `debug=True` for development.
* All routes defined in `app.py`.

---

## 7. Route and Endpoint Documentation

### `/` (GET)

* **Home Page**: Loads pets and shows listings on `index.html`

### `/COMMAND` (GET/POST)

* **Handles** form `line` input. If `login`, renders login page.

### `/login` (GET/POST)

* **Admin Login** with fixed credentials `Saif Coach`
* Redirects to admin dashboard `amdin.html`

### `/gallery` (GET/POST)

* Loads `about.html` showing all images from gallery folder

### `/Sell` (GET/POST)

* Renders pet selling form from `Sell.html`

### `/Pets?id=<filename>` (GET/POST)

* Displays detailed pet info (name, price, image, description)

### `/upload` (POST)

* Saves image and updates `Pets.txt`
* Fields: name, price, description, category, image, contact

### `/remove` (POST)

* Admin deletes a pet entry and image file

### `/admin` (GET/POST)

* Redirects to login screen (`login.html`)

### `/contact` (GET/POST)

* Renders `contact.html`

---

## 8. HTML Templates Overview

Each page is implemented using a dedicated Jinja2-powered HTML file:

* **index.html** – Home page with pet cards
* **login.html** – Admin login form
* **amdin.html** – Admin dashboard for listing removal
* **Sell.html** – Upload form for sellers
* **Pets.html** – Single pet view with full details
* **about.html** – Gallery grid view
* **contact.html** – Basic contact form

### Template Features

* Bootstrap containers, cards, navbar, and grid layouts
* Image previews using `<img>`
* Mobile-friendly with responsive media queries

---

## 9. Static Assets and File Management

* Uploaded images saved to:

  * `static/img/gallery/`
* Templates access image paths via:

  ```html
  <img src="{{ dat[pet]['image'] }}">
  ```

---

## 10. Input Validation and Security

* **Field Validation**: Enforced via HTML `required`, `type`, and Flask error handling
* **File Uploads**: Ensure valid filenames and MIME types
* **Security Enhancements** (recommended):

  * Use hashed password storage (Flask-Bcrypt)
  * Implement CSRF protection with Flask-WTF
  * Escape Jinja2 variables to prevent XSS

---

## 11. Testing and Quality Assurance

### Manual Testing

* Upload form validation
* Admin login/logout scenarios
* Pet deletion and file removal checks

### Automated Testing

* Flask client test cases
* JSON parsing edge cases from `Pets.txt`

---

## 12. Deployment Instructions

1. Install Flask:

```bash
pip install flask
```

2. Ensure `Pets.txt` contains: `{}`
3. Run:

```bash
python app.py
```

4. For production, use Gunicorn and serve behind Nginx

---

## 13. SEO Optimization & Keywords

### Meta Tags (in base HTML template):

```html
<meta name="description" content="Sell or adopt pets online. List dogs, cats, and more on our vendor pet marketplace.">
<meta name="keywords" content="pet adoption, pet sales, dog selling website, cat marketplace, Flask pet app">
```

### Suggested Keywords:

```
Flask pet marketplace
pet selling web app
dog and cat listing site
simple vendor portal
HTML upload form Flask
pet gallery Python
Flask pet marketplace
pet selling web app
dog and cat listing site
simple vendor portal
HTML upload form Flask
pet gallery Python
```

---


---

## 14. Author & License

**Author:** Smaron Biswas
**Year:** 2025
**License:** MIT License

Free to use, modify, and distribute.

---

*End of Full Documentation.*
