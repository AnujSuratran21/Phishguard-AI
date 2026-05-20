import whois

from datetime import datetime


def get_domain_info(url):

    try:

        domain_info = whois.whois(url)

        creation_date = domain_info.creation_date

        registrar = domain_info.registrar

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date:
            age_days = (
                datetime.now() - creation_date
            ).days
        else:
            age_days = -1

        return {
            "registrar": registrar,
            "domain_age_days": age_days
        }

    except Exception:

        return {
            "registrar": "Unknown",
            "domain_age_days": -1
        }
