import random
import time

# Sample trivia questions
questions = {}

# Adding 20 categories with 10 questions each to the questions dictionary
questions.update({
    "World Capitals": [
        {"question": "What is the capital of Argentina?", "answer": "Buenos Aires"},
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is the capital of Japan?", "answer": "Tokyo"},
        {"question": "What is the capital of Canada?", "answer": "Ottawa"},
        {"question": "What is the capital of Australia?", "answer": "Canberra"},
        {"question": "What is the capital of Germany?", "answer": "Berlin"},
        {"question": "What is the capital of Italy?", "answer": "Rome"},
        {"question": "What is the capital of Brazil?", "answer": "Brasília"},
        {"question": "What is the capital of India?", "answer": "New Delhi"},
        {"question": "What is the capital of South Africa?", "answer": "Pretoria"}
    ],
    "Science Facts": [
        {"question": "What planet is known as the Red Planet?", "answer": "Mars"},
        {"question": "What is the chemical symbol for water?", "answer": "H2O"},
        {"question": "What gas do plants absorb from the atmosphere?", "answer": "Carbon Dioxide"},
        {"question": "What is the speed of light in vacuum (m/s)?", "answer": "299792458"},
        {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond"},
        {"question": "What is the chemical symbol for gold?", "answer": "Au"},
        {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
        {"question": "What is the smallest unit of life?", "answer": "Cell"},
        {"question": "What is the chemical symbol for oxygen?", "answer": "O"},
        {"question": "What is the boiling point of water (°C)?", "answer": "100"}
    ],
    "Literature": [
        {"question": "Who wrote 'Romeo and Juliet'?", "answer": "Shakespeare"},
        {"question": "Who wrote '1984'?", "answer": "George Orwell"},
        {"question": "Who wrote 'Pride and Prejudice'?", "answer": "Jane Austen"},
        {"question": "Who wrote 'The Great Gatsby'?", "answer": "F. Scott Fitzgerald"},
        {"question": "Who wrote 'Moby-Dick'?", "answer": "Herman Melville"},
        {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
        {"question": "Who wrote 'The Odyssey'?", "answer": "Homer"},
        {"question": "Who wrote 'War and Peace'?", "answer": "Leo Tolstoy"},
        {"question": "Who wrote 'The Divine Comedy'?", "answer": "Dante Alighieri"},
        {"question": "Who wrote 'The Hobbit'?", "answer": "J.R.R. Tolkien"}
    ],
    "Sports": [
        {"question": "How many players are on a soccer team?", "answer": "11"},
        {"question": "What sport is known as 'America's pastime'?", "answer": "Baseball"},
        {"question": "What is the highest score in a single frame of bowling?", "answer": "30"},
        {"question": "What is the term for a score of zero in tennis?", "answer": "Love"},
        {"question": "What is the national sport of Japan?", "answer": "Sumo Wrestling"},
        {"question": "What is the diameter of a basketball hoop in inches?", "answer": "18"},
        {"question": "What is the only country to play in every World Cup?", "answer": "Brazil"},
        {"question": "What is the maximum score in 10-pin bowling?", "answer": "300"},
        {"question": "What is the length of an Olympic swimming pool in meters?", "answer": "50"},
        {"question": "What is the term for three strikes in a row in bowling?", "answer": "Turkey"}
    ],
    # Add 16 more categories with 10 questions each here
})

# Adding 10 more categories with 10 questions each to the questions dictionary
questions.update({
    "Movies": [
        {"question": "Who directed 'Inception'?", "answer": "Christopher Nolan"},
        {"question": "What is the highest-grossing film of all time?", "answer": "Avatar"},
        {"question": "Who played the Joker in 'The Dark Knight'?", "answer": "Heath Ledger"},
        {"question": "What year was the first 'Star Wars' movie released?", "answer": "1977"},
        {"question": "Who directed 'Pulp Fiction'?", "answer": "Quentin Tarantino"},
        {"question": "What is the name of the hobbit played by Elijah Wood in 'The Lord of the Rings'?", "answer": "Frodo Baggins"},
        {"question": "What is the name of the kingdom in 'Frozen'?", "answer": "Arendelle"},
        {"question": "Who played Jack in 'Titanic'?", "answer": "Leonardo DiCaprio"},
        {"question": "What is the name of the fictional African country in 'Black Panther'?", "answer": "Wakanda"},
        {"question": "Who directed 'Schindler's List'?", "answer": "Steven Spielberg"}
    ],
    "Music": [
        {"question": "Who is known as the King of Pop?", "answer": "Michael Jackson"},
        {"question": "What band was Freddie Mercury the lead singer of?", "answer": "Queen"},
        {"question": "Who is the best-selling female artist of all time?", "answer": "Madonna"},
        {"question": "What is the name of the Beatles' first album?", "answer": "Please Please Me"},
        {"question": "Who sang 'Rolling in the Deep'?", "answer": "Adele"},
        {"question": "What is the name of Elvis Presley's mansion?", "answer": "Graceland"},
        {"question": "Who is the lead singer of U2?", "answer": "Bono"},
        {"question": "What year did MTV launch?", "answer": "1981"},
        {"question": "Who sang 'Bohemian Rhapsody'?", "answer": "Queen"},
        {"question": "What is the best-selling album of all time?", "answer": "Thriller"}
    ],
    "History": [
        {"question": "Who was the first President of the United States?", "answer": "George Washington"},
        {"question": "What year did World War II end?", "answer": "1945"},
        {"question": "Who was known as the Iron Lady?", "answer": "Margaret Thatcher"},
        {"question": "What year did the Berlin Wall fall?", "answer": "1989"},
        {"question": "Who discovered America?", "answer": "Christopher Columbus"},
        {"question": "What was the name of the ship that carried the Pilgrims to America?", "answer": "Mayflower"},
        {"question": "Who was the first man to step on the moon?", "answer": "Neil Armstrong"},
        {"question": "What year was the Declaration of Independence signed?", "answer": "1776"},
        {"question": "Who was the first female Prime Minister of India?", "answer": "Indira Gandhi"},
        {"question": "What was the name of the last Queen of France?", "answer": "Marie Antoinette"}
    ],
    "Geography": [
        {"question": "What is the largest country in the world?", "answer": "Russia"},
        {"question": "What is the smallest country in the world?", "answer": "Vatican City"},
        {"question": "What is the longest river in the world?", "answer": "Nile"},
        {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest"},
        {"question": "What is the largest desert in the world?", "answer": "Sahara"},
        {"question": "What is the capital of Iceland?", "answer": "Reykjavik"},
        {"question": "What is the largest ocean in the world?", "answer": "Pacific Ocean"},
        {"question": "What is the capital of Kenya?", "answer": "Nairobi"},
        {"question": "What is the smallest continent?", "answer": "Australia"},
        {"question": "What is the capital of Thailand?", "answer": "Bangkok"}
    ],
    "Technology": [
        {"question": "Who is the founder of Microsoft?", "answer": "Bill Gates"},
        {"question": "What year was the first iPhone released?", "answer": "2007"},
        {"question": "What does HTTP stand for?", "answer": "HyperText Transfer Protocol"},
        {"question": "Who is the founder of Tesla?", "answer": "Elon Musk"},
        {"question": "What is the name of the first computer virus?", "answer": "Creeper"},
        {"question": "What does CPU stand for?", "answer": "Central Processing Unit"},
        {"question": "What is the name of the first search engine?", "answer": "Archie"},
        {"question": "What year was Facebook founded?", "answer": "2004"},
        {"question": "What does AI stand for?", "answer": "Artificial Intelligence"},
        {"question": "What is the name of the first programming language?", "answer": "Fortran"}
    ],
    "Food": [
        {"question": "What is the main ingredient in guacamole?", "answer": "Avocado"},
        {"question": "What is the most expensive spice in the world?", "answer": "Saffron"},
        {"question": "What is the national dish of Spain?", "answer": "Paella"},
        {"question": "What is the main ingredient in hummus?", "answer": "Chickpeas"},
        {"question": "What is the most consumed beverage in the world?", "answer": "Water"},
        {"question": "What is the main ingredient in sushi?", "answer": "Rice"},
        {"question": "What is the national dish of Italy?", "answer": "Pizza"},
        {"question": "What is the main ingredient in chocolate?", "answer": "Cocoa"},
        {"question": "What is the most popular fruit in the world?", "answer": "Banana"},
        {"question": "What is the main ingredient in bread?", "answer": "Flour"}
    ],
    "Animals": [
        {"question": "What is the largest mammal in the world?", "answer": "Blue Whale"},
        {"question": "What is the fastest land animal?", "answer": "Cheetah"},
        {"question": "What is the largest bird in the world?", "answer": "Ostrich"},
        {"question": "What is the largest reptile in the world?", "answer": "Saltwater Crocodile"},
        {"question": "What is the smallest mammal in the world?", "answer": "Bumblebee Bat"},
        {"question": "What is the most venomous snake in the world?", "answer": "Inland Taipan"},
        {"question": "What is the largest fish in the world?", "answer": "Whale Shark"},
        {"question": "What is the most intelligent animal after humans?", "answer": "Dolphin"},
        {"question": "What is the only mammal capable of true flight?", "answer": "Bat"},
        {"question": "What is the tallest animal in the world?", "answer": "Giraffe"}
    ],
    "Mythology": [
        {"question": "Who is the king of the Greek gods?", "answer": "Zeus"},
        {"question": "Who is the Norse god of thunder?", "answer": "Thor"},
        {"question": "Who is the Roman god of war?", "answer": "Mars"},
        {"question": "Who is the Egyptian god of the sun?", "answer": "Ra"},
        {"question": "Who is the Greek goddess of wisdom?", "answer": "Athena"},
        {"question": "Who is the Norse god of mischief?", "answer": "Loki"},
        {"question": "Who is the Roman goddess of love?", "answer": "Venus"},
        {"question": "Who is the Greek god of the sea?", "answer": "Poseidon"},
        {"question": "Who is the Egyptian god of the underworld?", "answer": "Osiris"},
        {"question": "Who is the Norse god of the dead?", "answer": "Hel"}
    ],
    "Space": [
        {"question": "What is the closest planet to the sun?", "answer": "Mercury"},
        {"question": "What is the largest planet in the solar system?", "answer": "Jupiter"},
        {"question": "What is the smallest planet in the solar system?", "answer": "Mercury"},
        {"question": "What is the name of the galaxy we live in?", "answer": "Milky Way"},
        {"question": "What is the name of the first manned moon landing mission?", "answer": "Apollo 11"},
        {"question": "What is the name of the first artificial satellite?", "answer": "Sputnik"},
        {"question": "What is the name of the largest moon of Saturn?", "answer": "Titan"},
        {"question": "What is the name of the largest volcano in the solar system?", "answer": "Olympus Mons"},
        {"question": "What is the name of the first American astronaut to orbit Earth?", "answer": "John Glenn"},
        {"question": "What is the name of the first woman in space?", "answer": "Valentina Tereshkova"}
    ]
})

# Adding 10 extra questions to each existing category in the questions dictionary
questions["World Capitals"].extend([
    {"question": "What is the capital of Norway?", "answer": "Oslo"},
    {"question": "What is the capital of Sweden?", "answer": "Stockholm"},
    {"question": "What is the capital of Finland?", "answer": "Helsinki"},
    {"question": "What is the capital of Denmark?", "answer": "Copenhagen"},
    {"question": "What is the capital of Poland?", "answer": "Warsaw"},
    {"question": "What is the capital of Greece?", "answer": "Athens"},
    {"question": "What is the capital of Portugal?", "answer": "Lisbon"},
    {"question": "What is the capital of Hungary?", "answer": "Budapest"},
    {"question": "What is the capital of Austria?", "answer": "Vienna"},
    {"question": "What is the capital of the Netherlands?", "answer": "Amsterdam"}
])

questions["Science Facts"].extend([
    {"question": "What is the chemical symbol for sodium?", "answer": "Na"},
    {"question": "What is the chemical symbol for potassium?", "answer": "K"},
    {"question": "What is the chemical symbol for iron?", "answer": "Fe"},
    {"question": "What is the chemical symbol for copper?", "answer": "Cu"},
    {"question": "What is the chemical symbol for zinc?", "answer": "Zn"},
    {"question": "What is the chemical symbol for chlorine?", "answer": "Cl"},
    {"question": "What is the chemical symbol for magnesium?", "answer": "Mg"},
    {"question": "What is the chemical symbol for phosphorus?", "answer": "P"},
    {"question": "What is the chemical symbol for sulfur?", "answer": "S"},
    {"question": "What is the chemical symbol for helium?", "answer": "He"}
])

questions["Literature"].extend([
    {"question": "Who wrote 'Les Misérables'?", "answer": "Victor Hugo"},
    {"question": "Who wrote 'The Scarlet Letter'?", "answer": "Nathaniel Hawthorne"},
    {"question": "Who wrote 'Don Quixote'?", "answer": "Miguel de Cervantes"},
    {"question": "Who wrote 'Frankenstein'?", "answer": "Mary Shelley"},
    {"question": "Who wrote 'The Catcher in the Rye'?", "answer": "J.D. Salinger"},
    {"question": "Who wrote 'The Iliad'?", "answer": "Homer"},
    {"question": "Who wrote 'The Aeneid'?", "answer": "Virgil"},
    {"question": "Who wrote 'The Picture of Dorian Gray'?", "answer": "Oscar Wilde"},
    {"question": "Who wrote 'The Brothers Karamazov'?", "answer": "Fyodor Dostoevsky"},
    {"question": "Who wrote 'Anna Karenina'?", "answer": "Leo Tolstoy"}
])

questions["Sports"].extend([
    {"question": "What is the length of a marathon in miles?", "answer": "26.2"},
    {"question": "What is the national sport of Canada?", "answer": "Lacrosse"},
    {"question": "What is the term for a hole-in-one in golf?", "answer": "Ace"},
    {"question": "What is the maximum score in a single game of darts?", "answer": "180"},
    {"question": "What is the name of the trophy awarded in the NHL?", "answer": "Stanley Cup"},
    {"question": "What is the name of the international cricket championship?", "answer": "Cricket World Cup"},
    {"question": "What is the name of the annual tennis tournament held in London?", "answer": "Wimbledon"},
    {"question": "What is the name of the football competition held every four years?", "answer": "FIFA World Cup"},
    {"question": "What is the name of the basketball league in the USA?", "answer": "NBA"},
    {"question": "What is the name of the famous horse race held in Kentucky?", "answer": "Kentucky Derby"}
])

# Adding 10 extra questions to the remaining categories in the questions dictionary
questions["Movies"].extend([
    {"question": "What is the name of the AI in '2001: A Space Odyssey'?", "answer": "HAL 9000"},
    {"question": "Who directed 'The Godfather'?", "answer": "Francis Ford Coppola"},
    {"question": "What is the name of the ship in 'Titanic'?", "answer": "RMS Titanic"},
    {"question": "Who played Forrest Gump?", "answer": "Tom Hanks"},
    {"question": "What is the name of the wizard in 'The Lord of the Rings'?", "answer": "Gandalf"},
    {"question": "Who directed 'The Shawshank Redemption'?", "answer": "Frank Darabont"},
    {"question": "What is the name of the main character in 'The Matrix'?", "answer": "Neo"},
    {"question": "Who played the lead role in 'Gladiator'?", "answer": "Russell Crowe"},
    {"question": "What is the name of the clown in 'It'?", "answer": "Pennywise"},
    {"question": "Who directed 'Jurassic Park'?", "answer": "Steven Spielberg"}
])

questions["Music"].extend([
    {"question": "Who is the lead singer of Coldplay?", "answer": "Chris Martin"},
    {"question": "What is the name of Beyoncé's debut solo album?", "answer": "Dangerously in Love"},
    {"question": "Who sang 'Shape of You'?", "answer": "Ed Sheeran"},
    {"question": "What is the name of Taylor Swift's first album?", "answer": "Taylor Swift"},
    {"question": "Who is the drummer for The Beatles?", "answer": "Ringo Starr"},
    {"question": "What is the name of the music festival held in California?", "answer": "Coachella"},
    {"question": "Who sang 'Like a Rolling Stone'?", "answer": "Bob Dylan"},
    {"question": "What is the name of the band that sang 'Hotel California'?", "answer": "Eagles"},
    {"question": "Who is the lead singer of The Rolling Stones?", "answer": "Mick Jagger"},
    {"question": "What is the name of the album with the song 'Bohemian Rhapsody'?", "answer": "A Night at the Opera"}
])

questions["History"].extend([
    {"question": "Who was the first Emperor of Rome?", "answer": "Augustus"},
    {"question": "What year did the Titanic sink?", "answer": "1912"},
    {"question": "Who was the first woman to win a Nobel Prize?", "answer": "Marie Curie"},
    {"question": "What year did the American Civil War end?", "answer": "1865"},
    {"question": "Who was the first President of South Africa after apartheid?", "answer": "Nelson Mandela"},
    {"question": "What year did the Soviet Union collapse?", "answer": "1991"},
    {"question": "Who was the British Prime Minister during World War II?", "answer": "Winston Churchill"},
    {"question": "What year did the French Revolution begin?", "answer": "1789"},
    {"question": "Who was the first man to circumnavigate the globe?", "answer": "Ferdinand Magellan"},
    {"question": "What year was the United Nations founded?", "answer": "1945"}
])

questions["Geography"].extend([
    {"question": "What is the capital of New Zealand?", "answer": "Wellington"},
    {"question": "What is the capital of South Korea?", "answer": "Seoul"},
    {"question": "What is the capital of Saudi Arabia?", "answer": "Riyadh"},
    {"question": "What is the capital of Mexico?", "answer": "Mexico City"},
    {"question": "What is the capital of Chile?", "answer": "Santiago"},
    {"question": "What is the capital of Egypt?", "answer": "Cairo"},
    {"question": "What is the capital of Turkey?", "answer": "Ankara"},
    {"question": "What is the capital of Switzerland?", "answer": "Bern"},
    {"question": "What is the capital of Ireland?", "answer": "Dublin"},
    {"question": "What is the capital of Belgium?", "answer": "Brussels"}
])

questions["Technology"].extend([
    {"question": "What does GPU stand for?", "answer": "Graphics Processing Unit"},
    {"question": "What year was Google founded?", "answer": "1998"},
    {"question": "What does RAM stand for?", "answer": "Random Access Memory"},
    {"question": "Who is the founder of Amazon?", "answer": "Jeff Bezos"},
    {"question": "What is the name of the first video game?", "answer": "Pong"},
    {"question": "What does URL stand for?", "answer": "Uniform Resource Locator"},
    {"question": "What year was YouTube founded?", "answer": "2005"},
    {"question": "What is the name of the first smartphone?", "answer": "IBM Simon"},
    {"question": "What does SSD stand for?", "answer": "Solid State Drive"},
    {"question": "What is the name of the first social media platform?", "answer": "Six Degrees"}
])

questions["Food"].extend([
    {"question": "What is the main ingredient in miso soup?", "answer": "Miso"},
    {"question": "What is the national dish of Japan?", "answer": "Sushi"},
    {"question": "What is the main ingredient in pesto?", "answer": "Basil"},
    {"question": "What is the main ingredient in risotto?", "answer": "Rice"},
    {"question": "What is the main ingredient in tzatziki?", "answer": "Yogurt"},
    {"question": "What is the main ingredient in falafel?", "answer": "Chickpeas"},
    {"question": "What is the main ingredient in kimchi?", "answer": "Cabbage"},
    {"question": "What is the main ingredient in ramen?", "answer": "Noodles"},
    {"question": "What is the main ingredient in pho?", "answer": "Noodles"},
    {"question": "What is the main ingredient in curry?", "answer": "Spices"}
])

questions["Animals"].extend([
    {"question": "What is the name of the fastest bird?", "answer": "Peregrine Falcon"},
    {"question": "What is the name of the largest land carnivore?", "answer": "Polar Bear"},
    {"question": "What is the name of the largest rodent?", "answer": "Capybara"},
    {"question": "What is the name of the largest amphibian?", "answer": "Chinese Giant Salamander"},
    {"question": "What is the name of the largest invertebrate?", "answer": "Colossal Squid"},
    {"question": "What is the name of the largest marsupial?", "answer": "Red Kangaroo"},
    {"question": "What is the name of the largest primate?", "answer": "Gorilla"},
    {"question": "What is the name of the largest snake?", "answer": "Green Anaconda"},
    {"question": "What is the name of the largest turtle?", "answer": "Leatherback Sea Turtle"},
    {"question": "What is the name of the largest bat?", "answer": "Flying Fox"}
])

questions["Mythology"].extend([
    {"question": "Who is the Greek god of the underworld?", "answer": "Hades"},
    {"question": "Who is the Norse god of wisdom?", "answer": "Odin"},
    {"question": "Who is the Roman god of the sea?", "answer": "Neptune"},
    {"question": "Who is the Egyptian goddess of love?", "answer": "Hathor"},
    {"question": "Who is the Greek god of war?", "answer": "Ares"},
    {"question": "Who is the Norse goddess of love?", "answer": "Freyja"},
    {"question": "Who is the Roman god of the underworld?", "answer": "Pluto"},
    {"question": "Who is the Egyptian god of chaos?", "answer": "Set"},
    {"question": "Who is the Greek god of wine?", "answer": "Dionysus"},
    {"question": "Who is the Norse god of the sun?", "answer": "Sol"}
])

questions["Space"].extend([
    {"question": "What is the name of the first human in space?", "answer": "Yuri Gagarin"},
    {"question": "What is the name of the first American in space?", "answer": "Alan Shepard"},
    {"question": "What is the name of the first spacecraft to land on the moon?", "answer": "Luna 2"},
    {"question": "What is the name of the first spacecraft to orbit the moon?", "answer": "Luna 10"},
    {"question": "What is the name of the first spacecraft to land on Mars?", "answer": "Viking 1"},
    {"question": "What is the name of the first spacecraft to orbit Mars?", "answer": "Mariner 9"},
    {"question": "What is the name of the first spacecraft to land on Venus?", "answer": "Venera 7"},
    {"question": "What is the name of the first spacecraft to orbit Venus?", "answer": "Mariner 2"},
    {"question": "What is the name of the first spacecraft to land on Jupiter?", "answer": "Galileo"},
    {"question": "What is the name of the first spacecraft to orbit Jupiter?", "answer": "Galileo"}
])

# Update the grid to display actual category names
category_names = list(questions.keys())
grid = [category_names[i:i + 10] for i in range(0, len(category_names), 10)]

# Display the grid
def display_grid(grid):
    for row in grid:
        print(" | ".join(row))
    print("\n")

# Update the trivia_battle function to ensure questions do not repeat within the same category
def trivia_battle(category):
    if category in questions:
        print(f"You have 60 seconds to answer as many questions as possible in the category: {category}")
        start_time = time.time()
        correct_answers = 0
        used_questions = set()

        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time >= 60:
                break

            # Filter out already used questions
            available_questions = [q for q in questions[category] if q["question"] not in used_questions]
            if not available_questions:
                print("No more questions available in this category.")
                break

            question_data = random.choice(available_questions)
            used_questions.add(question_data["question"])

            q = question_data["question"]
            correct_answer = question_data["answer"]
            print(f"Question: {q}")
            player_answer = input("Your Answer: ")
            if player_answer.strip().lower() == correct_answer.lower():
                print("Correct!")
                correct_answers += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")

        print(f"Time's up! You answered {correct_answers} questions correctly.")
        return correct_answers
    else:
        print("No questions available for this category.")
        return 0

# Update the gameplay loop to reflect the new structure
def gameplay_loop():
    display_grid(grid)
    selected_category = input("Select a category from the grid: ").strip().lower()
    matching_category = next((cat for cat in questions if cat.lower() == selected_category), None)
    if matching_category:
        correct_answers = trivia_battle(matching_category)
        print(f"You scored {correct_answers} points in the category: {matching_category}.")
    else:
        print("Invalid category. Please select a valid category from the grid.")

# Start the gameplay loop
gameplay_loop()