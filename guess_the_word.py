import random

def guess_the_word():
    # Words with hints
    words_with_hints = {
        "python": "🐍 A popular programming language.",
        "scratch": "🐱 A block-based coding language for kids.",
        "school": "🏫 A place where you learn new things.",
        "teacher": "👩‍🏫 A person who helps you learn.",
        "robot": "🤖 A machine that can follow instructions.",
        "coding": "💻 The skill of telling computers what to do."
    }
    
    word, hint = random.choice(list(words_with_hints.items()))
    guessed = ["_"] * len(word)  
    attempts = 7  
    score = 0  
    
    print("🌟 Welcome to Guess the Word ! 🌟")
    print("Try to guess the word letter by letter.")
    print(f"💡 Hint: {hint}")
    
    while attempts > 0 and "_" in guessed:
        print("\nWord: ", " ".join(guessed))
        print(f"❤️ Attempts left: {attempts} | ⭐ Score: {score}")
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single letter.")
            continue
        
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            score += 10  
            print("✅ Great job! You found a letter!")
        else:
            attempts -= 1
            score -= 5
            print("❌ Oops! That letter isn’t in the word.")
    
    if "_" not in guessed:
        print(f"\n🎉 Congratulations! You guessed the word: {word}")
        print(f"🏆 Final Score: {score}")
    else:
        print(f"\n😢 Game over! The word was: {word}")
        print(f"⭐ Final Score: {score}")


guess_the_word()
