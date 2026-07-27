from services.monday_api import (
    load_live_deals,
    load_live_work_orders
)


def total_deals():
    return len(load_live_deals())


def open_deals():
    deals = load_live_deals()

    return len(
        deals[
            deals["Deal Status"]
            .fillna("")
            .str.lower() == "open"
        ]
    )


def high_probability_deals():
    deals = load_live_deals()

    return len(
        deals[
            deals["Closure Probability"]
            .fillna("")
            .str.lower() == "high"
        ]
    )


def total_work_orders():
    return len(load_live_work_orders())


def top_sectors():

    deals = load_live_deals()

    return (
        deals["Sector/service"]
        .value_counts()
        .head(5)
    )


def top_clients():

    deals = load_live_deals()

    return (
        deals["Client Code"]
        .value_counts()
        .head(5)
    )