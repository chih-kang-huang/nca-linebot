import pandas as pd

sheet_id = "1OZaZYPPFPVo5EuThuyjS3STR8nMf7peSjK673_bPDHE"
sheet_name = "Admin"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

def get_admins():
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    return pd.read_csv(url)['idLINE'].tolist()

def get_menu(nameRestaurant):
    sheet_name = nameRestaurant
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    return pd.read_csv(url)#['idLINE'].tolist()
