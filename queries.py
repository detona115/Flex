def criarTabelaUser():
    query = "CREATE TABLE IF NOT EXISTS users(\
        id INT NOT NULL PRIMARY KEY,\
        name varchar(100),\
        username varchar(100),\
        email varchar(100),\
        address jsonb,\
        phone varchar(50),\
        website varchar(50),\
        company jsonb);"

    return query

def criarTabelaDividas():
    query = "CREATE TABLE IF NOT EXISTS debts(\
        id SERIAL,\
        iduser INT REFERENCES users(id) ON DELETE CASCADE,\
        reason varchar(150),\
        data DATE,\
        value DECIMAL,\
        PRIMARY KEY(id, iduser));"

    return query

def inserirUsers():
    query = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"

    return query

def listClients():
    query = "SELECT\
        id, name, username, email,\
        address ->> 'city',\
        address ->> 'street',\
        address ->> 'zipcode',\
        phone FROM users;"
    
    return query

def listaNomes():
    query = "SELECT name FROM users;"

    return query

def saveNewDebt():
    #query = "(SELECT id FROM users WHERE name = user)"
    #((SELECT id FROM users WHERE name = user), reason, data, valor )
    query2 = "INSERT INTO debts (iduser, reason, data, value) VALUES (%s, %s, %s, %s)"
    return query2