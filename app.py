import streamlit as st
import requests
import json

# ------------------------------
# PAGE CONFIG & LOGIN
# ------------------------------
st.set_page_config(page_title="GraphQL API Explorer", layout="wide")

def show_earth_symbol(width=100):
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; margin-bottom: 1rem;">
            <span style="font-size: {width}px;">🌍</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.caption("GlobalInternet.py – Earth symbol")

# Authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #0b3d5f, #1a6d8f);
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("🔐 Login Required")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        show_earth_symbol(150)
        st.markdown("<h2 style='text-align: center;'>GraphQL API Explorer</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>by GlobalInternet.py</p>", unsafe_allow_html=True)
        password_input = st.text_input("Enter password to access", type="password")
        if st.button("Login"):
            if password_input == "20082010":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect password. Access denied.")
    st.stop()

# ------------------------------
# AFTER LOGIN – MAIN APP (blue theme)
# ------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0b3d5f, #1a6d8f);
    }
    .main-header {
        background: rgba(255,255,255,0.1);
        padding: 1.5rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 1rem;
        backdrop-filter: blur(5px);
    }
    .main-header h1 { color: white; margin: 0; font-size: 2.5rem; }
    .main-header p { color: #FFD700; margin: 0; font-size: 1.1rem; }
    .download-btn { background-color: #28a745; color: white; padding: 10px 20px; border-radius: 30px; text-decoration: none; font-weight: bold; display: inline-block; }
    .footer { text-align: center; color: #ccc; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #ccc; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<div class="main-header">
    <h1>🌍 GraphQL API Explorer</h1>
    <p>Write queries, run against real APIs, explore data</p>
</div>
""", unsafe_allow_html=True)

col_flag, col_title = st.columns([1, 3])
with col_flag:
    show_earth_symbol(120)
with col_title:
    st.markdown("<p style='font-size:1.1rem; color:white;'>🔍 Test GraphQL queries using the public Countries API (or any GraphQL endpoint).</p>", unsafe_allow_html=True)

# ------------------------------
# SIDEBAR – COMPANY INFO & LOGOUT
# ------------------------------
with st.sidebar:
    st.markdown("## 🌍 GlobalInternet.py")
    show_earth_symbol(80)
    st.markdown("### GraphQL Explorer")
    st.markdown("---")
    st.markdown("**Founder & Developer:**")
    st.markdown("Gesner Deslandes")
    st.markdown("📞 **WhatsApp:** [509 4738-5663](https://wa.me/50947385663)")
    st.markdown("📧 **Email:** deslandes78@gmail.com")
    st.markdown("🌐 **Main website:** [globalinternetsitepy...](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
    st.markdown("---")
    st.markdown("### 💰 Price")
    st.markdown("**$1,200 USD** (one‑time license, includes source code, setup, and 1 year support)")
    st.markdown("---")
    st.markdown("### © 2025 GlobalInternet.py")
    st.markdown("All Rights Reserved")
    st.markdown("---")
    if st.button("🚪 Logout", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# ------------------------------
# MULTI-LANGUAGE SUPPORT
# ------------------------------
LANGUAGES = {"English":"en","Español":"es","Français":"fr","Kreyòl Ayisyen":"ht"}
TEXTS = {
    "en": {
        "api_endpoint": "🌐 GraphQL Endpoint",
        "query_label": "📝 GraphQL Query",
        "run_btn": "▶️ Run Query",
        "response_title": "📊 Response",
        "default_endpoint": "https://countries.trevorblades.com/",
        "default_query": "{\n  countries {\n    code\n    name\n    continent {\n      name\n    }\n  }\n}",
        "error_msg": "Error: Could not fetch data. Check endpoint or query syntax.",
        "success_msg": "Query executed successfully."
    },
    "es": {
        "api_endpoint": "🌐 Punto final GraphQL",
        "query_label": "📝 Consulta GraphQL",
        "run_btn": "▶️ Ejecutar consulta",
        "response_title": "📊 Respuesta",
        "default_endpoint": "https://countries.trevorblades.com/",
        "default_query": "{\n  countries {\n    code\n    name\n    continent {\n      name\n    }\n  }\n}",
        "error_msg": "Error: No se pudieron obtener los datos. Verifique el punto final o la sintaxis de la consulta.",
        "success_msg": "Consulta ejecutada con éxito."
    },
    "fr": {
        "api_endpoint": "🌐 Point d'accès GraphQL",
        "query_label": "📝 Requête GraphQL",
        "run_btn": "▶️ Exécuter la requête",
        "response_title": "📊 Réponse",
        "default_endpoint": "https://countries.trevorblades.com/",
        "default_query": "{\n  countries {\n    code\n    name\n    continent {\n      name\n    }\n  }\n}",
        "error_msg": "Erreur : Impossible de récupérer les données. Vérifiez le point d'accès ou la syntaxe de la requête.",
        "success_msg": "Requête exécutée avec succès."
    },
    "ht": {
        "api_endpoint": "🌐 Pwen GraphQL",
        "query_label": "📝 Rekèt GraphQL",
        "run_btn": "▶️ Kouri rekèt",
        "response_title": "📊 Repons",
        "default_endpoint": "https://countries.trevorblades.com/",
        "default_query": "{\n  countries {\n    code\n    name\n    continent {\n      name\n    }\n  }\n}",
        "error_msg": "Erè: Pa t kapab chache done yo. Tcheke pwen an oswa sentaks rekèt la.",
        "success_msg": "Rekèt egzekite avèk siksè."
    }
}
def get_text(key):
    lang = st.session_state.get("language", "en")
    return TEXTS[lang].get(key, TEXTS["en"].get(key, key))

lang_choice = st.sidebar.selectbox("🌐 Language", list(LANGUAGES.keys()))
st.session_state["language"] = LANGUAGES[lang_choice]

# ------------------------------
# GRAPHQL EXPLORER UI
# ------------------------------
st.markdown("---")
endpoint = st.text_input(get_text("api_endpoint"), value=get_text("default_endpoint"))
query = st.text_area(get_text("query_label"), value=get_text("default_query"), height=300)

if st.button(get_text("run_btn"), use_container_width=True):
    if not endpoint or not query:
        st.warning("Please provide both endpoint and query.")
    else:
        with st.spinner("Sending query..."):
            try:
                # Set proper headers for GraphQL
                headers = {"Content-Type": "application/json"}
                response = requests.post(endpoint, json={"query": query}, headers=headers, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    st.success(get_text("success_msg"))
                    st.subheader(get_text("response_title"))
                    st.json(data)
                else:
                    st.error(f"HTTP {response.status_code}: {response.text}")
            except requests.exceptions.Timeout:
                st.error("Request timed out. Please try again.")
            except requests.exceptions.ConnectionError:
                st.error("Connection error. Check the endpoint URL.")
            except Exception as e:
                st.error(f"{get_text('error_msg')} Details: {e}")

st.markdown("---")
st.markdown("📘 **Example query:** Get a list of all countries with their code, name, and continent. You can modify the query or change the endpoint to any public GraphQL API (e.g., SpaceX, GitHub, etc.).")

# Footer
st.markdown('<div class="footer">🌍 *GlobalInternet.py – GraphQL API Explorer* 🌍</div>', unsafe_allow_html=True)
