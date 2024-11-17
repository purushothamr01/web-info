import whois
import argparse
import socket
import dns.resolver
import requests
import shodan

# Set up argument parser
parser = argparse.ArgumentParser(description="This is the basic information tool.", usage="python3 pytest.py -d DOMAIN [-s IP] [-f OUTPUT]")
parser.add_argument("-d", "--domain", help="Enter the domain name for foot printing.", required=True)
parser.add_argument("-s", "--shodan", help="Enter the IP for Shodan search.")
parser.add_argument("-f", "--output", help="Enter the file to save or write output to.")

# Parse arguments
args = parser.parse_args()
domain = args.domain
ip = args.shodan
output = args.output

# WHOIS module
print("[+] Getting WHOIS Information For Domain:", domain)

whois_result = ''
try:
    py = whois.whois(domain)
    print("[+] WHOIS info found.")
    whois_result += "Name: {}\n".format(py.name if py.name else "N/A")
    whois_result += "Registrar: {}\n".format(py.registrar if py.registrar else "N/A")
    whois_result += "Creation Date: {}\n".format(py.creation_date if py.creation_date else "N/A")
    whois_result += "Expiration Date: {}\n".format(py.expiration_date if py.expiration_date else "N/A")
    whois_result += "Registrant: {}\n".format(py.registrant if py.registrant else "N/A")
    whois_result += "Registrant Country: {}\n".format(py.registrant_country if py.registrant_country else "N/A")

except Exception as e:
    print("Error fetching WHOIS information:", str(e))
print(whois_result)

# DNS module
print("[+] Getting DNS info...")
dns_result = ''
try:
    for a in dns.resolver.resolve(domain, 'A'):
        dns_result += "[+] A Record: {}\n".format(a.to_text())
    for ns in dns.resolver.resolve(domain, 'NS'):
        dns_result += "[+] NS Record: {}\n".format(ns.to_text())
    for mx in dns.resolver.resolve(domain, 'MX'):
        dns_result += "[+] MX Record: {}\n".format(mx.to_text())
    for txt in dns.resolver.resolve(domain, 'TXT'):
        dns_result += "[+] TXT Record: {}\n".format(txt.to_text())

except Exception as e:
    print("Error fetching DNS information:", str(e))
print(dns_result)

# Geolocation module
print("[+] Getting geolocation info...")
geo_result = ''
try:
    response = requests.get("https://geolocation-db.com/json/" + socket.gethostbyname(domain)).json()
    geo_result += "[+] Country: {}\n".format(response.get('country_name', 'N/A'))
    geo_result += "[+] City: {}\n".format(response.get('city', 'N/A'))
    geo_result += "[+] State: {}\n".format(response.get('state', 'N/A'))
    geo_result += "[+] Latitude: {}\n".format(response.get('latitude', 'N/A'))
    geo_result += "[+] Longitude: {}\n".format(response.get('longitude', 'N/A'))
except Exception as e:
    print("Error fetching geolocation information:", str(e))
print(geo_result)

# Shodan module
if ip:
    print("[+] Searching Shodan for IP:", ip)
    api_key = "aZ1z42mZ8xCCWlXkjEhTjxJoPbNxojIT"  # Using Shodan API key
    api = shodan.Shodan(api_key)

    try:
        results = api.host(ip)
        print("[+] Results found for IP: {}".format(ip))
        print("[+] IP: {}".format(results['ip_str']))
        print("[+] Organization: {}".format(results.get('org', 'N/A')))
        print("[+] Country: {}".format(results.get('country_name', 'N/A')))
        print("[+] Data: \n{}".format(results.get('data', 'N/A')))
    except Exception as e:
        print("[-] Error fetching Shodan information:", str(e))

# Output to file
#For getting Output file Use -f <file name u want to save>
#python3 webinfo.py -d DOMAIN [-s IP] [-f OUTPUT]


if output:
    with open(output, 'w') as file:
        file.write(whois_result + '\n\n')
        file.write(dns_result + '\n\n')
        file.write(geo_result + '\n\n')
