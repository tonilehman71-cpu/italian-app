
import random
import streamlit as st

st.set_page_config(page_title="Il Mio Menù", page_icon="🍝")

st.title("🍝 Italienischer Menü-Berater")

st.info(
    "ℹ️ **Hinweis:** Unser Restaurant ist komplett alkoholfrei. "
    "Wir servieren dir gerne verschiedene Wassersorten "
    "und italienische Erfrischungsgetränke!"
)

# Speisekarte
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

# Alkoholfreie Getränkekarte
getraenkekarte = [
    {
        "name": "Acqua Panna (Stilles Mineralwasser)",
        "kategorie": "Wasser",
    },
    {
        "name": "San Pellegrino (Mineralwasser mit Kohlensäure)",
        "kategorie": "Wasser",
    },
    {
        "name": "San Pellegrino Limonata (Zitronenlimonade)",
        "kategorie": "Erfrischungsgetränk",
    },
    {
        "name": "San Pellegrino Aranciata Rossa (Blutorange)",
        "kategorie": "Erfrischungsgetränk",
    },
    {
        "name": "Chinotto (Italienische Bitterorangen-Limonade)",
        "kategorie": "Erfrischungsgetränk",
    },
    {
        "name": "Hausgemachter Pfirsich-Eistee",
        "kategorie": "Erfrischungsgetränk",
    },
]

# Auswahl des Essens
st.subheader("🍽️ Dein Essen")

kategorie = st.selectbox(
    "Worauf hast du Lust?",
    ["Egal", "Pasta", "Pizza", "Antipasti", "Risotto"]
)

nur_veggie = st.checkbox("Nur vegetarisch")
soll_scharf = st.checkbox("Darf scharf sein")
eher_leicht = st.checkbox("Lieber etwas Leichtes")

# Auswahl der Getränke
st.subheader("🥤 Dein alkoholfreies Getränk")

getraenke_wunsch = st.radio(
    "Was möchtest du dazu trinken?",
    ["Egal", "Wasser", "Erfrischungsgetränk"],
    horizontal=True
)

# Empfehlung erstellen
if st.button("Menü empfehlen!"):

    # Passende Gerichte filtern
    treffer_essen = []

    for gericht in speisekarte:

        if kategorie != "Egal" and gericht["kategorie"] != kategorie:
            continue

        if nur_veggie and not gericht["vegetarisch"]:
            continue

        if soll_scharf and not gericht["scharf"]:
            continue

        if eher_leicht and not gericht["leicht"]:
            continue

        treffer_essen.append(gericht["name"])

    # Passende Getränke filtern
    treffer_getraenke = [
        getraenk["name"]
        for getraenk in getraenkekarte
        if getraenke_wunsch == "Egal"
        or getraenk["kategorie"] == getraenke_wunsch
    ]

    # Ergebnisse anzeigen
    if treffer_essen and treffer_getraenke:

        empfehlung_essen = random.choice(treffer_essen)
        empfehlung_getraenk = random.choice(treffer_getraenke)

        st.success(
            f"Unsere Empfehlung für dich:\n\n"
            f"🍽️ **Gericht:** {empfehlung_essen}\n\n"
            f"🥤 **Alkoholfreies Getränk:** {empfehlung_getraenk}"
        )

    else:
        st.warning(
            "Leider passt kein Gericht exakt zu diesen Filtern."
        )

# Hinweis am Ende
st.caption("🇮🇹 Buon appetito! Wir freuen uns auf deinen Besuch!")
