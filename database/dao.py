from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:

    @staticmethod
    def get_all_artists():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT *
                FROM artist a
                """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_artists_with_min_albums(min_albums):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                select a1.id, a1.name, COUNT(a2.title) as peso
                from artist a1 , album a2
                where a1.id = a2.artist_id 
                group by a1.id
                having peso >= %s
                """
        cursor.execute(query, (min_albums,))
        for row in cursor:
            result.append((row['id'],row['name'],row['peso']))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_connessioni():

        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)
        query = """
               select a.artist_id, t.genre_id
               from album a, track t
               where a.id = t.album_id 
                """
        cursor.execute(query)
        for row in cursor:
            if row['artist_id'] not in result:
                result[row['artist_id']] = {'genre_id': [row['genre_id']]}
            else:
                if row['genre_id'] not in result[row['artist_id']]['genre_id']:
                    result[row['artist_id']]['genre_id'].append(row['genre_id'])
        cursor.close()
        conn.close()
        return result
