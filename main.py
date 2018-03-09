with open("../ml-latest-small/genres.tmp.txt", "r") as f:
    for line in f:
        line = line[:-1]
        print("insert into movies.genres values (default,'" + line + "');")
