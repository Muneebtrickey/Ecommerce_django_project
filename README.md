# EcomerceDjango - Professional E-Commerce Platform

[![Django](https://img.shields.io/badge/Django-4.1.5-092e20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.13-3776ab?style=for-the-badge&logo=python)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0-563d7c?style=for-the-badge&logo=bootstrap)](https://getbootstrap.com/)

A robust, feature-rich e-commerce web application built with **Django**. This project provides a complete shopping experience, from browsing products and managing a wishlist to a secure checkout process. It features a modern, responsive user interface and a powerful admin dashboard for seamless management.

---

## 📸 Screenshots

> **Note to Developer:** Replace the placeholders below with your actual screenshots for a truly professional GitHub profile.

| Home Page | Product Collections |
| :---: | :---: |
| ![Home Page](https://via.placeholder.com/800x450?text=Home+Page+Screenshot) | ![Collections](https://via.placeholder.com/800x450?text=Collections+View+Screenshot) |

| Shopping Cart | Checkout Process |
| :---: | :---: |
| ![Cart](https://via.placeholder.com/800x450?text=Cart+Screenshot) | ![Checkout](https://via.placeholder.com/800x450?text=Checkout+Screenshot) |

| Modern Admin Dashboard (Jazzmin) |
| :---: |
| ![Admin Dashboard](https://via.placeholder.com/1000x500?text=Jazzmin+Admin+Panel+Screenshot) |

---

## ✨ Key Features

- **🛍️ Product Discovery:** Browse products by categories, trending items, and SEO-optimized slugs.
- **❤️ Wishlist System:** Save favorite products for later with a dedicated wishlist management view.
- **🛒 Dynamic Shopping Cart:** Add, update, and remove items with real-time stock management.
- **🔐 User Authentication:** Secure registration, login, and logout functionality.
- **💳 Checkout & Orders:** Comprehensive checkout flow with order history and status tracking (Pending, Out For Shipping, Completed).
- **🎨 Modern Admin UI:** Enhanced admin panel using `django-jazzmin` for a professional, customizable management experience.
- **📱 Fully Responsive:** Optimized for all devices using Bootstrap and custom CSS.
- **🔍 SEO Ready:** Built-in support for meta titles, keywords, and descriptions for categories and products.

---

## 🛠️ Technologies Used

- **Backend:** Django 4.1.5, Python 3.13
- **Database:** SQLite (Default), easily migratable to PostgreSQL or MySQL
- **Frontend:** HTML5, CSS3, JavaScript, jQuery, Bootstrap
- **Admin Interface:** Jazzmin
- **Image Handling:** Pillow (PIL)

---

## 📂 Project Structure

```text
EcomerceDjango/
├── Ecom/                   # Project configuration
│   ├── settings.py         # App settings & Jazzmin config
│   └── urls.py             # Root URL routing
├── store/                  # Main application logic
│   ├── controller/         # Modular views (Auth, Cart, Wishlist, Checkout)
│   ├── models.py           # Database schema (Product, Category, Order, etc.)
│   ├── templates/          # HTML templates
│   └── urls.py             # App-specific URL routing
├── static/                 # Static assets (CSS, JS, Images, Uploads)
├── manage.py               # Django CLI tool
└── db.sqlite3              # Database file
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/EcomerceDjango.git
cd EcomerceDjango
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django django-jazzmin pillow mysqlclient
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6. Start Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the site and `http://127.0.0.1:8000/admin` for the admin panel.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

**Your Name** - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/your-username/EcomerceDjango](https://github.com/your-username/EcomerceDjango)
