import requests

BASE_URL = "https://wordle.votee.dev:8000"

def guess_word(mode="random", guess="table"):
    """Make a guess and return the response"""
    url = f"{BASE_URL}/{mode}?guess={guess}" if mode != "random" else f"{BASE_URL}/random?guess={guess}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def filter_words(word_list, feedback):
    """Filter the word list based on feedback"""
    must_have = [f['guess'] for f in feedback if f['result'] == 'correct']
    must_not_have = [f['guess'] for f in feedback if f['result'] == 'absent']
    
    return [
        word for word in word_list 
        if all(ch in word for ch in must_have) and not any(ch in word for ch in must_not_have)
    ]

def display_feedback(guess, feedback):
    """Prints the feedback in a readable format"""
    print("\n" + "="*40)
    print(f"Mode : {mode.upper()}")
    print(f"🟢 Guess: {guess.upper()}")
    print("="*40)

    for f in feedback:
        letter = f["guess"].upper()
        result = f["result"]
        if result == "correct":
            status = "✅ Correct"
        elif result == "present":
            status = "🟡 Present (Wrong Position)"
        else:
            status = "❌ Absent"
        print(f"  {letter}: {status}")

    print("="*40 + "\n")

if __name__ == "__main__":
    mode = "daily"
    guess = "mound"
    response = guess_word(mode, guess)

    if response:
        display_feedback(guess, response)