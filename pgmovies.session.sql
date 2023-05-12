CREATE TABLE actor (
  ActorId BIGSERIAL NOT NULL,
  FirstName VARCHAR(50) NOT NULL,
  LastName VARCHAR(50) NOT NULL,
  PRIMARY KEY  (ActorId),
);


MovieId FOREIGN KEY (MovieId) REFERENCES movie(MovieId)
CREATE TABLE movie (
  MovieId BIGSERIAL NOT NULL,
  Title VARCHAR(255) NOT NULL,
  ReleaseYear INTEGER NOT NULL,
  Rating VARCHAR(10) NOT NULL,
  PRIMARY KEY  (movie_id),
  ActorId FOREIGN KEY (ActorId) REFERENCES actor(ActorId)
);


CREATE TABLE actor_movie(
  actor_id BIGINT NOT NULL,
  movie_id BIGINT NOT NULL,
  PRIMARY KEY (actor_id, movie_id),
  FOREIGN KEY (actor_id) REFERENCES actor (actor_id),
  FOREIGN KEY (movie_id) REFERENCES movie (movie_id)
);

