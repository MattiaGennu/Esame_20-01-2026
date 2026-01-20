from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:

    @staticmethod
    def get_all_nodes(n_alb):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT artist.id,COUNT(artist.id) as n_alb, artist.name
                    FROM artist, album 
                    WHERE album.artist_id = artist.id
                    GROUP BY artist.id
                    having n_alb>=%s
                """
        cursor.execute(query, (n_alb,))
        for row in cursor:
            a = Artist(
                id=row['id'],
                name=row['name'],

            )
            result.append(a)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_mappa_collegamenti():
        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)

        query = """
                SELECT t.id, g.name, t.composer
                FROM track t, genre g
                WHERE t.genre_id = g.id

                """

        cursor.execute(query)
        for row in cursor:

            nodo_id = row['composer']
            collegamento_id = row['name']

            if nodo_id not in result:
                result[nodo_id] = set()

            result[nodo_id].add(collegamento_id)

        cursor.close()
        conn.close()
        return result