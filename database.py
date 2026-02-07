import mysql.connector
import mysql


# Database connection
def try_connection():
    """
    Attempts to connect to the MySQL database.
    Returns a database connection object if successful,
    or False if the connection is refused.
    """
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="{Ljdf6@BF%Ye0$t!}",
            database="a-levelnea"
        )
        return db
    except ConnectionRefusedError:
        # Connection failed
        return False


# Leaderboard & scores
def collect_leaderboard_data():
    """
    Fetches all users and their high scores from the database,
    sorted in descending order (highest score first).
    Returns a list of tuples: [(username, high_score), ...]
    """
    db = try_connection()
    cursor = db.cursor()

    cursor.execute(
        "SELECT Username, high_score "
        "FROM players "
        "ORDER BY high_score DESC;"
    )

    high_score = cursor.fetchall()

    return high_score


def collect_scores(User_ID):
    """
    Fetches a specific user's recent score and high score
    based on their User_ID.
    Returns a tuple: (recent_score, high_score)
    """
    db = try_connection()
    cursor = db.cursor()

    cursor.execute(
        "SELECT recent_score, High_score "
        "FROM players "
        "WHERE User_ID = %s", (User_ID,)
    )

    scores = cursor.fetchone()
    return scores


# User registration
def registor_new_user(Username, password):
    """
    Registers a new user with the database.
    Initializes recent_score and High_score to 0.
    Returns True on success.
    """
    db = try_connection()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO players (Username, password, recent_score, High_score) "
        "VALUES (%(Username)s, %(password)s, 0, 0)",
        {'Username': Username, 'password': password}
    )

    db.commit()
    return True


# User login check
def check_database(username, password):
    """
    Checks if a given username/password pair exists in the database.
    Returns:
        (True, User_ID) if user exists
        (False, new_user_id) if user does not exist
    """
    db = try_connection()
    cursor = db.cursor()

    # Get all usernames and passwords
    cursor.execute(
        "SELECT Username, password "
        "FROM players;"
    )

    data = cursor.fetchall()

    # Search for matching username/password
    for i in range(len(data)):
        if data[i][0] == username and data[i][1] == password:
            return True, i + 1  # i+1 corresponds to User_ID

    # If no match, return False and next available User_ID
    return False, len(data) + 1
