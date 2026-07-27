import streamlit as st

from services.ai_agent import ask_gemini
from services.monday_api import (
    load_live_deals,
    load_live_work_orders
)

from services.analysis import (
    total_deals,
    open_deals,
    high_probability_deals,
    total_work_orders,
    top_clients,
    top_sectors
)


def show_chat():

    st.header("💬 NovaBI AI Assistant")

    st.success("🟢 Connected to Live Monday.com")

    # -----------------------------
    # Chat History
    # -----------------------------
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # -----------------------------
    # Chat Input
    # -----------------------------
    question = st.chat_input(
        "Ask anything about your Deals or Work Orders..."
    )

    if question:

        # Display user message
        with st.chat_message("user"):
            st.markdown(question)

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        # Load live Monday.com data
        deals = load_live_deals()
        work_orders = load_live_work_orders()

        if deals.empty:

            answer = "Unable to retrieve live data from Monday.com."

        else:

            q = question.lower()

            with st.spinner("NovaBI is analyzing your business..."):

                # -----------------------------
                # Smart Business Analytics
                # -----------------------------

                if (
                    "open deal" in q
                    or "how many open" in q
                    or "open opportunities" in q
                ):

                    answer = (
                        f"There are **{open_deals()} open deals** currently available."
                    )

                elif (
                    "total deal" in q
                    or "number of deals" in q
                    or "deal count" in q
                ):

                    answer = (
                        f"There are **{total_deals()} total deals** in Monday.com."
                    )

                elif (
                    "high probability" in q
                    or "high chance" in q
                ):

                    answer = (
                        f"There are **{high_probability_deals()} high-probability deals**."
                    )

                elif (
                    "work order" in q
                    or "work orders" in q
                ):

                    answer = (
                        f"There are **{total_work_orders()} work orders**."
                    )

                elif (
                    "top client" in q
                    or "best client" in q
                    or "top customer" in q
                ):

                    answer = "### Top Clients\n\n"
                    answer += top_clients().to_markdown()

                elif (
                    "top sector" in q
                    or "sector" in q
                ):

                    answer = "### Top Sectors\n\n"
                    answer += top_sectors().to_markdown()

                else:

                    # AI handles everything else
                    answer = ask_gemini(
                        question,
                        deals,
                        work_orders
                    )

        # Store assistant response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(answer)