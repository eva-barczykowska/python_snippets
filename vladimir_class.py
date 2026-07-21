import pandas as pd
import matplotlib.pyplot as plt

# 1. DATA - Tydenni zaznam kroku (jako tabulka v Excelu)
data = {
    'Den': ['Po', 'Ut', 'St', 'Ct', 'Pa', 'So', 'Ne'],
    'Kroky': [7500, 4200, 9800, 5100, 12000, 15500, 8000]
}

# Prevedeme data do formatu Pandas (DataFrame)
df = pd.DataFrame(data)

# 2. ANALYZA - Pridame logiku (Cil je 10 000 kroku)
cil = 10000
# Vytvori sloupec True/False (neco jako filtr v Excelu)
df['Splneno'] = df['Kroky'] >= cil

# 3. GRAF - Vizualizace vysledku
plt.figure(figsize=(10, 6))

# Nastaveni barev: Zelena pro uspech, cervena pro dny pod cilem
barvy = ['green' if splneno else 'red' for splneno in df['Splneno']]

# Vytvoreni sloupcoveho grafu
plt.bar(df['Den'], df['Kroky'], color=barvy, alpha=0.8)

# Pridani modre prerusovane cary pro cil
plt.axhline(y=cil, color='blue', linestyle='--', label=f'Denní cíl ({cil} kroků)')

# Nastaveni popisku (Styling)
plt.title('Moje pohybová aktivita', fontsize=16)
plt.xlabel('Den v týdnu', fontsize=12)
plt.ylabel('Počet kroků', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle=':', alpha=0.7)

# Zobrazeni grafu v PyCharmu
plt.show()

# 4. BONUS - Vypis do konzole (Filtrovani)
print("--- SHRNUTI TYDNE ---")
print(f"Celkem kroku: {df['Kroky'].sum()}")
print(f"Prumerny pocet: {df['Kroky'].mean():.0f}")
print("\nDny, kdy jsi nesplnil cil:")
print(df[df['Splneno'] == False][['Den', 'Kroky']])



#poznamky
# Den jeden konkrétní sloupec (v Excelu sloupec A), ale v rámci cyklu for se k němu chováme jako k buňce v daném řádku.
# Den jako klíč: V datech (slovníku) je 'Den' název sloupce.
# V cyklu for index, radek in df.iterrows():: Tady je radek (row) celá vodorovná linka dat. Když pak napíšeš radek['Den'], říkáš Pythonu: "Vezmi aktuální řádek a podívej se do sloupce Den."