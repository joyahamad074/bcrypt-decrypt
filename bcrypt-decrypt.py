import bcrypt
import concurrent.futures

# The bcrypt hash you want to crack
hashed_password = b"$2y$10$faEbIBlG4LOTeear/LeO1uIqrFJ8DkyNd4S4iwM6grrPz7zuEAMTe"

# Path to your wordlist file
wordlist_path = "path/to/your/wordlist.txt"

# Function to check a single password
def check_password(hash, password):
    return bcrypt.checkpw(password.encode('utf-8'), hash)

# Function to process a chunk of the wordlist
def process_chunk(hash, chunk):
    for password in chunk:
        if check_password(hash, password):
            return password
    return None

def crack_password(hash, wordlist, num_threads=4):
    with open(wordlist, 'r', errors='ignore') as file:
        passwords = [line.strip() for line in file]
    
    chunk_size = len(passwords) // num_threads
    chunks = [passwords[i:i + chunk_size] for i in range(0, len(passwords), chunk_size)]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_chunk = {executor.submit(process_chunk, hash, chunk): chunk for chunk in chunks}
        for future in concurrent.futures.as_completed(future_to_chunk):
            result = future.result()
            if result:
                return result
    return None

# Attempt to crack the password
cracked_password = crack_password(hashed_password, wordlist_path, num_threads=8)

if cracked_password:
    print(f"Password found: {cracked_password}")
else:
    print("Password not found in wordlist.")
