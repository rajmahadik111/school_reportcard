import hashlib
from datetime import datetime
import streamlit as st

# Initialize the blockchain as an empty list
blockchain = []

# Function to generate a unique hash for each block
def generate_hash(block):
    block_string = f"{block['index']}{block['data']}{block['timestamp']}{block['previous_hash']}"
    return hashlib.sha256(block_string.encode()).hexdigest()

# Function to create a new block
def create_block(index, data, previous_hash):
    return {
        "index": index,
        "data": data,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "previous_hash": previous_hash
    }

# Function to add a new block to the blockchain
def add_block(data):
    previous_block = blockchain[-1]  # Get the last block in the chain
    new_index = previous_block["index"] + 1  # New block index
    new_hash = generate_hash(previous_block)  # Hash of the last block

    # Create a new block
    new_block = create_block(new_index, data, new_hash)
    blockchain.append(new_block)  # Add to the blockchain

# Initialize the blockchain with the first block (genesis block)
genesis_block = create_block(0, "Genesis Block", "0")
blockchain.append(genesis_block)

# Streamlit app layout
st.title("Blockchain Report Card App")

# Input form to add new report card
with st.form(key="report_form"):
    student_name = st.text_input("Student Name")
    math_grade = st.selectbox("Math Grade", ["A", "B", "C", "D", "F"])
    science_grade = st.selectbox("Science Grade", ["A", "B", "C", "D", "F"])
    submit_button = st.form_submit_button(label="Add Report Card")

    if submit_button:
        if student_name and math_grade and science_grade:
            data = f"{student_name} - Math: {math_grade}, Science: {science_grade}"
            add_block(data)
            st.success(f"Report card for {student_name} added successfully!")

# Display the blockchain
st.subheader("Blockchain Overview")

for block in blockchain:
    st.write(f"**Block Index:** {block['index']}")
    st.write(f"**Data:** {block['data']}")
    st.write(f"**Timestamp:** {block['timestamp']}")
    st.write(f"**Previous Hash:** {block['previous_hash']}")
    st.write("---")
