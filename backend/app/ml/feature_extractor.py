import re
from urllib.parse import urlparse


def extract_features(url):

    parsed = urlparse(url)

    domain = parsed.netloc

    features = {

        "url_length": len(url),

        "domain_length": len(domain),

        "has_https": 1 if parsed.scheme == "https" else 0,

        "count_dots": url.count("."),

        "count_hyphen": url.count("-"),

        "count_at": url.count("@"),

        "count_question": url.count("?"),

        "count_equal": url.count("="),

        "count_digits": sum(c.isdigit() for c in url),

        "count_slash": url.count("/"),

        "has_ip": 1 if re.match(
            r"^\d+\.\d+\.\d+\.\d+$",
            domain
        ) else 0,

        "has_suspicious_words": 1 if any(
            word in url.lower()
            for word in [
                "login",
                "verify",
                "secure",
                "account",
                "update",
                "bank",
                "paypal",
                "free",
                "bonus"
            ]
        ) else 0,

        "subdomain_count": domain.count("."),

        "is_shortened": 1 if any(
            short in domain
            for short in [
                "bit.ly",
                "tinyurl",
                "goo.gl",
                "t.co"
            ]
        ) else 0
    }

    return list(features.values())
