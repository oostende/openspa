from sys import modules
import os
import time

def getVersionString():
	return getImageVersionString()

def getImageVersionString():
	try:
		if os.path.isfile('/var/lib/opkg/status'):
			st = os.stat('/var/lib/opkg/status')
		else:
			st = os.stat('/usr/lib/ipkg/status')
		tm = time.localtime(st.st_mtime)
		if tm.tm_year >= 2011:
			return time.strftime("%Y-%m-%d %H:%M:%S", tm)
	except:
		pass
	return _("unavailable")

def getEnigmaVersionString():
	import enigma
	enigma_version = enigma.getEnigmaVersionString()
	if '-(no branch)' in enigma_version:
		enigma_version = enigma_version [:-12]
	return enigma_version

def getGStreamerVersionString():
	import enigma
	return enigma.getGStreamerVersionString()

def getKernelVersionString():
	try:
		return open("/proc/version","r").read().split(' ', 4)[2].split('-',2)[0]
	except:
		return _("unknown")

def getChipSetString():
	try:
		f = open('/proc/stb/info/chipset', 'r')
		chipset = f.read()
		f.close()
		return str(chipset.lower().replace('\n','').replace('bcm','').replace('brcm','').replace('sti',''))
	except:
		return "unavailable"

def getModelString():
	try:
		file = open("/proc/stb/info/boxtype", "r")
		model = file.readline().strip()
		file.close()
		return model
	except IOError:
		return "unknown"

def getCPUString():
	try:
		file = open('/proc/cpuinfo', 'r')
		lines = file.readlines()
		for x in lines:
			splitted = x.split(': ')
			if len(splitted) > 1:
				splitted[1] = splitted[1].replace('\n','')
				if splitted[0].startswith("system type"):
					system = splitted[1].split(' ')[0]
				elif splitted[0].startswith("Processor"):
					system = splitted[1].split(' ')[0]
		file.close()
		return system 
	except IOError:
		return "unavailable"

def getCPUSpeedString():
	try:
		file = open('/proc/cpuinfo', 'r')
		lines = file.readlines()
		for x in lines:
			splitted = x.split(': ')
			if len(splitted) > 1:
				splitted[1] = splitted[1].replace('\n','')
				if splitted[0].startswith("cpu MHz"):
					speed = splitted[1].split('.')[0]
		file.close()
		return speed
	except IOError:
		return "unavailable"

def getCpuCoresString():
	try:
		file = open('/proc/cpuinfo', 'r')
		lines = file.readlines()
		for x in lines:
			splitted = x.split(': ')
			if len(splitted) > 1:
				splitted[1] = splitted[1].replace('\n','')
				if splitted[0].startswith("processor"):
					if int(splitted[1]) > 0:
						cores = 2
					else:
						cores = 1
		file.close()
		return cores
	except IOError:
		return "unavailable"

def getCPUTempString():
	try:
		if os.path.isfile('/proc/stb/fp/temp_sensor_avs'):
			temperature = open("/proc/stb/fp/temp_sensor_avs").readline().replace('\n','')
			return _("%s°C") % temperature
	except:
		pass
	return ""

def getHardwareTypeString():
	try:
		if os.path.isfile("/proc/stb/info/boxtype"):
			return open("/proc/stb/info/boxtype").read().strip().upper()
		if os.path.isfile("/proc/stb/info/azmodel"):
			return "AZBOX " + open("/proc/stb/info/azmodel").read().strip().upper() + "(" + open("/proc/stb/info/version").read().strip().upper() + ")" 
		if os.path.isfile("/proc/stb/info/vumodel"):
			return "VU+" + open("/proc/stb/info/vumodel").read().strip().upper() + "(" + open("/proc/stb/info/version").read().strip().upper() + ")" 
		if os.path.isfile("/proc/stb/info/model"):
			return open("/proc/stb/info/model").read().strip().upper()
	except:
		pass
	return _("unavailable")

def getImageTypeString():
	try:
		return open("/etc/issue").readlines()[-2].capitalize().strip()[:-6]
	except:
		pass
	return _("undefined")

# For modules that do "from About import about"
about = modules[__name__]
