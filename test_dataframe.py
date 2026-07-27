from services.monday_api import board_to_dataframe

DEALS_BOARD_ID = 5030218690

df = board_to_dataframe(DEALS_BOARD_ID)

print(df.head())

print(df.columns)
