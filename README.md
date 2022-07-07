
# Meme-dozer

## About
Meme-dozer is django based twitter-like social network <br>
Link: [peteropletaev.pythonanywhere.com](http://peteropletaev.pythonanywhere.com) (**adblock recommended**)

Implemented features:
- Profile: create, edit, restore password, add pfp
- Create a post. If a post has a picture, it is considered to be a humoresque. Otherwise - an anecdote.
- Posts are showed on the home page. Posts are positioned by a pinterest-inspired grid.
- Posts will load by 10-packs as the user scrolls down the page
- Posts can be edited, deleted and liked
- Liking a post uses Rest API so that a page doesn't have to be reloaded
- All the information is stored in a SQLite database that consists of 3 tables: users, posts, likes
- Website has an admin page accessible at /admin. Login: admin, password: admin
- Website is adapted for all kinds of screens

# Setup

The first thing to do is to clone the repository:

$ git clone [https://github.com/petosbratok/meme-dozer](https://github.com/petosbratok/meme-dozer)

$ cd meme-dozer

Install Python and Pip.
Install the dependencies:

$ pip install -r requirements.txt

Once  `pip`  has finished downloading the dependencies:

$ cd project
$ python manage.py runserver

# Main links 
Home page:  `http://127.0.0.1:8000/`<br>
Profile: `http://127.0.0.1:8000/profile`<br>
Posts of a certain user: `http://127.0.0.1:8000/user/<user_id>`<br>
Certain post: `http://127.0.0.1:8000/post/<post_id>` <br>
About the website: `http://127.0.0.1:8000/about`

