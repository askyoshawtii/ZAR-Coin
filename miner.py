import hashlib
def mine(block_number, transactions, previous_hash, difficulty):
    prefix = '0' * difficulty
    for nonce in range(10000000): # Nonce search
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = hashlib.sha256(text.encode()).hexdigest()
        if new_hash.startswith(prefix):
            return new_hash, nonce

# Test the function
if __name__ == "__main__":
    result = mine(1, "test transactions", "0000000000000000000000000000000000000000000000000000000000000000", 4)
    print(result)