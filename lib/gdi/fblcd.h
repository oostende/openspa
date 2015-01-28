#ifndef __LCDFB_H
#define __LCDFB_H

#include <lib/base/eerror.h>
#include <linux/fb.h>
#include <lib/gdi/lcd.h>
#include "gpixmap.h"

#if defined(__sh__)
#define VFDBRIGHTNESS         0xc0425a03
#define VFDPWRLED             0xc0425a04 /* added by zeroone, also used in fp_control/global.h ; set PowerLed Brightness on HDBOX*/
#define VFDDRIVERINIT         0xc0425a08
#define VFDICONDISPLAYONOFF   0xc0425a0a
#define VFDDISPLAYWRITEONOFF  0xc0425a05
#define VFDDISPLAYCHARS       0xc0425a00

#define VFDCLEARICONS         0xc0425af6
#define VFDSETRF              0xc0425af7
#define VFDSETFAN             0xc0425af8
#define VFDGETWAKEUPMODE      0xc0425af9
#define VFDGETTIME            0xc0425afa
#define VFDSETTIME            0xc0425afb
#define VFDSTANDBY            0xc0425afc
#define VFDREBOOT             0xc0425afd
#define VFDSETLED             0xc0425afe
#define VFDSETMODE            0xc0425aff

#define VFDGETWAKEUPTIME      0xc0425b00
#define VFDGETVERSION         0xc0425b01
#define VFDSETDISPLAYTIME     0xc0425b02
#define VFDSETTIMEMODE        0xc0425b03
#define VFDDISPLAYCLR         0xc0425b00

/* structs are needed for sending icons etc. to aotom                           */
struct set_mode_s {
        int compat; /* 0 = compatibility mode to vfd driver; 1 = nuvoton mode */
};

struct set_brightness_s {
        int level;
};

struct set_icon_s {
        int icon_nr;
        int on;
};

struct set_led_s {
        int led_nr;
        int on;
};

/* time must be given as follows:
 * time[0] & time[1] = mjd ???
 * time[2] = hour
 * time[3] = min
 * time[4] = sec
 */
struct set_standby_s {
        char time[5];
};

struct set_time_s {
        char time[5];
};

struct aotom_ioctl_data {
        union
        {
                struct set_icon_s icon;
                struct set_led_s led;
                struct set_brightness_s brightness;
                struct set_mode_s mode;
                struct set_standby_s standby;
                struct set_time_s time;
        } u;
};
#endif

class eFbLCD: public eLCD
{
	int m_xRes, m_yRes, m_bpp;
	int m_brightness, m_gamma, m_alpha;
	int m_available;
	struct fb_var_screeninfo m_screeninfo;
	fb_cmap m_cmap;
	unsigned char m_ramp[256], m_rampalpha[256]; // RGB ramp 0..255
	uint16_t m_red[256], m_green[256], m_blue[256], m_trans[256];
	int m_phys_mem;
	int m_manual_blit;

	void calcRamp();
	int setMode(int xRes, int yRes, int bpp);
	void getMode();
	void enableManualBlit();
	void disableManualBlit();
			// low level gfx stuff
	int putCMAP();
public:
	eFbLCD(const char *fb="/dev/fb1");
	~eFbLCD();
	bool detected() { return m_available; }
	eSize size() { return eSize(m_xRes, m_yRes); }
	void setPalette(gUnmanagedSurface);
	int waitVSync();
	int setLCDContrast(int contrast) { return 0; };
	int setLCDBrightness(int brightness);
	void setInverted( unsigned char ) {};
	void setFlipped(bool) {};
#if defined(__sh__)
        void ShowIcon(int icon, bool show);
#endif
	bool isOled() const { return 0; };
	void update();  // blit
	int lock();
	void unlock();
	int islocked() { return locked; }
};

#endif
