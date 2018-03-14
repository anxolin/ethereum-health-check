# Ethereum Health Check
Checks the state of a RPC node in ethereum

Install dependencies:
```bash
python3 -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

Run check:
```bash
URL=https://kovan.infura.io/DyTLJKrhta2BDMSZ9MaV python check-health.py
```