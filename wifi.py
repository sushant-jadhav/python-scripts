import objc
import os
# sudo gem install terminal-notifier
# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

name_wifi = 'sushant';

objc.loadBundle('CoreWLAN',
                bundle_path = '/System/Library/Frameworks/CoreWLAN.framework',
                module_globals = globals())

iface = CWInterface.interface()

networks, error = iface.scanForNetworksWithName_error_(name_wifi, None)

network = networks.anyObject()

success, error = iface.associateToNetwork_password_error_(network, '31-12-1993', None);

if(success):
	# Calling the function
	notify(title    = 'Wifi Connected',
	       subtitle = 'with %s'%name_wifi,
	       message  = 'Connected!!!, This is WIFI Check')
if(error):
	# Calling the function
	notify(title    = 'Wifi Not Connected',
	       subtitle = 'with %s '%name_wifi,
	       message  = 'Not Connected!!!,Please check WIFI with %s' %error)