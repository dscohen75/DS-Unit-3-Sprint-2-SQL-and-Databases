import sqlite3 

conn = sqlite3.connect(r'c:\Users\anika\Desktop\AnikaDS\SL\SQL\Chinook_Sqlite.sqlite')
cursor = conn.cursor()

invoice = cursor.execute('SELECT AVG(Total) FROM Invoice GROUP BY CustomerId LIMIT 5;').fetchall()
us_cust = cursor.execute('SELECT * FROM Customer WHERE Country = "USA" LIMIT 5;').fetchall()
no_report = cursor.execute('SELECT EmployeeID, FirstName, LastName FROM Employee WHERE ReportsTo IS NULL;').fetchall()
composers = cursor.execute('SELECT COUNT (DISTINCT Composer) FROM Track LIMIT 10;').fetchall()
tracks = cursor.execute('SELECT COUNT(*) FROM Track;').fetchall()

black_sabbath = cursor.execute('SELECT Track.Name, Album.Title, Track.Composer FROM Track INNER JOIN Album ON Track.AlbumId = Album.AlbumId WHERE Composer = "Black Sabbath";').fetchall()
genre_tracks = cursor.execute('SELECT COUNT(DISTINCT(Track.TrackId)), Genre.Name FROM Track INNER JOIN Genre ON Track.GenreId = Genre.GenreId GROUP BY Genre.GenreId ORDER BY COUNT(DISTINCT(Track.TrackId)) DESC LIMIT 1;').fetchall()

if __name__ == "__main__":
    print(genre_tracks)


'''
Output 1: [(5.659999999999999,), (5.3742857142857146,), (5.659999999999999,), (5.659999999999999,), (5.802857142857143,)]
Output 2: [(16, 'Frank', 'Harris', 'Google Inc.', '1600 Amphitheatre Parkway', 'Mountain View', 'CA', 'USA', '94043-1351', '+1 (650) 253-0000', '+1 (650) 253-0000', 'fharris@google.com', 4), (17, 'Jack', 'Smith', 'Microsoft Corporation', '1 Microsoft Way', 'Redmond', 'WA', 'USA', '98052-8300', '+1 (425) 882-8080', '+1 (425) 882-8081', 'jacksmith@microsoft.com', 5), (18, 'Michelle', 'Brooks', None, '627 Broadway', 'New York', 'NY', 'USA', '10012-2612', '+1 (212) 221-3546', '+1 (212) 221-4679', 'michelleb@aol.com', 3), (19, 'Tim', 'Goyer', 'Apple Inc.', '1 Infinite Loop', 'Cupertino', 'CA', 'USA', '95014', '+1 (408) 996-1010', '+1 (408) 996-1011', 'tgoyer@apple.com', 3), (20, 'Dan', 'Miller', None, '541 Del Medio Avenue', 'Mountain View', 'CA', 'USA', '94040-111', '+1 (650) 644-3358', None, 'dmiller@comcast.com', 4)]
Output 3: [(1, 'Andrew', 'Adams')]
Output 4: [(852,)]
Output 5: [(3503,)]
Output 6: [('Sabbra Cadabra', 'Garage Inc. (Disc 1)', 'Black Sabbath')]
Output 7: [(1297, 'Rock')]
'''