import streamlit as st


def Card(title: str = None, description: str = None, key: str = None):
    st.markdown(f"""
        <div style="
            background: var(--muted);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 1.25rem 1.5rem;
            font-family: var(--font-sans);
            margin-bottom: 1rem;
        ">
            {'<div style="font-size:1rem;font-weight:600;color:var(--foreground);margin-bottom:0.25rem;">' + title + '</div>' if title else ''}
            {'<div style="font-size:0.875rem;color:var(--muted-foreground);">' + description + '</div>' if description else ''}
        </div>
    """, unsafe_allow_html=True)