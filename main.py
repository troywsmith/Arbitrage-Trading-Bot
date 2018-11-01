import argparse
import json

configFile = 'config.json'

f = open(configFile)    
config = json.load(f)
f.close()
