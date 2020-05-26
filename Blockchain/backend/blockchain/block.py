import time
from backend.util.crypto_hash import crypto_hash
from backend.util.hex_to_binary import hex_to_binary
from backend.config import MINE_RATE

GENESIS_DATA={
    'timestamp':1,
    'last_hash':'genesis_last_hash',
    'hash':'genesis_hash',
    'data':[],
    'difficulty':3,
    'nonce':'genesis_nonce'
    }
'''
def mine_block(last_block,data):
    """
    Mine a block based on data and last_block
    """
    timestamp=time.time_ns()
    hash=f"{timestamp}- {last_block.hash}"
    last_hash=last_block.hash

    return Block(data, timestamp , hash, last_hash)

def genesis():
    return Block("genesis_data", 1, "genesis_hash", "genesis_last_hash")
'''
class Block:
    """
    Block: unit of storage
    """
    def __init__(self, data, timestamp, hash, last_hash, difficulty, nonce):
            self.data=data
            self.timestamp=timestamp
            self.hash=hash
            self.last_hash=last_hash
            self.difficulty=difficulty
            self.nonce=nonce

    def __repr__(self):
        return (
            "Block("
            f"data: {self.data}, "
            f"timestamp: {self.timestamp}, "
            f"hash: {self.hash}, "
            f"last_hash: {self.last_hash}, "
            f"difficulty:{self.difficulty}, "
            f"nonce:{self.nonce})"
            )
    def __eq__(self, other):
        return self.__dict__==other.__dict__

    def to_json(self):
        '''
        Serialize the block into a dictionary of its attributes
        '''
        return self.__dict__
    
    @staticmethod
    def mine_block(last_block,data):
        """
        Mine a block based on data and last_block untill a block hash
        is found that meets
        the leading 0's proof of work requirements.
        """
        timestamp=time.time_ns()
        last_hash=last_block.hash
        difficulty=Block.adjust_difficulty(last_block,timestamp)
        nonce=0
        hash=crypto_hash(timestamp,last_hash,data,difficulty,nonce)
        while hex_to_binary(hash)[0:difficulty] != '0' * difficulty:
            nonce+=1
            timestamp=time.time_ns()
            difficulty = Block.adjust_difficulty(last_block, timestamp)
            hash=crypto_hash(timestamp,last_hash,data,difficulty,nonce)

        return Block(data, timestamp , hash, last_hash, difficulty, nonce)

    @staticmethod
    def genesis():
        '''
        return Block(
                timestamp=GENESIS_DATA['timestamp'],
                last_hash=GENESIS_DATA['last_hash'],
                hash=GENESIS_DATA['hash'],
                data=GENESIS_DATA['data']
                and further added
            )
        '''
        return Block(**GENESIS_DATA)
    @staticmethod
    def from_json(block_json):
        '''
        Deserialize a block's json representation back into a block instance.
        '''
        return Block(**block_json)

    @staticmethod
    def adjust_difficulty(last_block,new_timestamp):
        '''
        calculate the adjust difficulty according to the MINE_RATE.
        Increase the difficulty for quickly mined blocks.
        Decrease the difficulty for slowly mined blocks.
        '''
        if (new_timestamp-last_block.timestamp)< MINE_RATE:
            return last_block.difficulty+1

        if (last_block.difficulty-1)>0:
            return last_block.difficulty-1

        return 1
    
    @staticmethod
    def is_valid_block(last_block, block):
        '''
        validate block by enforcing the following rules:
            -the block must have the proper last_hash reference
            -the block must meet the proof of work requirement
            -the difficulty must only adjust by 1
            -the block hash must be a valid combination of block feilds
        '''
        if block.last_hash !=last_block.hash:
            raise Exception("The block last_hash must be correct")

        if hex_to_binary(block.hash)[0:block.difficulty] != '0'*block.difficulty:
            raise Exception("The proof of work requirement was not met")

        if abs(last_block.difficulty-block.difficulty) > 1:
            raise Exception("The block difficulty must only adjust by 1")

        reconstructed_hash=crypto_hash(
            block.timestamp,
            block.last_hash,
            block.data,
            block.nonce,
            block.difficulty
            )

        if block.hash != reconstructed_hash:
            raise Exception("The block hash must be correct")


def main():
    genesis_block = Block.genesis()
    bad_block = Block.mine_block(Block.genesis(), 'foo')
    bad_block.last_hash = 'evil_data'
    try:
        Block.is_valid_block(genesis_block, bad_block)
    except Exception as e:
        print(f'is_valid_block: {e}')
        
        
if __name__=='__main__':
    main()





















    
