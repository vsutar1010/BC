import hashlib
import json

class Block:

    def __init__(self, index, data, previous_hash):

        self.index = index
        self.data = data
        self.previous_hash = previous_hash

        self.hash = self.calculate_hash()

    def calculate_hash(self):

        block_data = json.dumps({
            "index": self.index,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True)

        return hashlib.sha256(
            block_data.encode()
        ).hexdigest()


class Blockchain:

    def __init__(self):

        self.chain = []

        genesis = Block(0, "Genesis Block", "0")

        self.chain.append(genesis)

    def add_block(self, data):

        previous = self.chain[-1]

        new_block = Block(
            len(self.chain),
            data,
            previous.hash
        )

        self.chain.append(new_block)

    def display_chain(self):

        for block in self.chain:

            print("Block:", block.index)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Hash:", block.hash)
            print("-------------------")


bc = Blockchain()

bc.add_block("Vaibhav sends 100 to Rahul")
bc.add_block("Rahul sends 50 to Amit")

bc.display_chain()