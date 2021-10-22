# Week 1 (Project) - IPGeolocation

## Scenario: Congrats, your Penetration testing company Red Planet has landed an external assessment for Microsoft! Your point of contact has give you a few IP addresses for you to test. Like with any test you should always verify the scope given to you to make sure there wasn't a mistake.


---
**Beginner Task:** Write a script that will have the user input an IP address. The script should output the ownership and geolocation of the IP. The output should be presented in a way that is clean and organized in order to be added to your report.

Solved:
```
Usage: ./ipGeolocation.py <ip address> <api_key>
Example: ./ipGeolocation.py 131.253.12.5 f2fb2bd77bab4b27ac702b0e363277e2
```

Output:
```                                                        
./ipGeolocation.py 131.253.12.5 f2fb2bd77bab4b27ac702b0e363277e2


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
PROJECT NAME: ipGeolocation for IPs in a list
VERSION: 1.0.0
AUTHOR: Empress O. Obazee (7igr3ss)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 




###################################### IPGEOLOCATION SCRIPT ###################################### 
    

[✓] [22/10/2021 12:47:31] ~ Quering IP ~ 
        IP Address: 131.253.12.5
        Organization: Microsoft Corporation
        Country: China
        Country Code: CHN
                                                                                                                  
```

---
**Intermediate Task:**  Have the script read multiple IP addresses from a text file and process them all at once.

Solved:
```
Usage: ./ipGeolocation.py </path/file> <api_key>
Example: ./ipGeolocation.py /path/ipaddress_list.txt f2fb2bd77bab4b27ac702b0e363277e2
```

Output:
```
./ipGeolocation.py ipaddress_list.txt f2fb2bd77bab4b27ac702b0e363277e2


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
PROJECT NAME: ipGeolocation for IPs in a list
VERSION: 1.0.0
AUTHOR: Empress O. Obazee (7igr3ss)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 




###################################### IPGEOLOCATION SCRIPT ###################################### 
    


 [✓] [22/10/2021 12:49:29] ~ Quering IP in List ~ 
        IP Address: 131.253.12.5
        Organization: Microsoft Corporation
        Country: China
        Country Code: CHN

 [✓] [22/10/2021 12:49:29] ~ Quering IP in List ~ 
        IP Address: 131.91.4.55
        Organization: Florida Atlantic University
        Country: United States
        Country Code: USA

 [✓] [22/10/2021 12:49:29] ~ Quering IP in List ~ 
        IP Address: 192.224.113.15
        Organization: 
        Country: United States
        Country Code: USA

 [✓] [22/10/2021 12:49:29] ~ Quering IP in List ~ 
        IP Address: 199.60.28.111
        Organization: Microsoft Corporation
        Country: United States
        Country Code: USA

```

---
**Expert Task:** Have the script read from a file containing both single IP addresses and CIDR notation, having it process it both types.

Solved:
```
Usage: ./ipGeolocation.py </path/file> <api_key>
Example: ./ipGeolocation.py /path/ipaddress_list.txt f2fb2bd77bab4b27ac702b0e363277e2
```

Output:
```
./ipGeolocation.py ipaddress_list.txt f2fb2bd77bab4b27ac702b0e363277e2


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
PROJECT NAME: ipGeolocation for IPs in a list
VERSION: 1.0.0
AUTHOR: Empress O. Obazee (7igr3ss)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 




###################################### IPGEOLOCATION SCRIPT ###################################### 
    


 [✓] [22/10/2021 12:50:34] ~ Quering IP in List ~ 
        IP Address: 20.128.0.1
        Organization: 
        Country: United States
        Country Code: USA

 [✓] [22/10/2021 12:50:34] ~ Quering IP in List ~ 
        IP Address: 20.128.0.2
        Organization: 
        Country: United States
        Country Code: USA

 [✓] [22/10/2021 12:50:34] ~ Quering IP in List ~ 
        IP Address: 20.128.0.3
        Organization: 
        Country: United States
        Country Code: USA

 [✓] [22/10/2021 12:50:34] ~ Quering IP in List ~ 
        IP Address: 20.128.0.4
        Organization: 
        Country: United States
        Country Code: USA

 [✓] [22/10/2021 12:50:34] ~ Quering IP in List ~ 
        IP Address: 20.128.0.5
        Organization: 
        Country: United States
        Country Code: USA
[snip...]
```