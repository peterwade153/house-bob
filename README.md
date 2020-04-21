# house-bob

This is a Django application which uses a scrapy spider to pull properties data .i.e houses and offices available for rent in Kampala and neighbouring districts.
The Scraped data containing property price, location, district, bedrooms, bathrooms, status whether its available for rent or sale and agent details is then saved in a Postgres database.

### Installation

Create a virtual env and activate it.

Clone the project
<pre>
git clone https://github.com/peterwade153/properties.git
</pre>

Create a Postgres Database.


Create a `.env` file from the `.env.example` and replace with the actual values.


Install Dependencies.

<pre>
pip install requirements.txt
</pre>

