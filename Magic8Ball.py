#Magic8Ball.py
#Name:abbas bashir
#Date:02/3/2025
#Assignment:lab 2


import random

def main():
    # List of possible Magic 8 Ball responses
    answers = [
        "As I see it, yes.", "Ask again later.", "Better not tell you now.",
        "Cannot predict now.", "Concentrate and ask again.", "Dont count on it.",
        "It is certain.", "It is decidedly so.", "Most likely.",
        "My reply is no.", "My sources say no.", "Outlook not so good.",
        "Outlook good.", "Reply hazy, try again.", "Signs point to yes.",
        "Very doubtful.", "Without a doubt.", "Yes.",
        "Yes  definitely.", "You may rely on it."
    ]

    print("🎱 Magic 8 Ball 🎱")
    
    
    input("Ask the Magic 8 Ball a yes/no question: ")

    # Select a random response
    response = random.choice( )

    # Display the response
    print("\nMagic 8 Ball says:", response)

if __name__ == '__main__':
    main()
