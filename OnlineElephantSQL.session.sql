
--@BLOCK 
CREATE TABLE actor (
  ActorId BIGSERIAL NOT NULL,
  FirstName VARCHAR(50) NOT NULL,
  LastName VARCHAR(50) NOT NULL,
  PRIMARY KEY  (ActorId)
);

--@BLOCK
CREATE TABLE movie (
  MovieId BIGSERIAL NOT NULL,
  Title VARCHAR(255) NOT NULL,
  ReleaseYear INTEGER NOT NULL,
  Rating VARCHAR(10) NOT NULL,
  PRIMARY KEY  (Movieid)
);

--@BLOCK
CREATE TABLE actor_movie(
    ShareId  BIGSERIAL NOT NULL,
    actor_id BIGINT NOT NULL,
    movie_id BIGINT NOT NULL
);


--@BLOCK
Drop TABLE actor_movie;

--@BLOCK
INSERT INTO movie (Title, ReleaseYear, Rating) VALUES 
('The Shawshank Redemption', 1994, '9.3'),
('The Godfather', 1972, '9.2'),
('The Godfather: Part II', 1974, '9.0'),
('The Dark Knight', 2008, '9.0'),
('12 Angry Men', 1957, '8.9'),
('Schindler''s List', 1993, '8.9'),
('The Lord of the Rings: The Return of the King', 2003, '8.9'),
('Pulp Fiction', 1994, '8.9'),
('The Good, the Bad and the Ugly', 1966, '8.8'),
('Fight Club', 1999, '8.8'),
('Forrest Gump', 1994, '8.8'),
('Inception', 2010, '8.7'),
('The Lord of the Rings: The Fellowship of the Ring', 2001, '8.7'),
('The Lord of the Rings: The Two Towers', 2002, '8.7'),
('Star Wars: Episode V - The Empire Strikes Back', 1980, '8.7'),
('The Matrix', 1999, '8.6'),
('Goodfellas', 1990, '8.6'),
('One Flew Over the Cuckoo''s Nest', 1975, '8.6'),
('Seven Samurai', 1954, '8.6'),
('Se7en', 1995, '8.6');

--@BLOCK
ALTER TABLE actor_movie
ADD FOREIGN KEY (actor_id) REFERENCES actor(ActorId),
ADD FOREIGN KEY (movie_id) REFERENCES movie(MovieId);

--@BLOCK
INSERT INTO actor (actorid, firstname, lastname)
VALUES (1, 'Samuel L.', 'Jackson'),
       (2, 'John', 'Travolta'),
       (3, 'Uma', 'Thurman'),
       (4, 'Bruce', 'Willis'),
       (5, 'Christian', 'Bale'),
       (6, 'Heath', 'Ledger'),
       (7, 'Gary', 'Oldman'),
       (8, 'Aaron', 'Eckhart'),
       (9, 'Tom', 'Hanks'),
       (10, 'Robin', 'Wright'),
       (11, 'Sally', 'Field'),
       (12, 'Leonardo', 'DiCaprio'),
       (13, 'Tom', 'Hardy'),
       (14, 'Ellen', 'Page'),
       (15, 'George', 'Clooney'),
       (16, 'Brad', 'Pitt'),
       (17, 'Julia', 'Roberts'),
       (18, 'Robert', 'De Niro'),
       (19, 'Al', 'Pacino'),
       (20, 'Matt', 'Damon'),
       (21, 'Mark', 'Wahlberg'),
       (22, 'Philip Seymour', 'Hoffman'),
       (23, 'Meryl', 'Streep'),
       (24, 'Amy', 'Adams'),
       (25, 'Jack', 'Nicholson'),
       (26, 'Kim', 'Basinger'),
       (27, 'Jude', 'Law'),
       (28, 'Cate', 'Blanchett'),
       (29, 'Kate', 'Beckinsale'),
       (30, 'Jennifer', 'Lawrence'),
       (31, 'Woody', 'Harrelson'),
       (32, 'Emma', 'Watson'),
       (33, 'Alan', 'Rickman'),
       (34, 'Matthew', 'McConaughey'),
       (35, 'Hailee', 'Steinfeld'),
       (36, 'Jeff', 'Bridges'),
       (37, 'Angelina', 'Jolie'),
       (38, 'Frances', 'McDormand');




-- @BLOCK
SELECT FirstName, LastName FROM actor;

WHERE

-- @BLOCK
SELECT * FROM movie;

-- @BLOCK
SELECT * FROM actor_movie 

-- @BLOCK
DROP TABLE actor_movie

-- @BLOCK
CREATE INDEX FirstName_index ON actor(FirstName);
CREATE INDEX LastName_index ON actor(LastName);
CREATE INDEX Title_index ON movie(Title);
CREATE INDEX ReleaseYear_index ON movie(ReleaseYear);
CREATE INDEX Rating_index ON movie(Rating);


-- @BLOCK
SELECT