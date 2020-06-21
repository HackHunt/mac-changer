# MAC Changer 

### Media Access Control Address (MAC Address):
 - Permanent
 - Physical
 - Unique
 - Assigned by manufacturer

### Why to change the MAC address?
- Increase anonymity
- Impersonate other devices
- Bypass filters

### Supports Platform: Linux, Debain

### How to use:
- Convert the setup.sh into executable
	> **chmod 755 setup.sh**
- Run setup.sh
	> **./setup.sh**

- Convert the mac_changer into executable.
    > **chmod u+x mac_changer**
- Run the Executable.
    > **./mac_changer** 

### Available Arguments:
- **-h or --help:** *Displays all the available options.*
- **-i or --interface**: *This option needs to be used as to 
define for which interface you want to change the MAC address.*
- **-m or --mac:** *Optional. Can be used to specify a MAC Address.*

- **Note:** 
    - If *-m* or *--mac* option is not defined, the program will use 
    *Random MAC Address Generation Algorithm*. 
    - **Random MAC Address Generation Algorithm** will always generate a unicast mac address.

### Color:
- **Green:** Successful.
- **Yellow:** In process.
- **White:** MAC Address.
- **Red:** Unsuccessful or Errors. 

### Licensed: GNU General Public License, version 3

### Developer Information:
- **Website:** [Hack Hunt](https://hack-hunt.blogspot.com/)
- **Contact:** hh.hackunt@gmail.com
- **Youtube:** [Hack Hunt](https://youtube.com/hackhunt) 
- **Instagram:** [hh.hackhunt](https://www.instagram.com/hh.hackhunt/)
- **Facebook:** [hh.hackhunt](https://www.facebook.com/hh.hackhunt/)
- **Twitter:** [hh_hackhunt](https://twitter.com/hh_hackhunt/)
