import mysql.connector
import mysql


def try_connection():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="{Ljdf6@BF%Ye0$t!}",
            database="a-levelnea"
        )

        return db

    except ConnectionRefusedError:
        return False


def collect_leaderboard_data():
    db = try_connection()
    cursor = db.cursor()

    cursor.execute("SELECT Username, high_score "
                   "FROM players "
                   "ORDER BY high_score DESC;")

    high_score = cursor.fetchall()
    print(high_score)
    return high_score


def collect_recent_score(User_ID):
    db = try_connection()
    cursor = db.cursor()

    cursor.execute("SELECT recent_score "
                   "FROM players "
                   "WHERE User_ID = %s", (User_ID,))

    recent_score = cursor.fetchone()

    return recent_score

def registor_new_user(Username, password):
    db = try_connection()
    cursor = db.cursor()

    cursor.execute("INSERT INTO players (Username, password, recent_score, High_score) "
                   "Values (%(Username)s, %(password)s, 0, 0 )", {'Username': Username, 'password': password},)

    db.commit()

    return True


def commit_recent_score(recent_score, user_ID):
    db = try_connection()
    cursor = db.cursor()
    cursor.execute("")

    db.commit()


