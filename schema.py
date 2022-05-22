from pydantic import BaseModel


class AgentResult(BaseModel):
        computer_name: str
        system_version: str
        antivirus_installed: bool
        antivirus_enabled: bool
        antivirus_up_to_date: bool
        windows_firewall_is_active: bool
        max_pass_age: int
        min_pass_len: int
        number_of_connected_doks: int
        chrome_version: str
        failed_login_event: list