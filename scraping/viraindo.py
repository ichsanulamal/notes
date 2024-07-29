import requests
import os
import base64
import json
import pandas as pd
from io import StringIO
from datetime import datetime
import pandas_gbq
from google.oauth2.service_account import Credentials

def read_gcp_sa_key_from_secret(secret_name):
  """Reads a GCP Service Account key JSON from a GitHub Actions secret.

  Args:
    secret_name: The name of the GitHub Actions secret.

  Returns:
    A Google Credentials object.
  """

  # Get the base64 encoded secret from the environment
  base64_encoded_key = os.environ.get(secret_name)

  # Decode the base64 string
  decoded_key = base64.b64decode(base64_encoded_key).decode('utf-8')

  # Parse the JSON
  key_dict = json.loads(decoded_key)

  # Create Google Credentials object
  credentials = Credentials.from_service_account_info(key_dict)

  return credentials

secret_name = 'GCP_CREDENTIALS'  # Replace with your secret name
credentials = read_gcp_sa_key_from_secret(secret_name)

def fetch_data(url):
    """
    Fetches HTML data from a given URL and returns it as a DataFrame.
    """
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    response = requests.get(url, headers=header)
    response.raise_for_status()  # Raise an exception for HTTP errors
    df = pd.read_html(StringIO(response.text))[0]
    return df


def transform_columns(df):
    """
    Transforms DataFrame with pairs of columns into a DataFrame with two columns: 'name' and 'price'.
    """
    new_df = pd.DataFrame()
    for i in range(0, len(df.columns), 2):
        pair = df.iloc[:, i : i + 2]
        pair.columns = ["name", "price"]
        new_df = pd.concat([new_df, pair], axis=0, ignore_index=True)
    return new_df


def main():
    links = [
        "motherboard.html",
        "proc.html",
        "storage.html",
        "memory.html",
        "lcd.html",
        "casing.html",
        "psu.html",
        "vga.html",
        "mcardflashdisk.html",
        "keymouse.html",
        "audio.html",
        "cooler.html",
        "aksesoris.html",
        "networking.html",
        "printer.html",
        "office.html",
        "tinta.html",
        "software.html",
        "ups-stabilizer.html",
        "notebook.html",
        "partnotebook.html",
        "gadget.html",
        "pcbranded.html",
        "projector.html",
        "server.html",
        "rackserver.html",
    ]

    dataframes = {}
    for link in links:
        category = link.removesuffix(".html")
        url = f"https://viraindo.net/{link}"

        try:
            df = fetch_data(url)
            df = transform_columns(df)
            dataframes[category] = df
            print("Processed", category, df.shape)
        except Exception as e:
            print(f"Error fetching data for {category}: {e}")

    combined_df = pd.concat(
        [df.assign(category=cat) for cat, df in dataframes.items()], ignore_index=True
    )

    combined_df = combined_df[
        (combined_df["price"].notna()) & (combined_df["price"] != "Call")
    ]
    combined_df = combined_df.drop_duplicates(subset=["name"])

    combined_df["inserted_at"] = datetime.now().date()

    combined_df.to_csv("viraindo_raw.csv", index=False)

    table_id = "de_zoomcamp.viraindo_raw"
    pandas_gbq.to_gbq(
        dataframe=combined_df,
        credentials=credentials,
        destination_table=table_id,
        if_exists="append",
    )

    print("Success")


if __name__ == "__main__":
    main()
