import ssl
import socket

from urllib.parse import urlparse


def check_ssl(url):

    try:

        hostname = urlparse(url).hostname

        context = ssl.create_default_context()

        with socket.create_connection(
            (hostname, 443)
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=hostname
            ) as ssock:

                cert = ssock.getpeercert()

                return {
                    "ssl_valid": True,
                    "issuer": dict(
                        x[0] for x in cert["issuer"]
                    ).get("organizationName", "Unknown")
                }

    except Exception:

        return {
            "ssl_valid": False,
            "issuer": "Unknown"
        }
