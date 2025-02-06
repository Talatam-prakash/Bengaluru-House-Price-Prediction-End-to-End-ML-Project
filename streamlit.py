import streamlit as st
import numpy as np
import pickle
import json

# Load the trained model and column names.
with open('banglore_home_prices_model.pickle', 'rb') as file:
    model = pickle.load(file)

with open('columns.json', 'r') as file:
    columns = json.load(file)

# Define prediction function.
def predict_price(area_type, location, sqft, bath, bhk):
    location=location.lower()
    try:
        loc_index = columns['data_columns'].index(location)
    except:
        loc_index=4

    df = np.zeros(len(columns['data_columns']))
    area = {"Plot  Area": 0, "Carpet  Area": 1, "Built-up  Area": 2, "Super built-up  Area": 3}
    df[0] = area[area_type]
    df[1] = sqft
    df[2] = bath
    df[3] = bhk
    if loc_index >= 0:
        df[loc_index] = 1

    return model.predict([df])[0]

# Streamlit app
st.title("House Price Prediction")

st.write("Enter the details below to predict the house price.")

# Input fields
area_type = st.selectbox("Select Area Type", ["Plot  Area", "Carpet  Area", "Built-up  Area", "Super built-up  Area"])
location = st.selectbox("Select Location", ["1st phase jp nagar", "2nd phase judicial layout", "5th phase jp nagar", 
                                            "6th phase jp nagar", "7th phase jp nagar", "8th phase jp nagar", "9th phase jp nagar", 
                                            "aecs layout", "abbigere", "akshaya nagar", "ambalipura", "ambedkar nagar",
                                            "amruthahalli", "anandapura", "ananth nagar", "anekal", "anjanapura", "ardendale", "arekere", 
                                            "attibele", "beml layout", "btm 2nd stage", "btm layout", "babusapalaya", "badavala nagar", 
                                            "balagere", "banashankari", "banashankari stage ii", "banashankari stage iii", "banashankari stage v",
                                            "banashankari stage vi", "banaswadi", "bannerghatta", "bannerghatta road", "basavangudi", "basaveshwara nagar", 
                                            "battarahalli", "begur", "begur road", "bellandur", "benson town", "bharathi nagar", "bhoganhalli", "billekahalli",
                                            "binny pete", "bisuvanahalli", "bommanahalli", "bommasandra", "bommasandra industrial area", "bommenahalli", "brookefield", 
                                            "budigere", "cv raman nagar", "chamrajpet", "chandapura", "channasandra", "chikka tirupathi", "chikkabanavar", "chikkalasandra",
                                            "choodasandra", "cooke town", "cox town", "cunningham road", "dasanapura", "dasarahalli", "devanahalli", 
                                            "devarachikkanahalli", "dodda nekkundi", "doddaballapur", "doddakallasandra", "doddathoguru", "domlur", 
                                            "dommasandra", "epip zone", "electronic city", "electronic city phase ii", "electronics city phase 1", "frazer town", 
                                            "gm palaya", "garudachar palya", "gollarapalya hosahalli", "gottigere", "green glen layout", "gubbalala",
                                            "gunjur", "hbr layout", "hrbr layout", "hsr layout", "haralur road", "harlur", "hebbal", "hebbal kempapura",
                                            "hegde nagar", "hennur", "hennur road", "hoodi", "horamavu agara", "horamavu banaswadi", "hormavu", "hosa road", "hosakerehalli",
                                            "hoskote", "hosur road", "hulimavu", "itpl", "iblur village", "indira nagar", "jp nagar", "jakkur", "jalahalli",
                                            "jalahalli east", "jigani", "judicial layout", "kr puram", "kadubeesanahalli", "kadugodi", "kaggadasapura", "kaggalipura", "kaikondrahalli",
                                            "kalena agrahara", "kalyan nagar", "kambipura", "kammanahalli", "kammasandra", "kanakapura", "kanakpura road", "kannamangala", "karuna nagar", 
                                            "kasavanhalli", "kasturi nagar", "kathriguppe", "kaval byrasandra", "kenchenahalli", "kengeri", "kengeri satellite town", "kereguddadahalli", "kodichikkanahalli", "kodigehaali",
                                            "kodihalli", "kogilu", "konanakunte", "koramangala", "kothannur", "kothanur", "kudlu", "kudlu gate", "kumaraswami layout", "kundalahalli", "lb shastri nagar", "lakshminarayana pura", 
                                            "lingadheeranahalli", "magadi road", "mahadevpura", "mallasandra", "malleshpalya", "malleshwaram", "marathahalli", "margondanahalli", "mico layout", "munnekollal",
                                            "murugeshpalya", "mysore road", "ngr layout", "nri layout", "nagarbhavi", "nagavara", "nagavarapalya", "narayanapura", "neeladri nagar", "nehru nagar", "ombr layout",
                                            "old airport road", "old madras road", "padmanabhanagar", "pai layout", "panathur", "parappana agrahara", "pattandur agrahara", "poorna pragna layout", "prithvi layout",
                                            "r.t. nagar", "rachenahalli", "raja rajeshwari nagar", "rajaji nagar", "rajiv nagar", "ramagondanahalli", "ramamurthy nagar", "rayasandra", "sahakara nagar", "sanjay nagar", 
                                            "sarakki nagar", "sarjapur", "sarjapur  road", "sarjapura - attibele road", "sector 2 hsr layout", "sector 7 hsr layout", "seegehalli", "singasandra", "somasundara palya", "sompura",
                                            "sonnenahalli", "subramanyapura", "sultan palaya", "tc palaya", "talaghattapura", "thanisandra", "thigalarapalya", "thubarahalli", "tumkur road", "ulsoor", "uttarahalli", "varthur",
                                            "varthur road", "vasanthapura", "vidyaranyapura", "vijayanagar", "vittasandra", "whitefield", "yelachenahalli", "yelahanka", "yelahanka new town", "yelenahalli", "yeshwanthpur"])
total_sqft = st.number_input("Enter Total Square Feet", min_value=0.0, step=1.0)
bath = st.number_input("Enter Number of Bathrooms", min_value=1, step=1)
bhk = st.number_input("Enter Number of BHK", min_value=1, step=1)

# Predict button
if st.button("Predict Price"):
    try:
        price = predict_price(area_type, location, total_sqft, bath, bhk)
        price=price*100000
        st.success(f"Predicted Price: ₹{price:,.2f}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
