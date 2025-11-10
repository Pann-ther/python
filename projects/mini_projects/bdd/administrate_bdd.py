import psycopg2 as c

config={
    "host" : "192.168.1.36",
    "user" : "panther",
    "password" : "pan",
    "database" : "wsl25",
    "port":"5432"
}


def test_connection():
    # Parametres de connexion a PSQL
    connection = c.connect(**config)
    
    # Teste la connexion avec PSQL
    try:
        # connection a la base
        print("connection au serveur reussi")
        
        # Test avec requete
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"Verion: {version[0]}")
        cursor.close()
        connection.close()
        return True
        
    except c.OperationalError as e:
        # Gestion de l'erreur
        print(f"Impossible de se conecter au serveur: {e}")
        print("Parametres utilises: ")
        
        for key, value in connection.items():
            
            if key != "password":
                print(f"{key}: {value}")
        
        connection.close()
        print("connection ferme")
        

def insert_data(connection,table,mu,pu,dips,squat):
    cursor = connection.cursor()
    cursor.execute(
        f"INSERT INTO {table} (mu, pu, dips, squat) VALUES (%s,%s,%s,%s)",
        (mu,pu,dips,squat)        
    )
    
    connection.commit()
    print("Les donnees ont bien ete saisi")
    cursor.close

    
def select_data(connection,table):
    cursor=connection.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    users=cursor.fetchall()
    
    for user in users:
        print(f"ID:{user[0]} mu:{user[1]} pu:{user[2]} dips:{user[3]} squat:{user[4]}")
    
    cursor.close()

if __name__ == "__main__":
    if test_connection() == True:
        connection = c.connect(**config)
        valeurs_test={
            "table":"m_66kg",
            "mu":"43",
            "pu":"100",
            "dips":"117.5",
            "squat":"187.5"
        }
        
        insert_data(
            connection,
            valeurs_test["table"],
            valeurs_test["mu"],
            valeurs_test["pu"],
            valeurs_test["dips"],
            valeurs_test["squat"]
        )
        select_data(connection, valeurs_test["table"])
