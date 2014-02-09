installdir = $(pkglibdir)/python/Plugins/SystemPlugins

SUBDIRS = SoftwareManager PositionerSetup Satfinder \
	SkinSelector SatelliteEquipmentControl VideoTune Hotplug \
	DefaultServicesScanner DiseqcTester CommonInterfaceAssignment \
	CableScan FastScan OSDPositionSetup OSD3DSetup HdmiCEC VideoClippingSetup \
	Videomode VideoEnhancement WirelessLan NetworkWizard 3GModemManager

if HAVE_TEMPFANCONTROL
SUBDIRS += TempFanControl
endif

if DREAMBOX
SUBDIRS += FrontprocessorUpgrade NFIFlash
endif

install_PYTHON =	\
	__init__.py
