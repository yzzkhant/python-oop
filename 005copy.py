class CryptoProject:
    def __init__ (self, name, blockchain, category):
        self.name = name
        self.blockchain = blockchain
        self.category = category
        
    def display_info(self):
        print(self.name)
        print(self.blockchain)
        print(self.category)
crypto1 = CryptoProject("Uniswap", "Ethereum", "DeFi")
crypto1.display_info()

hello