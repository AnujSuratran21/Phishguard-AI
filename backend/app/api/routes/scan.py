from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from urllib.parse import urlparse

from app.ml.predictor import predict_url

from app.services.virustotal_service import (
    check_virustotal
)

from app.services.whois_service import (
    get_domain_info
)

from app.services.ssl_service import (
    check_ssl
)

from app.core.database import get_db
from app.models.scan import Scan


router = APIRouter(
    prefix="/scan",
    tags=["URL Scanner"]
)


class URLRequest(BaseModel):
    url: str


# =====================================
# TRUSTED DOMAINS
# =====================================

TRUSTED_DOMAINS = [

    "google.com",
    "youtube.com",
    "github.com",
    "microsoft.com",
    "apple.com",
    "amazon.com",
    "linkedin.com",
    "infosys.com",
    "openai.com",
    "gov.in",
    "mhcyber.gov.in",
    "sbi.co.in",
    "onlinesbi.sbi",
    "bank.co.in",
    "bank.in"

]


# =====================================
# EXTRACT DOMAIN
# =====================================

def extract_domain(url: str):

    parsed = urlparse(url)

    return parsed.netloc.lower().replace(
        "www.",
        ""
    )


@router.post("/")
def scan_url(
    data: URLRequest,
    db: Session = Depends(get_db)
):

    url = data.url.lower()

    domain = extract_domain(url)

    # =====================================
    # TRUSTED DOMAIN CHECK
    # =====================================

    is_trusted = any(
        trusted in domain
        for trusted in TRUSTED_DOMAINS
    )

    # =====================================
    # IF TRUSTED WEBSITE
    # =====================================

    if is_trusted:

        result = {
            "url": url,
            "prediction": "safe",
            "confidence": 99,
            "risk_score": "LOW",
            "risk_points": 0,
            "virustotal": {
                "malicious": 0,
                "suspicious": 0
            },
            "whois": {
                "domain_age_days": 3650
            },
            "ssl": {
                "ssl_valid": True
            }
        }

        new_scan = Scan(
            url=url,
            prediction="safe",
            confidence=99.0,
            risk_score="LOW"
        )

        db.add(new_scan)

        db.commit()

        db.refresh(new_scan)

        result["id"] = new_scan.id

        return result

    # =====================================
    # AI MODEL PREDICTION
    # =====================================

    ml_result = predict_url(url)

    vt_result = check_virustotal(url)

    whois_result = get_domain_info(url)

    ssl_result = check_ssl(url)

    confidence = float(
        ml_result["confidence"]
    )

    risk_points = 0

    # =====================================
    # ML ANALYSIS
    # =====================================

    if ml_result["prediction"] == "phishing":

        risk_points += 30

    else:

        risk_points -= 20

    # =====================================
    # CONFIDENCE ANALYSIS
    # =====================================

    if confidence < 40:

        risk_points += 30

    elif confidence < 80:

        risk_points += 15

    else:

        risk_points -= 10

    # =====================================
    # VIRUSTOTAL ANALYSIS
    # =====================================

    malicious = vt_result.get(
        "malicious",
        0
    )

    suspicious = vt_result.get(
        "suspicious",
        0
    )

    risk_points += malicious * 5

    risk_points += suspicious * 3

    # =====================================
    # SSL ANALYSIS
    # =====================================

    if not ssl_result.get(
        "ssl_valid",
        False
    ):

        risk_points += 15

    # =====================================
    # DOMAIN AGE ANALYSIS
    # =====================================

    domain_age = whois_result.get(
        "domain_age_days",
        -1
    )

    if domain_age == -1:

        risk_points += 10

    elif domain_age < 30:

        risk_points += 25

    elif domain_age < 180:

        risk_points += 10

    else:

        risk_points -= 10

    # =====================================
    # SUSPICIOUS KEYWORDS
    # =====================================

    suspicious_words = [

        "verify",
        "bonus",
        "crypto",
        "wallet",
        "free",
        "claim",
        "gift",
        "prize",
        "win",
        "login",
        "signin",
        "secure"

    ]

    if any(
        word in url
        for word in suspicious_words
    ):

        risk_points += 35

    # =====================================
    # FINAL RISK LOGIC
    # =====================================

    if risk_points >= 50:

        risk = "HIGH"

        prediction = "phishing"

        confidence = 25

    elif risk_points >= 25:

        risk = "MEDIUM"

        prediction = "suspicious"

        confidence = 60

    else:

        risk = "LOW"

        prediction = "safe"

        confidence = 95

    # =====================================
    # SAVE TO DATABASE
    # =====================================

    new_scan = Scan(
        url=url,
        prediction=prediction,
        confidence=float(confidence),
        risk_score=risk
    )

    db.add(new_scan)

    db.commit()

    db.refresh(new_scan)

    # =====================================
    # FINAL RESPONSE
    # =====================================

    return {
        "id": new_scan.id,
        "url": url,
        "prediction": prediction,
        "confidence": round(confidence, 2),
        "risk_score": risk,
        "risk_points": risk_points,
        "virustotal": vt_result,
        "whois": whois_result,
        "ssl": ssl_result
    }
