import streamlit as st

st.title("Serial Number Stripper")

if "serial_input" not in st.session_state:
    st.session_state.serial_input = ""
if "result" not in st.session_state:
    st.session_state.result = ""

def clear_input():
    st.session_state.serial_input = ""
    st.session_state.result = ""

serial_input = st.text_input("Input Serial Number", key="serial_input")

def format_serial(text):
    prefixes = ["0100796", "0100787", "0100786", "32104"]
    part_a = ""
    for prefix in prefixes:
        idx = text.find(prefix)
        if idx != -1:
            raw = prefix + text[idx + len(prefix):idx + len(prefix) + 4]
            part_a = raw[:-4] + raw[-3:]
            break

    paren_idx = text.find("(")
    part_b = ""
    if idx != -1 and paren_idx > 0:
        segment = text[idx + len(prefix) + 4:paren_idx]
        for ch in segment:
            if ch.isupper():
                part_b = ch
                break

    close_paren_idx = text.find(")")
    part_c = ""
    part_d = ""
    if close_paren_idx != -1:
        part_c = text[close_paren_idx + 1:close_paren_idx + 4]
        part_d = text[close_paren_idx + 5:close_paren_idx + 14]

    return f"{part_a}{part_b}:{part_c}-{part_d}"

col1, col2 = st.columns(2)
with col1:
    if st.button("Format"):
        if serial_input:
            st.session_state.result = format_serial(serial_input)
        else:
            st.warning("Please enter a serial number.")
with col2:
    st.button("Clear", on_click=clear_input)

if st.session_state.result:
    st.code(st.session_state.result, language=None)
