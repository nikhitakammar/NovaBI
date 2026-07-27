import os
import requests
import pandas as pd
from dotenv import load_dotenv

# ----------------------------------------
# Load Environment Variables
# ----------------------------------------
load_dotenv()

# ----------------------------------------
# Monday API Configuration
# ----------------------------------------
MONDAY_API_TOKEN = os.getenv("MONDAY_API_TOKEN")

URL = "https://api.monday.com/v2"

HEADERS = {
    "Authorization": MONDAY_API_TOKEN,
    "Content-Type": "application/json"
}

# ----------------------------------------
# Board IDs
# ----------------------------------------
DEALS_BOARD_ID = 5030218690
WORK_ORDERS_BOARD_ID = 5030218940


# ----------------------------------------
# Get All Boards
# ----------------------------------------
def get_boards():

    query = """
    {
        boards {
            id
            name
        }
    }
    """

    response = requests.post(
        URL,
        json={"query": query},
        headers=HEADERS
    )

    return response.json()


# ----------------------------------------
# Get Items from a Board
# ----------------------------------------
def get_board_items(board_id):

    query = f"""
    {{
        boards(ids: {board_id}) {{
            items_page {{
                items {{
                    id
                    name

                    column_values {{
                        text
                        column {{
                            title
                        }}
                    }}
                }}
            }}
        }}
    }}
    """

    response = requests.post(
        URL,
        json={"query": query},
        headers=HEADERS
    )

    return response.json()


# ----------------------------------------
# Convert Board to DataFrame
# ----------------------------------------
def board_to_dataframe(board_id):

    data = get_board_items(board_id)

    try:
        items = data["data"]["boards"][0]["items_page"]["items"]
    except (KeyError, IndexError):
        print("Unable to fetch board data from Monday.com")
        return pd.DataFrame()

    rows = []

    for item in items:

        row = {
            "Name": item["name"]
        }

        for column in item["column_values"]:

            title = column["column"]["title"]
            value = column["text"]

            row[title] = value

        rows.append(row)

    return pd.DataFrame(rows)


# ----------------------------------------
# Load Deals Board
# ----------------------------------------
def load_live_deals():

    return board_to_dataframe(DEALS_BOARD_ID)


# ----------------------------------------
# Load Work Orders Board
# ----------------------------------------
def load_live_work_orders():

    return board_to_dataframe(WORK_ORDERS_BOARD_ID)