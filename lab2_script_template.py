def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {'full name' : ' Nilarjo Mazumdar' ,
                'student_id' : 10312032,
                'pizza_topping' : [
                    'ONION' ,
                    'JALAPENEOS'
                    'HOT PEPPERS'
                ] ,
                'movies' : [
                    {'title' : 'The Shawshank Redemption' ,
                     'genre' : 'Drama'},
                    {'title' : 'Dead Poets Society' ,
                      'genre' : 'Drama'}
                      ]
                      }

    # TODO: Step 3 - Add another movie to the data structure
    about_me['movies'].append:({'title' : '3 Idiots',
                                'genre' : 'coming of the age drama'})
    print_student_name_and_id(about_me)
    return
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(data_struct):
    full_name = data_struct['full name']
    first_name = (full_name.split(' '))[0]
    student_id = data_struct['student_id']

    print(f"My name is {full_name}, but you can call me señor {first_name}.")
    print(f"My Student ID is {student_id}.")
    return
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(data_struct, toppings):
     if 'pizza_topping' in data_struct:
        pizza_toppings = data_struct['pizza_topping']
        pizza_toppings.extend(toppings)
        pizza_toppings.sort()
        pizza_toppings = [topping.lower() for topping in pizza_toppings]
        data_struct['pizza_topping'] = pizza_toppings
     return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_favorite_toppings(data_struct):
     if 'pizza_toppings' in data_struct:
        pizza_toppings = data_struct['pizza_toppings']

        print("My favourite pizza toppings are:")
        for topping in pizza_toppings:
            print(f"- {topping}")
     return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(data_struct):
    if 'movies' in data_struct:
        movies = data_struct['movies']

        if movies:
            genres = [movie['genre'] for movie in movies]
            genre_list = ", ".join(genres[:-1]) + (" and " if len(genres) > 1 else "") + genres[-1]

            print(f"I like to watch {genre_list} movies.")
    return

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    if movie_list:
        titles = [movie['title'] for movie in movie_list]
        edited_titles = ", ".join([title.title() for title in titles[:-1]]) + (" and " if len(titles) > 1 else "") + titles[-1].title()

        print(f"Some of my favourite movies are {edited_titles}!")
    return
if __name__ == '__main__':
    main()