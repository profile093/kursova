import mysql.connector

# Подключение к базе данных
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)

cursor = mydb.cursor()

# Создание базы данных
cursor.execute("CREATE DATABASE IF NOT EXISTS awards_db")
cursor.execute("USE awards_db")

# Создание таблицы премий
cursor.execute("""
CREATE TABLE IF NOT EXISTS awards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year INT NOT NULL,
    award_name VARCHAR(255) NOT NULL,
    university VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    gender VARCHAR(50)
)
""")

# Вставка данных
awards_data = [
(1936, 'Fields Medal', 'Harvard University', 'Lars', 'Ahlfors', 'Finland', 'Male'),
    (1936, 'Fields Medal', 'MIT', 'Jesse', 'Douglas', 'USA', 'Male'),
    (1950, 'Fields Medal', 'University of Paris', 'Laurent', 'Schwartz', 'France', 'Male'),
    (1950, 'Fields Medal', 'Institute for Advanced Study', 'Atle', 'Selberg', 'Norway', 'Male'),
    (1954, 'Fields Medal', 'University of Tokyo', 'Kunihiko', 'Kodaira', 'Japan', 'Male'),
    (1954, 'Fields Medal', 'Collège de France', 'Jean-Pierre', 'Serre', 'France', 'Male'),
    (1958, 'Fields Medal', 'University College London', 'Klaus', 'Roth', 'UK', 'Male'),
    (1958, 'Fields Medal', 'University of Strasbourg', 'René', 'Thom', 'France', 'Male'),
    (1962, 'Fields Medal', 'Lomonosov Moscow State University', 'Lars', 'Hormander', 'Sweden', 'Male'),
    (1962, 'Fields Medal', 'University of Paris', 'John', 'Milnor', 'USA', 'Male'),
    (1966, 'Fields Medal', 'University of Moscow', 'Michael', 'Atiyah', 'UK', 'Male'),
    (1966, 'Fields Medal', 'Lomonosov Moscow State University', 'Paul', 'Cohen', 'USA', 'Male'),
    (1970, 'Fields Medal', 'University of California, Berkeley', 'Alan', 'Baker', 'UK', 'Male'),
    (1970, 'Fields Medal', 'Institut des Hautes Études Scientifiques', 'Heisuke', 'Hironaka', 'Japan', 'Male'),
    (1974, 'Fields Medal', 'University of Cambridge', 'Enrico', 'Bombieri', 'Italy', 'Male'),
    (1974, 'Fields Medal', 'University of California, Berkeley', 'David', 'Mumford', 'USA', 'Male'),
    (1978, 'Fields Medal', 'University of Chicago', 'Pierre', 'Deligne', 'Belgium', 'Male'),
    (1978, 'Fields Medal', 'Massachusetts Institute of Technology', 'Charles', 'Fefferman', 'USA', 'Male'),
    (1982, 'Fields Medal', 'University of Chicago', 'Alain', 'Connes', 'France', 'Male'),
    (1982, 'Fields Medal', 'Harvard University', 'William', 'Thurston', 'USA', 'Male'),
    (1986, 'Fields Medal', 'University of Oxford', 'Simon', 'Donaldson', 'UK', 'Male'),
    (1986, 'Fields Medal', 'University of California, Berkeley', 'Gerd', 'Faltings', 'Germany', 'Male'),
    (1990, 'Fields Medal', 'Princeton University', 'Vladimir', 'Drinfeld', 'Ukraine', 'Male'),
    (1990, 'Fields Medal', 'University of Cambridge', 'Vaughan', 'Jones', 'New Zealand', 'Male'),
    (1994, 'Fields Medal', 'University of California, Berkeley', 'Jean', 'Bourgain', 'Belgium', 'Male'),
    (1994, 'Fields Medal', 'University of Chicago', 'Efim', 'Zelmanov', 'Russia', 'Male'),
    (1998, 'Fields Medal', 'University of California, Berkeley', 'Richard', 'Borcherds', 'UK', 'Male'),
    (1998, 'Fields Medal', 'Institut des Hautes Études Scientifiques', 'Maxim', 'Kontsevich', 'Russia', 'Male'),
    (2002, 'Fields Medal', 'ETH Zurich', 'Laurent', 'Lafforgue', 'France', 'Male'),
    (2002, 'Fields Medal', 'Institute for Advanced Study', 'Vladimir', 'Voevodsky', 'Russia', 'Male'),
    (2006, 'Fields Medal', 'Université Paris-Sud', 'Andrei', 'Okounkov', 'Russia', 'Male'),
    (2006, 'Fields Medal', 'Université Paris-Sud', 'Grigori', 'Perelman', 'Russia', 'Male'),
    (2010, 'Fields Medal', 'University of California, Berkeley', 'Elon', 'Lindenstrauss', 'Israel', 'Male'),
    (2010, 'Fields Medal', 'Université Pierre-et-Marie-Curie', 'Ngô', 'Bảo Châu', 'Vietnam', 'Male'),
    (2014, 'Fields Medal', 'IMPA', 'Artur', 'Avila', 'Brazil', 'Male'),
    (2014, 'Fields Medal', 'Princeton University', 'Manjul', 'Bhargava', 'USA', 'Male'),
(2014, 'Fields Medal', 'University of Warwick', 'Martin', 'Hairer', 'UK', 'Male'),
    (2014, 'Fields Medal', 'Stanford University', 'Maryam', 'Mirzakhani', 'Iran', 'Female'),
    (2018, 'Fields Medal', 'University of Cambridge', 'Caucher', 'Birkar', 'UK', 'Male'),
    (2018, 'Fields Medal', 'ETH Zurich', 'Alessio', 'Figalli', 'Italy', 'Male'),
    (2018, 'Fields Medal', 'University of Bonn', 'Peter', 'Scholze', 'Germany', 'Male'),
    (2018, 'Fields Medal', 'Institute for Advanced Study', 'Akshay', 'Venkatesh', 'Australia', 'Male'),
    (2022, 'Fields Medal', 'Princeton University', 'June', 'Huh', 'USA', 'Male'),
    (2022, 'Fields Medal', 'University of Oxford', 'James', 'Maynard', 'UK', 'Male'),
    (2022, 'Fields Medal', 'Université Paris-Saclay', 'Hugo', 'Duminil-Copin', 'France', 'Male'),
    (2022, 'Fields Medal', 'University of Copenhagen', 'Maryna', 'Viazovska', 'Ukraine', 'Female'),
    (1975, 'Salem Prize', 'Princeton University', 'Paul', 'Cohen', 'USA', 'Male'),
    (1976, 'Salem Prize', 'Princeton University', 'Elias', 'Stein', 'USA', 'Male'),
    (2022, 'Salem Prize', 'MIT', 'Alexei', 'Borodin', 'Russia', 'Male'),
    (2019, 'Salem Prize', 'UC San Diego', 'Michael H.', 'Freedman', 'USA', 'Male'),
    (1952, 'Abel Prize', 'University of Oslo', 'Atle', 'Selberg', 'Norway', 'Male'),
    (1965, 'Abel Prize', 'Harvard University', 'Raoul', 'Bott', 'USA', 'Male'),
    (2022, 'Abel Prize', 'CUNY', 'Dennis Parnell', 'Sullivan', 'USA', 'Male'),
    (2021, 'Abel Prize', 'Eötvös Loránd University', 'László', 'Lovász', 'Hungary', 'Male')
]

cursor.executemany("""
INSERT INTO awards (year, award_name, university, first_name, last_name, country, gender) 
VALUES (%s, %s, %s, %s, %s, %s, %s)
""", awards_data)

# Создание таблицы регистраций
cursor.execute("""
CREATE TABLE IF NOT EXISTS registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    university VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    award_year INT NOT NULL,
    award_name VARCHAR(255) NOT NULL
)
""")

# Подтверждение изменений
mydb.commit()
cursor.close()
mydb.close()

print("Database and table created, and data inserted successfully.")