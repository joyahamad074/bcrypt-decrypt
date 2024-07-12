# bcrypt-decrypt
bcrypt hash decrypt

## Install dependency:
install bcrypt pip `pip3 install bcrypt`



## Usage:

Edit into the script and replace with your bcrypt hash password
```
# The bcrypt hash you want to crack 
hashed_password = b"$2y$10$faEbIBlG4LOTeear/LeO1uIqrFJ8DkyNd4S4iwM6grrPz7zuEAMTe"
```

Also change the wordlist directory using that you can bruteforce 
```
# Path to your wordlist file
wordlist_path = "path/to/your/wordlist.txt"
```

Use `python3 bcrypt-decrypt.py`
