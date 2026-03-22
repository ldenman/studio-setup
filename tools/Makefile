WAPI_DIR = ../lib/wapi

wingctl: wingctl.c $(WAPI_DIR)/wext.h
	cc -O2 -o wingctl wingctl.c -I$(WAPI_DIR) -L$(WAPI_DIR) -lwapi

clean:
	rm -f wingctl

.PHONY: clean
