$(call inherit-product, device/samsung/jfltecdma/full_jfltecdma.mk)

# Enhanced NFC
$(call inherit-product, vendor/cm/config/nfc_enhanced.mk)

# Inherit some common CM stuff.
$(call inherit-product, vendor/cm/config/common_full_phone.mk)

PRODUCT_NAME := cm_jfltecdma
PRODUCT_DEVICE := jfltecdma

