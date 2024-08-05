import os
import pandas as pd
from datetime import datetime
import base64
import json
import requests
from fake_useragent import UserAgent
import pandas_gbq

from google.oauth2 import service_account

try:
    credentials_json = os.getenv("GCP_CREDENTIALS")
    credentials = service_account.Credentials.from_service_account_info(
        json.loads(credentials_json),
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
except TypeError:
    credentials = None

def generate_cookies():
    session = requests.Session()
    response = session.get('https://www.enterkomputer.com')
    cookies = session.cookies.get_dict()
    str_cookies = f'ess={cookies['ess']}; csrf_cookie_name={cookies['csrf_cookie_name']}'
    return str_cookies

def fetch_product_list(cat_id, cat):
    """
    Fetches the product list from Enterkomputer API for a given category.
    """
    product_list = []
    page_counter = 1
    status = True

    ua = UserAgent()

    while status:
        url = "https://www.enterkomputer.com/jeanne/v2/product-list"
        headers = {
            "User-Agent": ua.random,
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://www.enterkomputer.com",
            "Referer": f"https://www.enterkomputer.com/category/{cat_id}/{cat}",
            "Cookie": generate_cookies(),
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
        }

        data = {
            "KCODE": cat_id,
            "SCODE": "all",
            "BCODE": "all",
            "BNAME": "",
            "MORDR": "default",
            "MSTGE": "mapping",
            "MKYWD": "",
            "MTAGS": "",
            "MSGMN": "category",
            "MPAGE": page_counter,
            "token": "U2FsdGVkX1-E55sT1JEmUtTtgjHvzgK98PZU8pKsTjQf8t2cV6U0Rrrd5ijzmdtRiKOvKb944B267vLzsZdvag",
            "signature": "6f2f8494bc4194daf124fbd20862b729",
        }

        json_response = json.loads(requests.post(url, headers=headers, json=data).text)
        print(cat, page_counter, json_response["status"])

        page_counter += 1
        status = json_response["status"]

        if status:
            products = json_response["result"][0]["PPRNT"][0]["PCHLD"]
            for p1 in products:
                for p2 in p1["PLIST"]:
                    product_list.append(p2)

    return product_list


def main():
    categories = [
        ["17", "processor"],
        ["12", "motherboard"],
        ["3", "casing"],
        ["24", "vga"],
        ["9", "lcd"],
        ["11", "memory-ram"],
        ["4", "cooler"],
        ["8", "keyboard"],
        ["19", "psu"],
        ["101", "solid-state-drive"],
        ["6", "hard-disk"],
    ]

    all_product_list = []
    for cat_id, cat in categories:
        product_list = fetch_product_list(cat_id, cat)
        all_product_list.extend(product_list)

    df = pd.DataFrame(all_product_list)
    df["inserted_at"] = datetime.now().date()

    # df.to_csv("enterkomputer_raw.csv", index=False)

    for col in df.columns:
        df[col] = df[col].astype("str")

    table_id = "de_zoomcamp.enterkomputer_raw"
    pandas_gbq.to_gbq(
        dataframe=df,
        credentials=credentials,
        destination_table=table_id,
        if_exists="append",
    )

    print(df.shape, "Data exported to CSV successfully.")


if __name__ == "__main__":
    main()
