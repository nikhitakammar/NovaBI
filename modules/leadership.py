import streamlit as st
from datetime import datetime

from services.ai_agent import ask_gemini
from services.monday_api import (
    load_live_deals,
    load_live_work_orders
)


def show_leadership():

    st.header("📈 Executive Leadership Report")

    st.write(
        "Generate an AI-powered leadership report using live Monday.com data."
    )

    if st.button("📄 Generate Leadership Report"):

        deals = load_live_deals()
        work_orders = load_live_work_orders()

        if deals.empty:
            st.error("Unable to retrieve live Monday.com data.")
            return

        # Current System Date
        today = datetime.now().strftime("%B %d, %Y")

        with st.spinner("Generating Executive Report..."):

            prompt = f"""
You are NovaBI, an Executive Business Intelligence Assistant.

Today's date is {today}.

Generate ONLY the body of the report.

Do NOT generate:
- Report title
- Prepared By
- Date

Analyze the following live business data.

Deals:

{deals.to_string(index=False)}

Work Orders:

{work_orders.to_string(index=False)}

Include these sections:

1. Executive Summary

2. Sales Pipeline Overview

3. Work Order Overview

4. Key Business Risks

5. Growth Opportunities

6. Recommendations

Use professional business language.
"""

            report = ask_gemini(
                prompt,
                deals,
                work_orders
            )

        st.success("Leadership Report Generated")

        st.markdown(f"""
# 📈 Executive Leadership Report

**Prepared by:** NovaBI AI Business Intelligence Assistant

**Date:** {today}

---
""")

        st.markdown(report)