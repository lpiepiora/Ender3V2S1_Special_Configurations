#!/usr/bin/python

# ------------------------------------------------------------------------------
# Ender3S1 Configurations generator script for the Professional Firmware
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('Ender3S1', ['S1'])
CreateConfigs.Generate('Ender3S1-ManualMesh', ['S1-ManualMesh'])
