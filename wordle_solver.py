import requests  # Import requests library for API calls

# Base URL of the Wordle API
BASE_URL = "https://wordle.votee.dev:8000"

def guess_word(mode, guess):
    """
    Makes a guess using the selected mode: 'daily', 'random', or a specific word.
    Returns the API response or handles errors.
    """
    if mode == "daily":
        url = f"{BASE_URL}/daily?guess={guess}"
    elif mode == "random":
        url = f"{BASE_URL}/random?guess={guess}"
    else:  # Custom word mode
        url = f"{BASE_URL}/word/{mode}?guess={guess}"

    response = requests.get(url)  # Send request to API
    
    # Handle different response cases
    if response.status_code == 200:
        return response.json()  # Successful guess
    elif response.status_code == 422:
        print("⚠️ Invalid guess! Please try another word.")  # Invalid word format
        return None
    else:
        print(f"⚠️ Error {response.status_code}: {response.text}")  # Other errors
        return None

def display_feedback(guess, feedback):
    """
    Prints the Wordle-style feedback for the guessed word in a readable format.
    """
    print("\n" + "="*40)
    print(f"🟢 Guess: {guess.upper()}")  # Display guessed word in uppercase
    print("="*40)

    # Loop through feedback and print each letter's result
    for f in feedback:
        letter = f["guess"].upper()  # Convert letter to uppercase for display
        result = f["result"]  # Get feedback result (correct, present, absent)

        # Assign icons for better readability
        if result == "correct":
            status = "✅ Correct"
        elif result == "present":
            status = "🟡 Present (Wrong Position)"
        else:
            status = "❌ Absent"
        
        print(f"  {letter}: {status}")  # Print formatted feedback

    print("="*40 + "\n")  # Add separation line for readability

if __name__ == "__main__":
    """
    Main script execution:
    1. Prompt user for game mode and first guess.
    2. Send the guess to the API and receive feedback.
    3. Display the feedback in a readable format.
    """

    # Get user input for mode (daily, random, or custom)
    mode = input("Enter mode (daily/random/custom): ").strip().lower()
    
    # If custom mode, ask for the specific word to guess against
    if mode == "custom":
        target_word = input("Enter the specific word to guess against: ").strip().lower()
    else:
        target_word = mode  # Use "daily" or "random" directly

    # Prompt user for their word guess
    guess = input("Enter your guess: ").strip().lower()

    # Make the guess using the API
    response = guess_word(target_word, guess)

    # If the response is valid, display feedback
    if response:
        display_feedback(guess, response)
