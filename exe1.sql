CREATE Table Movies(
    id INT PRIMARY KEY,
    Title Text,
    Director TEXT,
    Year INT,
    Length_minutes INT
    );

INSERT INTO Movies (id,Title, Director, Year, Length_minutes) VALUES (1,'Toy Story','John Lasseter',1995,85);
INSERT INTO Movies (id,Title, Director, Year, Length_minutes) VALUES (2,'A Bug''s Life','El Direcore',1998,95);
INSERT INTO Movies (id,Title, Director, Year, Length_minutes) VALUES (3,'Toy Story 2','John Lasseter',1899,93);
INSERT INTO Movies (id,Title, Director, Year, Length_minutes) VALUES (4,'Monster, lnc.','Pete Docter',2001,92);
INSERT INTO Movies (id,Title, Director, Year, Length_minutes) VALUES (5,'Toy Story','Andrew Stanton',2003,107);
INSERT INTO Movies (id,Title, Director, Year, Length_minutes) VALUES (6,'The Incredibles','Brad Bird',2004,116);
INSERT INTO Movies (id,Title, Director, Year, Length_minutes) VALUES (7,'Cars','John Lasseter',2006,117);
INSERT INTO Movies (id,title, director, year, length_minutes) VALUES (8,'Ratatouille', 'Brad Bird', 2007, 115);
INSERT INTO Movies (id,title, director, year, length_minutes) VALUES (9,'WALL-E', 'Andrew Stanton', 2008, 104);
INSERT INTO Movies (id,title, director, year, length_minutes) VALUES (10,'Up','Pete Docter', 2009, 101);
INSERT INTO Movies (id,title, director, year, length_minutes) VALUES (11,'Toy story 8', 'El Directre', 2010, 103);
INSERT INTO Movies (id,title, director, year, length_minutes) VALUES (12,'Cars 2', 'John Lasseter', 2011, 120);
INSERT INTO Movies (id,title, director, year, length_minutes) VALUES (13,'Brave', 'Brenda Chapman', 2012, 102);
INSERT INTO Movies (id,title, director, year, length_minutes) VALUES (14,'Monsters University', 'Dan Scanlon', 2013, 110);

select*from Movies;
select title from Movies;
select director from Movies;
select title,director from Movies;
select title,year from Movies;
select * from Movies where id = 6;
select * from Movies where year between 2000 and 2010;
select * from Movies where year not between 2000 and 2010;
select title,year from Movies where id between 1 and 5;
select * from Movies where Title like 'Toy Story';
select * from Movies where Director like 'John Lasseter';
select * from Movies where Director not like 'John Lasseter';
select * from Movies where title like '%WALL%';
