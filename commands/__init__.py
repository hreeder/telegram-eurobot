from . import server_status, whois

commands = {
    "server": server_status.server_status,
    "whois": whois.whois
}
