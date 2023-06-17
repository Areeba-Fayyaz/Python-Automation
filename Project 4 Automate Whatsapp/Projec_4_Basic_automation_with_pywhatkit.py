import pywhatkit

pn=input('enter phone number')
pywhatkit.sendwhatmsg(pn, "Test", 9, 5, 15, True, 2)

group_id=input('enter phone number')
pywhatkit.sendwhatmsg_to_group(group_id, "Test", 9, 5, 15, True, 2)
