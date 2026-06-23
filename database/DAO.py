from database.DB_connect import DBConnect
from model.opera import Opera

class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getNodes():
        conn=DBConnect.get_connection()
        cursor=conn.cursor()

        query="""select o.object_id as id , o.object_name as oName
                from objects o """
        ris=[]

        cursor.execute(query)
        for row in cursor.fetchall():
            ris.append(Opera(*row))

        cursor.close()
        conn.close()
        return ris

    @staticmethod
    def getEdges():
        conn=DBConnect.get_connection()
        cursor=conn.cursor(dictionary=True)
        query="""   SELECT eo.object_id as id1  , eo2.object_id as id2, count(*) as cnt
                    from exhibition_objects eo ,  exhibition_objects eo2 
                    WHERE eo.exhibition_id = eo2.exhibition_id AND eo.object_id<eo2.object_id AND eo.object_id!=eo2.object_id 
                    GROUP BY eo.object_id , eo2.object_id

                """
        ris=[]
        cursor.execute(query)
        for row in cursor.fetchall():
            ris.append((row["id1"],row["id2"],row["cnt"]))

        cursor.close()
        conn.close()
        return ris
