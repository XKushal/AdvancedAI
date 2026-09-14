import argparse
import json
import numpy as np

from compute_scores import pearson_score
from collaborative_filtering import find_similar_users

#parse the input arguments 

def build_arg_parser():
	parser = argparse.ArgumentParser(description='Find recommendations for the given user')
	parser.add_argument('--user', dest='user', required=True, help='Input user')
	return parser

#get movie recommendation for the given user 
def get_recommendations(dataset, input_user):
	if input_user not in dataset:
		raise TypeError('Cannot find' + input_user + ' in the dataset')
	#define the variable to track the score 
	overall_scores = {}
	similarity_scores = {}

	#compute scores between the input user and all other user in dataset 
	for user in [x for x in dataset if x != input_user]:
		similarity_score = pearson_score(dataset, input_user, user)
		if similarity_score <= 0:
			continue
		#extract the list of movies that have been rated by the current user but havent been rated by the input user
		filtered_list = [x for x in dataset[user] if x not in \
		dataset[input_user] or dataset[input_user][x] == 0]

		for item in filtered_list:
			overall_scores.update({item: dataset[user][item] * similarity_score})
			similarity_scores.update({item: similarity_score})

	#if no such movies, then we cannot recommend anything
	if len(overall_scores) == 0:
		return ['No recommendations possible']

	#normalize the scores based on the weighted scores 
	#genrate movie ranks by normalizations
	movie_scores = np.array([[score/similarity_scores[item], item]
		for item, score in overall_scores.items()])
	#sort in decreasing order 
	movie_scores = movie_scores[np.argsort(movie_scores[:,0])[::-1]]
	#extract the movie recommendations
	movie_recommendations = [movie for _, movie in movie_scores]
	return movie_recommendations

if __name__ =='__main__':
	args = build_arg_parser().parse_args()
	user = args.user

	#load the movie rating data from the file ratinfs.json
	ratings_file = 'ratings.json'
	with open(ratings_file, 'r') as f:
		data = json.loads(f.read())

	print("\nMovie recommendations for " + user + ":")
	movies = get_recommendations(data, user)
	for i, movie in enumerate(movies):
		print(str(i+1) + '. ' + movie)











