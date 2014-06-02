installdir = $(pkglibdir)/python/Plugins/SystemPlugins

SUBDIRS = SoftwareManager PositionerSetup Satfinder \
	SatelliteEquipmentControl VideoTune Hotplug \
	DefaultServicesScanner DiseqcTester CommonInterfaceAssignment \
	FastScan HdmiCEC VideoClippingSetup \
	VideoEnhancement WirelessLan NetworkWizard 3GModemManager

if HAVE_TEMPFANCONTROL
SUBDIRS += TempFanControl
endif

if VUSOLO2
SUBDIRS += CableScan
endif

if VUSOLOSE
SUBDIRS += CableScan
endif

if VUDUO2
SUBDIRS += CableScan
endif

if VUUNO
SUBDIRS += CableScan
endif

if VUULTIMO
SUBDIRS += CableScan
endif

if DREAMBOX
SUBDIRS += FrontprocessorUpgrade NFIFlash CableScan
endif

install_PYTHON = __init__.py
