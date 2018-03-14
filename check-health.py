import json
import web3
import os
import logging
import sys

from web3 import Web3, HTTPProvider

SUCCESS_CODE = 0
ERROR_CODE_NOT_ENOUGH_PEERS = 1

# Logger
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


url = os.environ['URL']
if not url:
  raise ValueError("The environment varianle 'URL' is required")


logger.debug('Checking Health for %s', url)
w3 = Web3(HTTPProvider(url))

peer_count = w3.net.peerCount
if peer_count == 0:
  logger.error("There are any peers")
  sys.exit(ERROR_CODE_NOT_ENOUGH_PEERS)
else:
  logger.debug("There are enough peers: %d", peer_count)
  exit(SUCCESS_CODE)