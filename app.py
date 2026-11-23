import random
import streamlit as st

st.set_page_config(page_title="Il Mio Menù", page_icon="🍝")
st.title("🍝 Italienischer Menü-Berater")

# Deine Speisekarte als Datenbasis
speisekarte = [
    {
        "name": "Spaghetti Carbonara",
        "kategorie": "Pasta",
        "vegetarisch": False,
        "scharf": False,
        "leicht": False,
    },
    {
        "name": "Penne all'Arrabbiata",
        "kategorie": "Pasta",
        "vegetarisch": True,
        "scharf": True,
        "leicht": True,
    },
    {
        "name": "Pizza Margherita",
        "kategorie": "Pizza",
        "vegetarisch": True,
        "scharf": False,
        "leicht": False,
    },
    {
        "name": "Pizza Diavola",
        "kategorie": "Pizza",
        "vegetarisch": False,
        "scharf": True,
        "leicht": False,
    },
    {
        "name": "Caprese (Tomate-Mozzarella)",
        "kategorie": "Antipasti",
        "vegetarisch": True,
        "scharf": False,
        "leicht": True,
    },
    {
        "name": "Risotto ai Funghi",
        "kategorie": "Risotto",
        "vegetarisch": True,
        "scharf": False,
        "leicht": False,
    },
]

# Filter-Optionen für den Nutzer
kategorie = st.selectbox(
    "Worauf hast du Lust?", ["Egal", "Pasta", "Pizza", "Antipasti", "Risotto"]
)
nur_veggie = st.checkbox("Nur vegetarisch")
soll_scharf = st.checkbox("Darf scharf sein")
eher_leicht = st.checkbox("Lieber etwas Leichtes")

if st.button("Gericht empfehlen!"):
  treffer = []
  for gericht in speisekarte:
    if kategorie != "Egal" and gericht["kategorie"] != kategorie:
      continue
    if nur_veggie and not gericht["vegetarisch"]:
      continue
    if soll_scharf and not gericht["scharf"]:
      continue
    if eher_leicht and not gericht["leicht"]:
      continue
    treffer.append(gericht["name"])

  if treffer:
    empfehlung = random.choice(treffer)
    st.success(f"Unsere Empfehlung für dich: **{empfehlung}**")
  else:
    st.warning("Leider passt kein Gericht exakt zu diesen Filtern.")
