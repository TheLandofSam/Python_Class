movies =[
    {'name': 'Dead Poets Society', 'genre': 'drama', 'sub-genre': 'coming of age', 'rating': '8.0'},
    {'name': 'Apollo 13', 'genre': 'drama', 'sub-genre': 'docudrama', 'rating': '8.7'},
    {'name': 'Lord of the Rings: Fellowship of the Ring', 'genre': 'fantasy', 'sub-genre': 'adventure', 'rating': '9.9'},
    {'name': 'Lord of the Rings: The Two Towers', 'genre': 'fantasy', 'sub-genre': 'adventure', 'rating': '9.9'},
    {'name': 'Lord of the Rings: The Return of the King', 'genre': 'fantasy', 'sub-genre': 'adventure', 'rating': '9.9'},
    {'name': 'Mean Girls', 'genre': 'comedy', 'sub-genre': 'teen', 'rating': '6.8'},
    {'name': 'Erin Brocovich', 'genre': 'drama', 'sub-genre': 'legal', 'rating': '7.3'},
    {'name': 'Forrest Gump', 'genre': 'drama', 'sub-genre': 'comedy', 'rating': '8.2'},
    {'name': 'Silence of the Lambs', 'genre': 'thriller', 'sub-genre': 'horror', 'rating': '8.1'},
    {'name': 'The Girl With the Dragon Tattoo', 'genre': 'thriller', 'sub-genre': 'psychological', 'rating': '7.8'},
    {'name': 'The Bone Collector', 'genre': 'thriller', 'sub-genre': 'crime', 'rating': '8.0'},
    {'name': 'Harry Potter and the Sorcerer\'s Stone', 'genre': 'fantasy', 'sub-genre': 'children', 'rating': '9.0'},
    {'name': 'Harry Potter and the Chamber of Secrets', 'genre': 'fantasy', 'sub-genre': 'children', 'rating': '8.8'},
    {'name': 'Harry Potter and the Prisoner of Azkaban', 'genre': 'fantasy', 'sub-genre': 'teen', 'rating': '8.8'},
    {'name': 'Harry Potter and the Goblet of Fire', 'genre': 'fantasy', 'sub-genre': 'teen', 'rating': '8.9'},
    {'name': 'Harry Potter and the Order of the Phoenix', 'genre': 'fantasy', 'sub-genre': 'teen', 'rating': '9.0'},
    {'name': 'Harry Potter and the Half Blooded Prince', 'genre': 'fantasy', 'sub-genre': 'teen', 'rating': '9.0'},
    {'name': 'Harry Potter and the Deathly Hallows: Part 1', 'genre': 'fantasy', 'sub-genre': 'teen', 'rating': '9.0'},
    {'name': 'Harry Potter and the Deathly Hallows: Part 2', 'genre': 'fantasy', 'sub-genre': 'teen', 'rating': '9.0'}
]
'''
def print_movies(movie_list):
    print('\n Your movie recommendation(s): ')
    for movie in movie_list:
        print(f'{movie['name'], movie['genre'], movie['rating']}')

print_movies(movies)
'''

def print_movies(recommendation_list):
    for movie in recommendation_list:
        #print(f'📺 {movie['name'], movie['genre'], movie['rating']}') -- done with commas Python is taking it as a a group of data and thus putting the parenths
        print(f'📺 {movie['name']} 🟣 {movie['genre']} ⭐ {movie['rating']}')

def movie_recommendation():
    genre = input('What is your preferred genre? (Enter: drama, fantasy, thriller or comedy) ')

    min_rating = input('Please enter minimum rating between 1.0 and 10.00 ')

    recommendation_list = []
    for movie in movies:
        if movie['genre'] == genre.lower() and movie['rating'] >= min_rating:
            recommendation_list.append(movie)
                
    recommendation_list = [movie for movie in movies if movie['genre'] == genre.lower() and movie['rating']>= min_rating]
    
    print(f'\n You should check out the following film(s): \n')
    print_movies(recommendation_list)

    
movie_recommendation()