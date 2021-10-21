# Week 1 (Project) - IPGeolocation

## Scenario: Congrats, your Penetration testing company Red Planet has landed an external assessment for Microsoft! Your point of contact has give you a few IP addresses for you to test. Like with any test you should always verify the scope given to you to make sure there wasn't a mistake.


---
**Beginner Task:** Write a script that will have the user input an IP address. The script should output the ownership and geolocation of the IP. The output should be presented in a way that is clean and organized in order to be added to your report.

```
Usage: ./ipGeolocation.py <ip address> <api_key>
Example: ./ipGeolocation.py 192.253.12.5 f2fb2bd77bab4b27ac702b0e363277e2
```

---
**Intermediate Task:**  Have the script read multiple IP addresses from a text file and process them all at once.

```
Usage: ./ipGeolocation.py </path/file> <api_key>
Example: ./ipGeolocation.py /path/ipaddress_list.txt f2fb2bd77bab4b27ac702b0e363277e2
```

---
**Expert Task:** Have the script read from a file containing both single IP addresses and CIDR notation, having it process it both types.
```
Usage: ./ipGeolocation.py </path/file> <api_key>
Example: ./ipGeolocation.py /path/ipaddress_list.txt f2fb2bd77bab4b27ac702b0e363277e2
```