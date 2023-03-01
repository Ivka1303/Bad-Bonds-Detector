import pandas as pd
import selfies
 
# reading the CSV file
smiles = pd.read_csv('new_smiles.csv')
df = list(smiles.iloc[:, 0]) 

smiles = []

for mol in df:
    checker = True
    translated = False
    while checker:
        try:
            encoded = selfies.encoder(mol)
            translated = True
            break          
        except selfies.exceptions.EncoderError:
            checker = False   
            
    if translated:
        smiles.append(mol)

pd.DataFrame(smiles).to_csv("mynewcsv.csv")