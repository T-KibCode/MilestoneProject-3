CREATE TABLE movies (
  id INTEGER PRIMARY KEY,
  title TEXT,
  release_date DATE,
  genre TEXT,
  director TEXT,
  plot_summary TEXT,
  poster_url TEXT
);

CREATE TABLE actors (
  id INTEGER PRIMARY KEY,
  name TEXT,
  birthdate DATE,
  gender TEXT,
  nationality TEXT
);

CREATE TABLE movie_cast (
  movie_id INTEGER,
  actor_id INTEGER,
  role TEXT,
  FOREIGN KEY (movie_id) REFERENCES movies(id),
  FOREIGN KEY (actor_id) REFERENCES actors(id)
);

INSERT INTO movies (title, release_date, genre, director, plot_summary, poster_url)
VALUES
  ('A Star is Born', '2018-10-05', 'Drama, Music', 'Bradley Cooper', 'A musician helps a young singer find fame as age and alcoholism send his own career into a downward spiral.', 'https://www.example.com/posters/a-star-is-born.jpg'),
  ('Roma', '2018-11-21', 'Drama', 'Alfonso Cuarón', 'A year in the life of a middle-class family''s maid in Mexico City in the early 1970s.', 'https://www.example.com/posters/roma.jpg'),
  ('Black Panther', '2018-02-16', 'Action, Sci-Fi', 'Ryan Coogler', 'T''Challa, heir to the hidden but advanced kingdom of Wakanda, must step forward to lead his people into a new future and must confront a challenger from his country''s past.', 'https://www.example.com/posters/black-panther.jpg'),
  ('Avengers: Infinity War', '2018-04-27', 'Action, Sci-Fi', 'Anthony Russo, Joe Russo', 'The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.', 'https://www.example.com/posters/avengers-infinity-war.jpg'),
  ('Crazy Rich Asians', '2018-08-15', 'Comedy, Romance', 'Jon M. Chu', 'This contemporary romantic comedy, based on a global bestseller, follows native New Yorker Rachel Chu to Singapore to meet her boyfriend''s family.', 'https://www.example.com/posters/crazy-rich-asians.jpg'),
  ('Green Book', '2018-11-16', 'Biography, Comedy, Drama', 'Peter Farrelly', 'A working-class Italian-American bouncer becomes the driver of an African-American classical pianist on a tour of venues through the 1960s American South.', 'https://www.example.com/posters/green-book.jpg'),
  ('Parasite', '2019-05-30', 'Comedy, Drama, Thriller', 'Bong Joon-ho', 'Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.', 'https://www.example.com/posters/parasite.jpg'),
  ('Joker', '2019-10-04', 'Crime, Drama, Thriller', 'Todd Phillips', 'In Gotham City, mentally-troubled comedian Arthur Fleck is disregarded and mistreated by society. He then embarks on a downward spiral of revolution and bloody crime.', 'https://www.example.com/posters/joker.jpg'),
  ('The Irishman', '2019-11-27', 'Biography, Crime, Drama', 'Martin Scorsese', 'A mob hitman recalls his possible involvement with the slaying of Jimmy Hoffa.', 'https://www.example.com/posters/the-irishman.jpg'),
  ('1917','2019-12-25','Drama, War','Sam Mendes',"Two young British soldiers during the First World War are given an impossible mission: deliver a message deep in enemy territory that will stop 1,600 men, and one of the soldiers' brothers, from walking straight into a deadly trap.",'https://www.example.com/posters/1917.jpg');
