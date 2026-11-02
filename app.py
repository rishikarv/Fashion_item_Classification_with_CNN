
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Fabriq",
    page_icon="👗",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background: #090B12;
    color: #F8FAFC;
}

/* Page spacing */
.block-container {
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Hero section */
.hero {
    text-align: center;
    padding: 10px 0 25px 0;
}

.hero h1 {
    color: #F8FAFC;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 8px;
    letter-spacing: -1px;
}

.hero p:first-of-type {
    color: #B8A5FF;
    font-size: 19px;
    font-weight: 600;
    margin-top: 5px;
    margin-bottom: 8px;
}

.hero p:last-of-type {
    color: #A7AEC0;
    font-size: 15px;
    font-weight: 400;
    margin-top: 0;
}
/* Welcome card */
.welcome {
    background: linear-gradient(135deg, #171827, #211B35);
    border: 1px solid #44365F;
    border-radius: 16px;
    padding: 24px;
    margin: 15px 0 30px 0;
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}

.welcome h3 {
    color: #FFFFFF;
    margin-top: 0;
}

.welcome p {
    color: #CBD0DC;
    line-height: 1.7;
}

.welcome .details {
    color: #B8A5FF;
    font-weight: 600;
    font-size: 14px;
}

/* Section headings */
.stApp h2,
.stApp h3 {
    color: #F8FAFC;
}

/* Upload area */
[data-testid="stFileUploader"] {
    background: #141722;
    border: 1px dashed #8066C9;
    border-radius: 14px;
    padding: 14px;
    transition: all 0.3s ease;
}

[data-testid="stFileUploader"]:hover {
    border-color: #B8A5FF;
    background: #19182A;
}

[data-testid="stFileUploader"] section {
    background: transparent !important;
}

/* Browse files button */
[data-testid="stFileUploader"] button {
    background: #292343 !important;
    color: #E9DFFF !important;
    border: 1px solid #8066C9 !important;
    border-radius: 9px !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

[data-testid="stFileUploader"] button:hover {
    background: #8066C9 !important;
    color: #FFFFFF !important;
    border-color: #B8A5FF !important;
    box-shadow: 0 0 14px rgba(128, 102, 201, 0.4);
}

/* Upload text */
[data-testid="stFileUploader"] label,
[data-testid="stFileUploader"] small {
    color: #CBD5E1 !important;
}

/* Image preview */
[data-testid="stImage"] img {
    border-radius: 14px;
    border: 1px solid #44365F;
}

/* Predict button */
div.stButton > button {
    background: linear-gradient(135deg, #7054C8, #9273E8) !important;
    color: #FFFFFF !important;
    border: 1px solid #A78BFA !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    width: 100%;
    padding: 12px;
    transition: all 0.3s ease !important;
}

div.stButton > button:hover {
    background: linear-gradient(135deg, #9273E8, #B49AFF) !important;
    color: #FFFFFF !important;
    border: 1px solid #D0BCFF !important;
    box-shadow: 0 0 18px rgba(167,139,250,0.4);
    transform: translateY(-2px);
}

/* Prediction result */
.result-card {
    background: linear-gradient(135deg, #171827, #211B35);
    border: 1px solid #8066C9;
    border-radius: 16px;
    padding: 28px;
    text-align: center;
    margin-top: 10px;
    box-shadow: 0 8px 25px rgba(100,70,180,0.12);
}

.result-label {
    color: #A7AEC0;
    font-size: 13px;
    letter-spacing: 2px;
    font-weight: 600;
}

.result-name {
    color: #C5A5FF;
    font-size: 32px;
    font-weight: 800;
    margin: 12px 0;
}

.result-score {
    color: #FFFFFF;
    font-size: 36px;
    font-weight: 800;
    margin-bottom: 0;
}

.result-caption {
    color: #A7AEC0;
    font-size: 13px;
}

/* Model information cards */
.info-card {
    background: #151827;
    border: 1px solid #393052;
    border-radius: 12px;
    padding: 17px 10px;
    text-align: center;
    min-height: 105px;
}

.info-card .value {
    color: #C5A5FF;
    font-size: 23px;
    font-weight: 800;
}

.info-card .label {
    color: #A7AEC0;
    font-size: 12px;
    margin-top: 5px;
}

/* Expander */
[data-testid="stExpander"] {
    background: #141722;
    border: 1px solid #393052;
    border-radius: 12px;
}

/* Alerts */
[data-testid="stAlert"] {
    background: #171D2B !important;
    color: #DCE5F5 !important;
    border: 1px solid #35415D !important;
    border-radius: 10px;
}

/* Progress bar */
.stProgress > div > div > div {
    background: #9273E8 !important;
}

/* Header and toolbar */
[data-testid="stHeader"],
[data-testid="stToolbar"] {
    background: #090B12;
}

/* Deploy button */
[data-testid="stAppDeployButton"] {
    background: #090B12;
    color: #FFFFFF;
}

[data-testid="stAppDeployButton"] * {
    color: #FFFFFF !important;
}

/* Status widget */
[data-testid="stStatusWidget"] {
    background-color: #090B12 !important;
    color: #FFFFFF !important;
}

[data-testid="stStatusWidget"] * {
    color: #FFFFFF !important;
}

/* Divider */
hr {
    border-color: #343047;
}

/* Footer */
.footer {
    text-align: center;
    color: #9295A5;
    font-size: 13px;
    line-height: 1.8;
    padding: 20px 10px;
}

/* Spinner */
.stSpinner > div {
    border-top-color: #B8A5FF !important;
}

</style>
""", unsafe_allow_html=True)


# ---------------- CLASS NAMES ----------------

class_names = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot"
]


# ---------------- LOAD MODEL ----------------

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(
        "fashion_cnn_model.keras"
    )

model = load_model()


# ---------------- HERO SECTION ----------------
st.markdown("""
<div class="hero">
    <h1>👗 Fabriq</h1>
    <p>A Smarter Way to Recognize Fashion</p>
    <p>Discover clothing categories using Deep Learning & CNN</p>
</div>
""", unsafe_allow_html=True)


# ---------------- WELCOME SECTION ----------------

welcome_html = """
<div class="welcome">
<h3>✨Welcome to Fabriq</h3>
<p>
Upload a fashion image and let our Convolutional Neural Network
identify its category. Our deep learning model recognizes
10 fashion categories using the Fashion-MNIST dataset.
</p>

</div>
"""

st.markdown(welcome_html, unsafe_allow_html=True)


# ---------------- MODEL INFORMATION ----------------

st.markdown("### 🧠 Model Information")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="info-card">
        <div class="value">CNN</div>
        <div class="label">Model Architecture</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <div class="value">90.47%</div>
        <div class="label">Test Accuracy</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <div class="value">10</div>
        <div class="label">Fashion Classes</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="info-card">
        <div class="value">28×28</div>
        <div class="label">Input Image Size</div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("---")


# ---------------- IMAGE UPLOAD ----------------

st.markdown("### 📸 Upload Your Image")

st.caption("Supported formats: PNG, JPG and JPEG")

uploaded_file = st.file_uploader(
    "Choose a fashion image",
    type=["png", "jpg", "jpeg"]
)


# ---------------- IMAGE PREVIEW ----------------

if uploaded_file is not None:

    original_image = Image.open(uploaded_file)

    # Convert to grayscale
    processed_image = original_image.convert("L")

    # Resize to 28x28
    processed_image = processed_image.resize((28, 28))

    # Convert to NumPy array
    image_array = np.array(processed_image).astype("float32")

    # Normalize
    image_array = image_array / 255.0

    # Reshape for CNN
    image_array = image_array.reshape(1, 28, 28, 1)

    st.markdown("### 🖼️ Image Preview")

    st.image(
        processed_image,
        width=220
    )

    st.caption("Image converted to grayscale and resized to 28 × 28 pixels.")

    # ---------------- PREDICTION BUTTON ----------------

    if st.button("🔮 Predict Fashion Item"):

        with st.spinner("Analyzing your image..."):

            prediction = model.predict(
                image_array,
                verbose=0
            )[0]

        predicted_class = int(np.argmax(prediction))

        confidence = float(
            np.max(prediction) * 100
        )

        # ---------------- PREDICTION RESULT ----------------

        st.markdown("---")
        st.markdown("### 🎯 Prediction Result")

        if confidence < 70:

            st.warning(
                "Low confidence! The model is not sure about this image. "
                "Please upload a clear Fashion-MNIST-style clothing image."
            )

        else:

            st.markdown(f"""
            <div class="result-card">
                <div class="result-label">PREDICTED CATEGORY</div>
                <div class="result-name">
                    {class_names[predicted_class]}
                </div>
                <div class="result-score">
                    {confidence:.2f}%
                </div>
                <div class="result-caption">
                    Model Confidence
                </div>
            </div>
            """, unsafe_allow_html=True)
     
        # ---------------- TOP 3 PREDICTIONS ----------------

        st.markdown("### 🏆 Top 3 Predictions")

        top_indices = np.argsort(prediction)[-3:][::-1]

        for index in top_indices:
            score = float(prediction[index])

            st.markdown(
                f"**{class_names[index]} — {score * 100:.2f}%**"
            )

            st.progress(score)

        st.success("Prediction completed successfully!")


else:

    st.info("Please upload a fashion image to start prediction.")


# ---------------- FOOTER ----------------

st.divider()

st.markdown("""
<div class="footer">
    <strong>Fabriq</strong><br>
    (A fashion item classifier)<br>
    Powered by TensorFlow, CNN and Streamlit<br>
    Deep Learning Project | Fashion-MNIST Dataset
</div>
""", unsafe_allow_html=True)
