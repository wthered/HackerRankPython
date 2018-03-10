movie = 0
rating = 0.0
output = open("genre.sql", "w")

for line in open("../ml-latest-small/movies.csv"):
	(movie, genres) = line.split(",")
	for genre in genres[:-1].split('|'):
		title_q = "INSERT INTO movies.titles (title_id) VALUES (" + movie + ");"
		genre_q = "INSERT into movies.titles_genres SELECT " + movie + ", genre_id from movies.genres where genre = '" + genre + "';"
		print(title_q)
		print(genre_q)
		output.write(title_q + "\n")
		output.write(genre_q + "\n")

output.close()
