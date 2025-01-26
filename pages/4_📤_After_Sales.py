import streamlit as st

# Konfiguration festlegen
st.set_page_config(
    page_title="After Sales",
    page_icon="📤",
)

# Logo
st.logo('images/logos/Uvex_logo.svg', size='large', icon_image='images/logos/uvex_logo_black.svg')

# Page-Überschrift
st.write("# After Sales 📤")

# Tabs aufmachen
tab1, tab2, tab3 = st.tabs(["Service", "🔒 Second-Hand", "🔒 Reparatur"])

# Tab 1: Service
with tab1:
    # Weitere Tabs aufmachen
    tab1_1, tab1_2 = st.tabs(["Reklamation", "Garantie"])

    # Tab 1.1
    with tab1_1:
        with st.form("rekla"):
            # Überschrift: Reklamation
            st.write("#### Reklamation")

            # Einleitungstext
            st.markdown('''##### :orange[Deine suXXeed industry Jacke ist nicht einwandfrei?]''')
            st.write("##### Dann fülle bitte dieses Reklamationsformular aus.")
            st.divider()

            # Eingabefelder
            st.write("###### Persönliche Daten")
            st.text_input("Vor- und Nachname")
            st.text_input("E-Mail-Adresse")
            st.text_input("Telefon")
            st.divider()

            st.write("###### Bestelldetails")
            st.text_input("Bestellnummer")
            st.text_area("Beschreibung des Mangels oder Defekts")
            st.file_uploader("Foto des Mangels oder Defekts")
            st.divider()

            submitted_rekla = st.form_submit_button("Absenden")

            if submitted_rekla:
                st.write("Vielen Dank! Ihre Reklamation wird schnellstmöglich bearbeitet!")
    
    # Tab 1.2
    with tab1_2:
        with st.form("garantie"):
            # Überschrift: Freischaltung erweiterte Garantie
            st.write("#### Freischaltung erweiterte Garantie")

            # Einleitungstext
            st.markdown('''##### :orange[Verlängere jetzt deine Garantiefrist auf 4 Jahre!]''')
            st.write("##### Fülle bitte dieses Formular aus.")
            st.divider()

            # Eingabefelder
            st.write("###### Persönliche Daten")
            st.text_input("Vor- und Nachname")
            st.text_input("E-Mail-Adresse")
            st.text_input("Telefon")
            st.divider()

            st.write("###### Bestelldetails")
            st.text_input("Bestellnummer")
            st.text_input("Bestelldatum")
            st.text_input("Garantiecode", "9456-6711-9903-0072")
            st.divider()

            submitted_garantie = st.form_submit_button("Garantie verlängern")

            if submitted_garantie:
                st.write("Vielen Dank! Die Garantiefrist wurde erfolgreich verlängert!")

# Tab 2: Second-Hand
with tab2:
    # Überschrift: Eingabe Daten zum Weiterverkauf
    st.write("#### Daten zum Weiterverkauf")

# Tab 3: Reparatur
with tab3:
    st.write("#### Informationen zu durchgeführten Reparaturen")