CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
);

INSERT INTO Roster (Name, Species, Age)
VALUES
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29);

UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax';

SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran';
