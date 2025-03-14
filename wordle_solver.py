import requests

BASE_URL = "https://wordle.votee.dev:8000"

def guess_word(mode="random", guess="table", size=5):
    """
    Makes a guess using the selected mode: 'daily', 'random', or a specific word.
    """
    if mode == "daily":
        url = f"{BASE_URL}/daily?guess={guess}&size={size}"
    elif mode == "random":
        url = f"{BASE_URL}/random?guess={guess}&size={size}"
    else:
        url = f"{BASE_URL}/word/{mode}?guess={guess}"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Example Usage
if __name__ == "__main__":
    mode = "random"  # Can be "daily", "random", or a specific word
    guess = "apple"   # Replace with your guess word
    result = guess_word(mode, guess)
    print("Response:", result)
