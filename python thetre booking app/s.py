import streamlit as st

st.set_page_config(page_title="Bus Seat Booking", layout="centered")

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"
if 'seats' not in st.session_state:
    st.session_state.seats = [[0 for _ in range(4)] for _ in range(10)]  # 10 rows, 4 seats per row

# Navigation Function
def navigate(page):
    st.session_state.current_page = page

# Sidebar Navigation Menu
with st.sidebar:
    st.title("Navigation")
    if st.button("Home"):
        navigate("Home")
    if st.button("Book Seat"):
        navigate("Book Seat")
    if st.button("Booking Summary"):
        navigate("Booking Summary")
    if st.button("complaint"):
        navigate("complaint ")

# Home Page
if st.session_state.current_page == "Home":
    st.title("Welcome to  Theatre Seat Booking app")
    st.write("Choose an option from the sidebar to get started.")
     # Placeholder image
    if st.button("show movies") :
        st.write(" you have wide range movies here")
        ticket= st.radio('Choose your favorite snack:', ['leo', 'mankatha', 'bigil', 'thalapathy 67','varisu'])
        price=st.number_input("enter the number of tickets")

    price=st.number_input("enter the number of tickets")
    st.write(f"you are seletion is very best choice and the rate for the show here {price*100}")
 
elif st.session_state.current_page == "Book Seat":
    st.title("Book Your Seat")
    st.subheader("Select Your Seat")

    for row in range(10):
        cols = st.columns(4)
        for col in range(4):
            if st.session_state.seats[row][col] == 0:
                if cols[col].button(f"Row {row+1} Seat {col+1}"):
                    st.session_state.seats[row][col] = 1
                    st.success(f"Booked Row {row+1} Seat {col+1}")
            else:
                cols[col].button("X", disabled=True)


elif st.session_state.current_page == "Booking Summary":
    st.title("Booking Summary")
    booked_seats = [
        f"Row {i+1} Seat {j+1}"
        for i in range(10) for j in range(4) if st.session_state.seats[i][j] == 1
    ]
    if booked_seats:
        st.write("You have booked the following seats:")
        for seat in booked_seats:
            st.write(seat)
            
    else:
        st.write("No seats booked yet.")
        
else :

    st.subheader("here you can mention your complaint and feedback ,sugestion here")



    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("complaint")
    complaint=st.text_input("number")
    

    
    # Display the submitted data
    if st.button("submitt"):
        st.success("Form submitted successfully!")
        st.write("**Name:**", name)
        st.write("**Email:**", email)
        st.write("**Message:**", message)
