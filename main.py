from datetime import datetime
import calendar

# with open("../ml-latest-small/genres.tmp.txt", "r") as f:
#     for line in f:
#         line = line[:-1]
#         print("insert into movies.genres values (default,'" + line + "');")

# movieId,title,genres
# title_id | title | year | plot | poster
movie = 0
rating = 0.0
d = datetime.utcnow()
stamp = calendar.timegm(d.utctimetuple())

output = open("genre.sql", "w")


def fun(lorem):
	line = lorem[:-1].split('"')
	print(line)
	return line


for line in open("../ml-latest-small/movies.csv"):

	(movie, title, genres) = line.split(",")

	# genres = genres[:-1]
	for genre in genres[:-1].split('|'):
		year = title[-5:-1]
		title_q = "INSERT INTO movies.titles (title_id, title, year) VALUES (" + movie + ",'" + title + "'," + year + ");"
		genre_q = "INSERT into movies.titles_genres SELECT " + movie + ", genre_id from movies.genres where genre = '" + genre + "';\n"
		print(title_q)
		print(genre_q)
		output.write(title_q + "\n")
		output.write(genre_q)

output.close()
