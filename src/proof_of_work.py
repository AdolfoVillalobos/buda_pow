import random
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()

class ProofOfWork:
  def __init__(self):
      self.pool= os.getenv('STRING_POOL')
      self.string_size = int(os.getenv('STRING_SIZE'))

  def to_hash(self, string):
    return hashlib.sha256(bytes(string, 'utf-8')).hexdigest()

  def sample_candidate(self):
    return "".join(random.choice(self.pool) for _ in range(self.string_size))

  def do(self, target):
    string = ""
    while True:
      string = self.sample_candidate()
      hashed = self.to_hash(string)
      if target in hashed:
        break
    return string, hashed
