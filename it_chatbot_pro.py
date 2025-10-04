# it_chatbot_pro.py
import random

class ITChatBot:
    def __init__(self, name="TechBot"):
        self.name = name
        self.memory = []  # Store conversation history

        # Knowledge base
        self.responses = {
            "greeting": ["Hello!", "Hi there!", "Hey!", "Greetings!", "Nice to meet you!"],
            "farewell": ["Goodbye!", "See you later!", "Take care!", "Bye 👋"],

            # Programming
            "languages": "Popular programming languages include Python, Java, C++, JavaScript, and Go.",
            "python": "Python is widely used in AI, ML, web dev, and automation. It's beginner-friendly and powerful.",
            "java": "Java is object-oriented and platform-independent. It’s used in Android apps, banking, and enterprise apps.",
            "loop": "A loop is used to repeat a block of code. Common types are for, while, and do-while loops.",
            "inheritance": "Inheritance in OOP allows one class to acquire properties and methods of another class.",
            "api": "An API (Application Programming Interface) allows two applications to communicate with each other.",
            "compiler": "A compiler translates high-level source code into machine code so the computer can execute it.",

            # Networking
            "networking": "Networking connects computers and devices to share data. Examples: LAN, WAN, TCP/IP, DNS, VPNs.",
            "ip": "An IP (Internet Protocol) address uniquely identifies a device on a network.",
            "http": "HTTP (HyperText Transfer Protocol) is the foundation of data transfer on the web.",
            "dns": "DNS (Domain Name System) translates human-friendly domain names (like google.com) into IP addresses.",

            # Databases
            "database": "Databases store and organize data. Examples: MySQL, PostgreSQL, MongoDB, Oracle.",
            "sql": "SQL (Structured Query Language) is used to query and manage relational databases.",
            "nosql": "NoSQL databases (like MongoDB) handle unstructured data and scale easily for big data apps.",

            # Cybersecurity
            "cybersecurity": "Cybersecurity protects systems from attacks. Techniques: firewalls, encryption, MFA, antivirus.",
            "phishing": "Phishing is a cyberattack where attackers trick users into revealing personal info via fake emails/websites.",
            "encryption": "Encryption converts data into a secure code, preventing unauthorized access.",
            "firewall": "A firewall filters network traffic and blocks malicious connections.",

            # AI & ML
            "ai": "Artificial Intelligence enables machines to simulate human intelligence. Example: chatbots, recommendation systems.",
            "ml": "Machine Learning is a subset of AI that learns from data to make predictions.",
            "deep learning": "Deep Learning is a type of ML using neural networks with many layers for complex tasks.",
            "nlp": "Natural Language Processing (NLP) enables machines to understand and generate human language.",

            # Cloud & OS
            "cloud": "Cloud computing delivers services (servers, storage, databases) via the internet. Examples: AWS, Azure, GCP.",
            "os": "An Operating System manages hardware and software. Examples: Windows, Linux, macOS, Android.",
            "linux": "Linux is an open-source OS widely used in servers, cloud, and cybersecurity.",
            "windows": "Windows is a popular OS developed by Microsoft, widely used in desktops and enterprises.",

            # Software Engineering
            "sdlc": "The Software Development Life Cycle (SDLC) includes steps: planning, designing, coding, testing, deployment.",
            "agile": "Agile is a software dev methodology focusing on iterative progress, collaboration, and flexibility.",
            "git": "Git is a version control system that tracks changes in code and helps in collaboration.",
            "devops": "DevOps integrates development and operations for faster, continuous delivery of software."
        }

        # Fallback responses
        self.fallback_responses = [
            "Hmm... I don’t know that yet. Try asking about programming, networking, databases, AI, or cybersecurity.",
            "Sorry, I didn’t get that. Can you rephrase?",
            "Interesting! But I only know IT-related topics.",
            "Let’s stick to IT knowledge 🙂"
        ]

    def get_response(self, user_input):
        user_input = user_input.lower()
        self.memory.append(("user", user_input))

        # Exit
        if user_input in ["bye", "exit", "quit"]:
            return random.choice(self.responses["farewell"]), True

        # Greetings
        if any(word in user_input for word in ["hi", "hello", "hey", "good morning", "good evening"]):
            return random.choice(self.responses["greeting"]), False

        # Memory recall
        if "repeat" in user_input:
            for msg in reversed(self.memory):
                if msg[0] == "bot":
                    return f"You previously heard me say: '{msg[1]}'", False

        # Small talk
        if "how are you" in user_input:
            return "I’m doing great as a bot 🤖! How about you?", False
        if "your name" in user_input:
            return f"I am {self.name}, your IT knowledge assistant.", False
        if "who created you" in user_input:
            return "I was created by students as part of an IT chatbot project!", False

        # Keyword matching
        for keyword, response in self.responses.items():
            if keyword in user_input:
                return response, False

        # Fallback
        return random.choice(self.fallback_responses), False

    def run(self):
        print(f"🤖 {self.name}: Hello! I’m {self.name}, your IT knowledge chatbot.")
        print("Ask me about programming, networking, databases, cybersecurity, AI, cloud, OS, or software engineering. Type 'bye' to exit.\n")
        while True:
            user_input = input("You: ")
            response, end = self.get_response(user_input)
            print(f"🤖 {self.name}: {response}")
            self.memory.append(("bot", response))
            if end:
                break


if __name__ == "__main__":
    bot = ITChatBot("TechBot")
    bot.run()
