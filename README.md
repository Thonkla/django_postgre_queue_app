
# Order and Queue Website
* Project name: LoreQ
* a simple order and queue website for customer
* To submit the assignment of CPE 334 SOFTWARE ENGINEERING, KMUTT, Thailand

##  Tech Stack:
-   [Django](https://www.djangoproject.com/)  - Django makes it easier to build better web apps more quickly and with less code.
-   [Bootstrap](https://getbootstrap.com/)  - Build fast, responsive sites with Bootstrap.
-   [Postgres](https://www.postgresql.org/)  - The World's Most Advanced Open Source Relational Database.

## Getting Started:
- Setting Posgresql
create new datebase: loreq
### create table: menu (insert your menu)
	* menu_name [PK](character varying 100)
	* menu_price (numeric)
	* description (character varying 500)
	* menu_type (character varying 100)
	* id (integer)

### create table: payment_method (insert your payment method)
	*  payment_method [PK](character varying 50)
	* description (character varying 50)
	
### create table: username
	* id [PK] (integer)
	* username (character varying 100)
	* table_no (integer)
	* date (date)
	* time (time without time zone)

### create table: userqueue
	* queue_id [PK] (integer)
	* username (character varying 100)
	* table_no (integer)
	* total_price (numeric)
	* date (date)
	* time (time without time zone)
	* payment_method (character varying 50)
	* status (character varying 20)

### create table: userqueue_detail
	* id [PK] (integer)
	* queue_id (integer)
	* menu_name (character varying 100)
	* quantity (integer)
	* price (nemeric)

### create table: usertable
	* id [PK] (integer)
	* username (character varying 100)
	* table_no (integer)
	* menu_name (character varying 100)
	* menu_price (double precision)
	* quantity (integer)
### Clone
	cd /your_path
	mkdir LoreQ
	cd LoreQ
	git clone https://github.com/Thonkla/django_postgre_queue_app.git .
### Create a Virtual Environment
	pip install virtualenv
	cd LoreQ
	python3.9 -m virtualenv .
	.\Scripts\activate
	**For Mac use:**  `source bin/activate`
### Install Dependencies
	pip install -r requirements.txt
	Add Your Environment variable to  `.env`. Refer  `.sample.env`  file.
### Make Migrations
	cd /your_path/LoreQ
	python manage.py makemigrations
	python manage.py migrate
### Run Dev Server
	python manage.py runserver localhost:8000
	Open  [localhost:8000](http://localhost:8000/)  in Browser.
