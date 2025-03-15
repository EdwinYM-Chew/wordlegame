import requests

BASE_URL = "https://wordle.votee.dev:8000"

def guess_word(mode, guess):
    """Make a guess and return the response from the API."""
    if mode == "daily":
        url = f"{BASE_URL}/daily?guess={guess}"
    elif mode == "random":
        url = f"{BASE_URL}/random?guess={guess}"
    else:  # Custom word mode
        url = f"{BASE_URL}/word/{mode}?guess={guess}"

    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 422:
        print("⚠️ Invalid guess! Please try another word.")
        return None
    else:
        print(f"⚠️ Error {response.status_code}: {response.text}")
        return None

def display_feedback(guess, feedback):
    """Prints the feedback in a readable format."""
    print("\n" + "="*40)
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
    # Get user input for mode and guess
    mode = input("Enter mode (daily/random/custom): ").strip().lower()
    
    if mode == "custom":
        target_word = input("Enter the specific word to guess against: ").strip().lower()
    else:
        target_word = mode  # Use "daily" or "random" directly

    guess = input("Enter your guess: ").strip().lower()

    # Make the first guess
    response = guess_word(target_word, guess)

    if response:
        display_feedback(guess, response)