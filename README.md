Domain Information Gathering Tool

This Python script is a simple tool designed for gathering basic information about a domain and its associated IP address.
It provides WHOIS data, DNS records, geolocation information, and Shodan data for any given IP address. 
This tool is useful for security professionals, researchers, or anyone interested in domain footprinting.

Features

WHOIS Lookup: Fetches information about the domain's registration.
DNS Records: Retrieves various DNS records, including A, NS, MX, and TXT records.
Geolocation: Provides geolocation data based on the domain's resolved IP address.
Shodan Integration: Searches for additional information using the Shodan API if an IP address is provided.
Output to File: Saves the gathered information to a specified output file.

Requirements

Python 3.x
Required libraries:
whois
argparse
socket
dns.resolver
requests
shodan
