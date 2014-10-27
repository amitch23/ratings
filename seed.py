import model
import csv
from datetime import datetime, date

# bulk insert a bunch of our movie data into the pre-existing database.


def load_users(session):
    # use u.user

    # open a file
    f = open("seed_data/u.user", "r")
        
    user_table = f.readlines()

    # read and parse each row/line
    for line in user_table:
        row = line.strip().split('|')

        # create an object
        eachuser = model.User(
                               age = int(row[1]),
                               zipcode = row[4])

        session.add(eachuser)
    session.commit()

    f.close()

    


def load_movies(session):

    # use u.item
    f = open("seed_data/u.item", "r")
        
    movie_table = f.readlines()

    # read and parse each row/line
    for line in movie_table:
        row = line.strip().split('|')

        if row[2] != '':
            datetime_obj = datetime.strptime(row[2], "%d-%b-%Y")
        else: 
            datetime_obj = None

        title = row[1].split("(")
        title = title[0].decode("latin-1").strip()

        # create an object
        eachmovie = model.Movie(
                               name = title,
                               released_at = datetime_obj,
                               imdb_url = row[3])

        session.add(eachmovie)

    session.commit()

  
    f.close()


def load_ratings(session):
    # use u.ratings
    f = open("seed_data/u.data", "r")
        
    ratings_table = f.readlines()

    # read and parse each row/line
    for line in ratings_table:
        row = line.split()

        # create an object
        entry = model.Rating(
                               movie_id = row[1],
                               user_id = row[0],
                               rating = row[2])

        session.add(entry)

    session.commit()

    f.close()


    
def main(session):
    load_users(session)
    load_movies(session)
    load_ratings(session)
    # You'll call each of the load_* functions with the session as an argument
    

if __name__ == "__main__":
    s= model.connect()
    main(s)
