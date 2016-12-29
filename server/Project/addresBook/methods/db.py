import sqlite3


def getAllUser():
    db = sqlite3.connect("db.db")
    db.execute(
        'CREATE TABLE IF NOT EXISTS "User" ("username" TEXT NOT NULL, "password" TEXT NOT NULL, "userid" TEXT NOT NULL, "partment" TEXT NOT NULL, "email" TEXT NOT NULL, "tel" TEXT NOT NULL, "tag" TEXT NOT NULL, "creater" TEXT NOT NULL);')
    results = db.execute('select * from User')
    search_results = []
    for record in results:
        result = {
            'username': record[0],
            'password': record[1],
            'userid': record[2],
            'partment': record[3],
            'email': record[4],
            'tel': record[5],
            'tag': record[6],
            'creater': record[7]
        }
        search_results.append(result)
    db.close()
    return search_results


def addUser(insertUser: dict):
    db = sqlite3.connect("db.db")
    print(insertUser)
    db.execute(
        "INSERT INTO User "
        "(username,password,userid,partment,email,tel,tag,creater) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (insertUser['username'],
         insertUser['password'],
         insertUser['userid'],
         insertUser['partment'],
         insertUser['email'],
         insertUser['tel'],
         insertUser['tag'],
         insertUser['creater']))
    db.commit()
    db.close()


def deleteUser(userId : str):
    db = sqlite3.connect("db.db")
    db.executemany('delete from User where userid = ?', (userId))
    db.commit()
    print(db.total_changes)
    db.close()


if __name__ == '__main__':
    # addUser({
    #     'username': '李亚洲2',
    #     'password': "1234",
    #     'userid': "dsdfsaldf",
    #     'partment': "研发",
    #     'email': "Angry_Li@126.com",
    #     'tel': "18017304908",
    #     'tag': "研发",
    #     'creater': "AngryLi"
    # })
    deleteUser('d7f8a97dsf7sdfffdsf')
