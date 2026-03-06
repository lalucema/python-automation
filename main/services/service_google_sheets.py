# main/services/service_google_sheets.py

import requests
from main.utility.logger import automation_logger

class GoogleSheetsService:

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        automation_logger.info(f"[GoogleSheetsService] Initialized with base_url={base_url}")

    # -----------------------------
    # GET
    # -----------------------------
    def get_records(self):
        url = self.base_url
        automation_logger.info(f"[GET] Fetching Google Sheets records → {url}")

        response = requests.get(url, headers=self.headers)

        automation_logger.info(f"[GET] Status: {response.status_code}")
        automation_logger.info(f"[GET] Response: {response.text}")

        return response

    # -----------------------------
    # POST
    # -----------------------------
    def create_record(self, body: dict):
        url = self.base_url
        automation_logger.info(f"[POST] Creating Google Sheets record → {url}")
        automation_logger.info(f"[POST] Body: {body}")

        response = requests.post(url, headers=self.headers, json=body)

        automation_logger.info(f"[POST] Status: {response.status_code}")
        automation_logger.info(f"[POST] Response: {response.text}")

        return response

    # -----------------------------
    # PATCH
    # -----------------------------
    def update_record(self, row_id: str, body: dict):
        url = f"{self.base_url}/id/{row_id}"
        automation_logger.info(f"[PATCH] Updating Google Sheets row ID {row_id} → {url}")
        automation_logger.info(f"[PATCH] Body: {body}")

        response = requests.patch(url, headers=self.headers, json=body)

        automation_logger.info(f"[PATCH] Status: {response.status_code}")
        automation_logger.info(f"[PATCH] Response: {response.text}")

        return response

    # -----------------------------
    # DELETE
    # -----------------------------
    def delete_record(self, row_id: str):
        url = f"{self.base_url}/id/{row_id}"
        automation_logger.info(f"[DELETE] Deleting Google Sheets row ID {row_id} → {url}")

        response = requests.delete(url, headers=self.headers)

        automation_logger.info(f"[DELETE] Status: {response.status_code}")
        automation_logger.info(f"[DELETE] Response: {response.text}")

        return response
