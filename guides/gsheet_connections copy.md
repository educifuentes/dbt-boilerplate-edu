# Connecting a Private Google Sheet to Streamlit

also see
[Analyzing the Impact of Coronavirus on the Stock Market using Python, Google Sheets and Google Finance // Adil Moujahid // Bridging Tech and Art](https://adilmoujahid.com/posts/2020/04/stocks-analysis-covid19-coronavirus-python/)

Here is a step-by-step summary based on the [official Streamlit documentation](https://docs.streamlit.io/develop/tutorials/databases/private-gsheet).

## 1. Enable the Sheets API

1. Go to the [Google Cloud Console](https://console.cloud.google.com/apis/dashboard).
2. Select or create a project.
3. Search for **"Google Sheets API"** and enable it.

## 2. Create a Service Account & Key

1. Go to the [Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts) in Google Cloud Console.
2. Click **Create Service Account**.
3. Grant the account **Viewer** permissions (or Editor if you need to write).
4. Click **Done**.
5. Click on the newly created service account, go to the **Keys** tab.
6. Click **Add Key > Create new key**, select **JSON**, and download the file.

## 3. Share the Google Sheet

1. Open your private Google Sheet.
2. Click **Share**.
3. Paste the `client_email` found in your downloaded JSON key file.
4. Grant **Viewer** (or Editor) access.

## 4. Configure Local Secrets

Add the credentials to your `.streamlit/secrets.toml` file. **Do not commit this file to Git.**

```toml
[connections.gsheets]
spreadsheet = "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit"
type = "service_account"
project_id = "xxx"
private_key_id = "xxx"
private_key = "xxx"
client_email = "xxx"
client_id = "xxx"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "xxx"
```

_Note: You can copy the values directly from your downloaded JSON key file._

## 5. Install Dependencies

Install the connection library:

```bash
pip install st-gsheets-connection
```

## 6. Connect in Your App

Use `st.connection` to access the sheet.

```python
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object
conn = st.connection("gsheets", type=GSheetsConnection)

# Read the data
df = conn.read()

# Print results
st.dataframe(df)
```
