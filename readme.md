# NetShop

NetShop is a fully functional **web-based e-commerce application** built with **Django**. It supports both buyers and sellers, providing a complete online shopping experience. Stripe is integrated for secure and seamless payment processing.

---

## Features

* **User Authentication:** Login and registration for buyers and sellers.
* **Seller Accounts:** Sellers can manage their products and inventory.
* **Shopping Cart:** Buyers can add products to the cart, update quantities, and remove items.
* **Checkout with Stripe:** Secure payment processing via Stripe API.
* **Order Management:** Orders are recorded in the system with full details (buyer info, products, amounts).
* **Responsive Design:** Works on both desktop and mobile devices.

---

## Technologies Used

* **Backend:** Django 5.2
* **Frontend:** Django Templates, HTML, CSS
* **Database:** SQLite (default), can be configured for PostgreSQL or MySQL
* **Payments:** Stripe (test and live keys supported)
* **Environment Management:** python-decouple for secret keys and configuration

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/NetShop.git
cd NetShop
```

2. **Create a virtual environment:**

```bash
python -m venv netshop_env
```

3. **Activate the environment:**

* Windows PowerShell:

```powershell
.\netshop_env\Scripts\Activate.ps1
```

* CMD:

```cmd
.\netshop_env\Scripts\activate.bat
```

4. **Install dependencies:**

```bash
pip install -r requirements.txt
```

5. **Configure environment variables:**
   Create a `.env` file in the project root and add your keys:

```
SECRET_KEY=your_django_secret_key
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_PUB_KEY=your_stripe_public_key
WEBSITE_URL=http://localhost:8000/
```

6. **Run migrations:**

```bash
python manage.py migrate
```

7. **Create a superuser (admin account):**

```bash
python manage.py createsuperuser
```

8. **Start the development server:**

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`.

---

## Usage

* **Buyers:** Browse products, add items to cart, and checkout using Stripe.
* **Sellers:** Log in to manage products, update prices, and monitor orders.
* **Admins:** Access the Django admin panel for full control over users, products, and orders.

---

## Notes

* Always keep your `.env` file private — **never commit secret keys to GitHub**.
* Stripe keys can be in **test mode** for development. Switch to live keys for production.

---

## License

This project is licensed under the MIT License.
