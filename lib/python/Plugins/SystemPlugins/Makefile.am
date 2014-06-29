installdir = $(pkglibdir)/python/Plugins/SystemPlugins

SUBDIRS = SoftwareManager PositionerSetup Satfinder \
	SatelliteEquipmentControl VideoTune Hotplug CableScan \
	DefaultServicesScanner DiseqcTester CommonInterfaceAssignment \
	FastScan HdmiCEC VideoClippingSetup \
	VideoEnhancement WirelessLan NetworkWizard 3GModemManager

if HAVE_TEMPFANCONTROL
SUBDIRS += TempFanControl
endif

if DREAMBOX
SUBDIRS += FrontprocessorUpgrade NFIFlash CableScan
endif

install_PYTHON = __init__.py
