import argparse
import json
from exchange_arb import ExchangeArbitrageEngine

configFile = 'config.json'

f = open(configFile)    
config = json.load(f)
f.close()

print(config)

isMockMode = True

engine = ExchangeArbitrageEngine(config['exchange'], isMockMode)

if engine:
  engine.run()