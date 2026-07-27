import streamlit as st
import plotly.express as px

from services.monday_api import (
    load_live_deals,
    load_live_work_orders
)


def show_dashboard():

    st.header("📊 Business Dashboard")

    # -----------------------------------
    # Load Live Monday.com Data
    # -----------------------------------
    deals = load_live_deals()
    work_orders = load_live_work_orders()

    if deals.empty:
        st.error("Unable to load Deals from Monday.com.")
        return

    if work_orders.empty:
        st.warning("Work Orders board is empty or unavailable.")

    # -----------------------------------
    # KPI Cards
    # -----------------------------------

    total_deals = len(deals)

    total_work_orders = len(work_orders)

    open_deals = len(
        deals[
            deals["Deal Status"]
            .fillna("")
            .str.lower() == "open"
        ]
    )

    high_probability = len(
        deals[
            deals["Closure Probability"]
            .fillna("")
            .str.lower() == "high"
        ]
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📁 Total Deals",
        total_deals
    )

    col2.metric(
        "🛠 Work Orders",
        total_work_orders
    )

    col3.metric(
        "🟢 Open Deals",
        open_deals
    )

    col4.metric(
        "⭐ High Probability",
        high_probability
    )

    st.markdown("---")

    # -----------------------------------
    # Charts
    # -----------------------------------

    chart1, chart2 = st.columns(2)

    with chart1:

        st.subheader("📊 Deal Status Distribution")

        status_counts = (
            deals["Deal Status"]
            .fillna("Unknown")
            .value_counts()
        )

        fig = px.bar(
            x=status_counts.index,
            y=status_counts.values,
            labels={
                "x": "Deal Status",
                "y": "Number of Deals"
            },
            title="Deals by Status"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with chart2:

        st.subheader("🥧 Closure Probability")

        probability_counts = (
            deals["Closure Probability"]
            .fillna("Unknown")
            .value_counts()
        )

        fig2 = px.pie(
            values=probability_counts.values,
            names=probability_counts.index,
            title="Closure Probability"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.markdown("---")

    # -----------------------------------
    # Recent Deals
    # -----------------------------------

    st.subheader("📋 Live Deals (Monday.com)")

    st.dataframe(
        deals,
        hide_index=True,
        use_container_width=True
    )

    st.markdown("---")

    # -----------------------------------
    # Live Work Orders
    # -----------------------------------

    st.subheader("🛠 Live Work Orders (Monday.com)")

    st.dataframe(
        work_orders,
        hide_index=True,
        use_container_width=True
    )

    st.markdown("---")

    # -----------------------------------
    # Refresh Button
    # -----------------------------------

    if st.button("🔄 Refresh Monday Data"):
        st.rerun()