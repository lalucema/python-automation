import requests
from main.utility.logger import automation_logger as logger


class WookieService:
    """
    Unified service object for:
    - Reservation endpoints
    - Office endpoints

    This keeps API logic in ONE clean class.
    """

    def __init__(self, base_url, headers):
        self.base_url = base_url.rstrip("/")
        self.headers = headers

    # ---------------------------------------------------------
    # RESERVATION: GET by user_id
    # ---------------------------------------------------------
    def get_reservation_by_user_id(self, user_id: int):
        url = f"{self.base_url}/reservation?select=*&user_id=eq.{user_id}"

        logger.info("➡️ Sending GET request for reservation")
        logger.info(f"URL: {url}")

        response = requests.get(url=url, headers=self.headers)

        logger.info(f"⬅️ Response Status: {response.status_code}")

        try:
            json_data = response.json()
            logger.info(f"Returned Records: {len(json_data)}")
        except Exception:
            logger.error("❌ Response JSON is invalid")

        return response

    # ---------------------------------------------------------
    # OFFICE: GET offices by date + period + office_id
    # ---------------------------------------------------------
    def get_offices(self, date_input: str, period: str, office_id: int):
        url = (
            f"{self.base_url}/rpc/get_offices_by_date_period"
            f"?date_input={date_input}"
            f"&period={period}"
            f"&office_id=eq.{office_id}"
        )

        logger.info("➡️ Sending GET request for office data")
        logger.info(f"URL: {url}")

        response = requests.get(url=url, headers=self.headers)

        logger.info(f"⬅️ Response Status: {response.status_code}")

        try:
            json_data = response.json()
            logger.info(f"Returned: {json_data}")
        except Exception:
            logger.error("❌ Response JSON is invalid")

        return response
