import pandas as pd
from datetime import datetime
import json
import requests
from fake_useragent import UserAgent

import pandas_gbq
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    "/home/al/projects/creds/ichsanul-dev-cc6f799c9121.json",
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)


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
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://www.enterkomputer.com",
            "DNT": "1",
            "Sec-GPC": "1",
            "Connection": "keep-alive",
            "Referer": f"https://www.enterkomputer.com/category/{cat_id}/{cat}",
            "Cookie": "ess=a63e8c792788789ed3ca4488338282c2666be8f4; csrf_cookie_name=2221d451c939048e8e79b219af64d8ea",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers",
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
            "signature": "54f641b51cc26b51894b06dbdb55b4b3",
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

    df.to_csv("enterkomputer_raw.csv", index=False)

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
