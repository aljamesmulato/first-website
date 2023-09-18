import streamlit as st
from PIL import Image
st.set_page_config(page_title="Coffee Shop",layout="wide")
#asset
img_menu_f = Image.open("images/drinos.jpg")

st.title("Drino's Coffee & Cakes")
st.subheader("This Shop has unique Coffee")
st.write("[if your interested Contact me here](https://www.facebook.com/profile.php?id=61550798840094)")

with st.container():
    st.write("---")
    left_c, image_c = st.columns((4,4))
    with left_c:
        st.header("Menu")
        st.write("##")
        st.write(
            """
            Matcha 90.00 PHP

            Regular Coffee 50.00 PHP

            Java Chip 90.00 PHP

            Dalgona Coffee 100.00 PHP

            Spanish Latte 90.00 PHP


            """
        )
    with image_c:
        st.image(img_menu_f)

#asset
img_Chocolate_f = Image.open("images/cookies.jpg")

with st.container():
     st.write("---")
     image_c, left_c = st.columns((20,16))
with left_c:
     st.subheader("Chocolate")
     st.write("##")
     st.write(
        """
        This is Chocolate Cookie
        """
     )
with image_c:
        st.image(img_Chocolate_f)

#asset
img_Kape_f = Image.open("images/kape.jpg")

with st.container():
     st.write("---")
     left_c, image_c = st.columns((1,1))
with left_c:
     st.subheader("This is the Coffee for everyone")
     st.write("##")
     st.write(
        """
        This Coffee is very Taste Full
        """
     )
with image_c:
     st.image(img_Kape_f)

#asset
img_matcha_f = Image.open("images/cat.jpg")

with st.container():
     st.write("---")
     image_f, left_f = st.columns((1,1))
with left_f:
     st.subheader("This Matcha is the most favourite coffee here in drinos")
     st.write("##")
     st.write(
          """
          A very tasteful coffee
          """
     )
with image_f:
     st.image(img_matcha_f)