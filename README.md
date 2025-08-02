# Movies-Recommender-System

* How to set up
* About the application
* Data
* Technologies
* Database structure
  
## How to set up
#### 1. Required Python Version
Python 3.13.5
 
#### 2. Clone the Repository 
git clone https://github.com/kaushalsingh0410/Movies-Recommender-System.git

#### 3. Change Directory to Project Root
cd Movies-Recommender-System

#### 4. Create Virtual Environment using Python 3.13.5
python.exe -m venv env

#### 5. Activate Virtual Environment
env\Scripts\activate

#### 6. Change Directory to mrs
cd mrs

#### 7. Install Required Libraries
pip install -r requirements.txt

#### 8. Run the Server
python.exe manage.py runserver

#### 9. Open in Browser
Visit: http://127.0.0.1:8000/

## About the application
This is a movie recommendation system that recommends movies based on your interests.
It uses cosine similarity to find relationships between movies based on their title, genres, keywords, overview, production companies, actors, writers, and directors.
It’s not just a single-page application — users can perform multiple activities within it.

## Data
* I used the Kaggle TMDB 5000 Movies Dataset to build a cosine similarity model, which is available in the mrs-jupyter directory.
* The model was trained using the mrs.ipynb notebook.
* I used the TMDB API to collect and filter detailed data for all 5000 movies in the movies.ipynb notebook, also located in the mrs-jupyter directory.

## Technologies Used
* Jupyter Notebook
* Python
* scikit-learn
* Pandas
* Requests
* RapidFuzz
* Django
* HTML
* Bootstrap
* jQuery


## Database structure

A movie contains multiple types of data:

Some fields are mostly unique and hold a single value per movie, such as:

adult, budget, backdrop_path, poster_path, revenue, homepage, title, overview, popularity, release_date, runtime, tagline, vote_average, and vote_count.

Other fields can repeat across multiple movies and represent a sequence or list-like structure, similar to a dictionary or array:

belongs_to_collection, genres, origin_country, production_companies, spoken_languages, keywords, backdrops, posters, and videos.

To manage this structure effectively, there is a separate model for each repeatable category, and they are connected to the movie model using many-to-many relationships