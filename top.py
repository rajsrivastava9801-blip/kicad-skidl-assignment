"""
SKiDL script generated from AxxSolder.kicad_sch
Total components : 146
Standard parts   : 114
Custom stub parts: 32
"""

from skidl import *


# ═══════════════════════════════════════════════════════════════
# CUSTOM PART STUBS
# Vendor/custom parts not in KiCad standard libraries.
# Defined here so the script runs without needing external libs.
# ═══════════════════════════════════════════════════════════════

Adafruit_240x320_TFT = SchLib(tool=SKIDL)
MAX16171ATA_VY_T = SchLib(tool=SKIDL)
PEC11J_9215F_S0015 = SchLib(tool=SKIDL)
TSW_108_07_T_S = SchLib(tool=SKIDL)
ADTSM644KVTR = SchLib(tool=SKIDL)
SMF4L24AT1G = SchLib(tool=SKIDL)
WSLP25125L000FEA = SchLib(tool=SKIDL)
OPA2387DSGT = SchLib(tool=SKIDL)
TLV76733DRVR = SchLib(tool=SKIDL)
EEV227M035A9MAA = SchLib(tool=SKIDL)
part_61300611821 = SchLib(tool=SKIDL)
PMEG6020ER_115 = SchLib(tool=SKIDL)
STL10N3LLH5 = SchLib(tool=SKIDL)
BAV199WQ_7 = SchLib(tool=SKIDL)
INA281A5QDBVRQ1 = SchLib(tool=SKIDL)
part_2N7002NXAKR = SchLib(tool=SKIDL)
LTC4440AHMS8E_5_PBF = SchLib(tool=SKIDL)
TPD4E1U06DBVR = SchLib(tool=SKIDL)
STM32G431CBT6 = SchLib(tool=SKIDL)
BSC014N04LS = SchLib(tool=SKIDL)
SF_2410FP100W_2 = SchLib(tool=SKIDL)
USB4110_GF_A = SchLib(tool=SKIDL)
STUSB4500QTR = SchLib(tool=SKIDL)
SRP7028CC_150M = SchLib(tool=SKIDL)
part_691243110009 = SchLib(tool=SKIDL)
BLM18HE601SN1D = SchLib(tool=SKIDL)
STL9P3LLH6 = SchLib(tool=SKIDL)

# TFT1 — Adafruit_240x320_TFT (~)
Adafruit_240x320_TFT += Part(tool=SKIDL, name="Adafruit_240x320_TFT",
    ref_prefix="TFT",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR), Pin(num=4, name="p4", func=Pin.types.BIDIR), Pin(num=5, name="p5", func=Pin.types.BIDIR), Pin(num=6, name="p6", func=Pin.types.BIDIR), Pin(num=7, name="p7", func=Pin.types.BIDIR), Pin(num=8, name="p8", func=Pin.types.BIDIR)])

# IC7 — MAX16171ATA_VY+T (MAX16171ATA_VY+T)
MAX16171ATA_VY_T += Part(tool=SKIDL, name="MAX16171ATA_VY+T",
    ref_prefix="IC",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR), Pin(num=4, name="p4", func=Pin.types.BIDIR), Pin(num=5, name="p5", func=Pin.types.BIDIR), Pin(num=6, name="p6", func=Pin.types.BIDIR), Pin(num=7, name="p7", func=Pin.types.BIDIR)])

# U2 — PEC11J-9220F-S0015 (PEC11J-9215F-S0015)
PEC11J_9215F_S0015 += Part(tool=SKIDL, name="PEC11J-9220F-S0015",
    ref_prefix="U",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR), Pin(num=4, name="p4", func=Pin.types.BIDIR), Pin(num=5, name="p5", func=Pin.types.BIDIR), Pin(num=6, name="p6", func=Pin.types.BIDIR)])

# J7 — TSW-108-07-T-S (TSW-108-07-T-S)
TSW_108_07_T_S += Part(tool=SKIDL, name="TSW-108-07-T-S",
    ref_prefix="J",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR), Pin(num=4, name="p4", func=Pin.types.BIDIR), Pin(num=5, name="p5", func=Pin.types.BIDIR), Pin(num=6, name="p6", func=Pin.types.BIDIR), Pin(num=7, name="p7", func=Pin.types.BIDIR), Pin(num=8, name="p8", func=Pin.types.BIDIR)])

# S3 — ADTSM644KVTR (ADTSM644RVTR)
ADTSM644KVTR += Part(tool=SKIDL, name="ADTSM644KVTR",
    ref_prefix="S",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR)])

# D3 — SMF4L24AT1G (SMF4L24AT1G)
SMF4L24AT1G += Part(tool=SKIDL, name="SMF4L24AT1G",
    ref_prefix="D",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR)])

# R42 — WSLP25125L000FEA (5m)
WSLP25125L000FEA += Part(tool=SKIDL, name="WSLP25125L000FEA",
    ref_prefix="R",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR)])

# IC2 — OPA2387DSGT (OPA2387DSGT)
OPA2387DSGT += Part(tool=SKIDL, name="OPA2387DSGT",
    ref_prefix="IC",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR), Pin(num=4, name="p4", func=Pin.types.BIDIR), Pin(num=5, name="p5", func=Pin.types.BIDIR), Pin(num=6, name="p6", func=Pin.types.BIDIR), Pin(num=7, name="p7", func=Pin.types.BIDIR), Pin(num=8, name="p8", func=Pin.types.BIDIR), Pin(num=9, name="p9", func=Pin.types.BIDIR)])

# IC1 — TLV76733DRVR (TLV76733DRVR)
TLV76733DRVR += Part(tool=SKIDL, name="TLV76733DRVR",
    ref_prefix="IC",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR), Pin(num=4, name="p4", func=Pin.types.BIDIR), Pin(num=5, name="p5", func=Pin.types.BIDIR), Pin(num=6, name="p6", func=Pin.types.BIDIR), Pin(num=7, name="p7", func=Pin.types.BIDIR)])

# C37 — EEV227M035A9MAA (220u)
EEV227M035A9MAA += Part(tool=SKIDL, name="EEV227M035A9MAA",
    ref_prefix="C",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR)])

# J4 — 61300611821 (61300611821)
part_61300611821 += Part(tool=SKIDL, name="61300611821",
    ref_prefix="J",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR), Pin(num=4, name="p4", func=Pin.types.BIDIR), Pin(num=5, name="p5", func=Pin.types.BIDIR), Pin(num=6, name="p6", func=Pin.types.BIDIR)])

# D10 — PMEG6020ER,115 (PMEG6020ER)
PMEG6020ER_115 += Part(tool=SKIDL, name="PMEG6020ER,115",
    ref_prefix="D",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR)])

# Q2 — STL10N3LLH5 (STL10N3LLH5)
STL10N3LLH5 += Part(tool=SKIDL, name="STL10N3LLH5",
    ref_prefix="Q",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR)])

# D1 — BAV199WQ-7 (BAV199WQ-7)
BAV199WQ_7 += Part(tool=SKIDL, name="BAV199WQ-7",
    ref_prefix="D",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR)])

# IC9 — INA281A5QDBVRQ1 (INA281A5QDBVRQ1)
INA281A5QDBVRQ1 += Part(tool=SKIDL, name="INA281A5QDBVRQ1",
    ref_prefix="IC",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR), Pin(num=4, name="p4", func=Pin.types.BIDIR), Pin(num=5, name="p5", func=Pin.types.BIDIR)])

# Q3 — 2N7002NXAKR (2N7002NXAKR)
part_2N7002NXAKR += Part(tool=SKIDL, name="2N7002NXAKR",
    ref_prefix="Q",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR)])

# IC8 — LTC4440AHMS8E-5#PBF (LTC4440AHMS8E)
LTC4440AHMS8E_5_PBF += Part(tool=SKIDL, name="LTC4440AHMS8E-5#PBF",
    ref_prefix="IC",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR), Pin(num=4, name="p4", func=Pin.types.BIDIR), Pin(num=5, name="p5", func=Pin.types.BIDIR), Pin(num=6, name="p6", func=Pin.types.BIDIR), Pin(num=7, name="p7", func=Pin.types.BIDIR), Pin(num=8, name="p8", func=Pin.types.BIDIR), Pin(num=9, name="p9", func=Pin.types.BIDIR)])

# IC5 — TPD4E1U06DBVR (TPD4E1U06DBVR)
TPD4E1U06DBVR += Part(tool=SKIDL, name="TPD4E1U06DBVR",
    ref_prefix="IC",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR), Pin(num=4, name="p4", func=Pin.types.BIDIR), Pin(num=5, name="p5", func=Pin.types.BIDIR), Pin(num=6, name="p6", func=Pin.types.BIDIR)])

# IC4 — STM32G431CBT6 (STM32G431CBT6)
STM32G431CBT6 += Part(tool=SKIDL, name="STM32G431CBT6",
    ref_prefix="IC",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR), Pin(num=4, name="p4", func=Pin.types.BIDIR), Pin(num=5, name="p5", func=Pin.types.BIDIR), Pin(num=6, name="p6", func=Pin.types.BIDIR), Pin(num=7, name="p7", func=Pin.types.BIDIR), Pin(num=8, name="p8", func=Pin.types.BIDIR), Pin(num=9, name="p9", func=Pin.types.BIDIR), Pin(num=10, name="p10", func=Pin.types.BIDIR), Pin(num=11, name="p11", func=Pin.types.BIDIR), Pin(num=12, name="p12", func=Pin.types.BIDIR), Pin(num=13, name="p13", func=Pin.types.BIDIR), Pin(num=14, name="p14", func=Pin.types.BIDIR), Pin(num=15, name="p15", func=Pin.types.BIDIR), Pin(num=16, name="p16", func=Pin.types.BIDIR), Pin(num=17, name="p17", func=Pin.types.BIDIR), Pin(num=18, name="p18", func=Pin.types.BIDIR), Pin(num=19, name="p19", func=Pin.types.BIDIR), Pin(num=20, name="p20", func=Pin.types.BIDIR), Pin(num=21, name="p21", func=Pin.types.BIDIR), Pin(num=22, name="p22", func=Pin.types.BIDIR), Pin(num=23, name="p23", func=Pin.types.BIDIR), Pin(num=24, name="p24", func=Pin.types.BIDIR), Pin(num=25, name="p25", func=Pin.types.BIDIR), Pin(num=26, name="p26", func=Pin.types.BIDIR), Pin(num=27, name="p27", func=Pin.types.BIDIR), Pin(num=28, name="p28", func=Pin.types.BIDIR), Pin(num=29, name="p29", func=Pin.types.BIDIR), Pin(num=30, name="p30", func=Pin.types.BIDIR), Pin(num=31, name="p31", func=Pin.types.BIDIR), Pin(num=32, name="p32", func=Pin.types.BIDIR), Pin(num=33, name="p33", func=Pin.types.BIDIR), Pin(num=34, name="p34", func=Pin.types.BIDIR), Pin(num=35, name="p35", func=Pin.types.BIDIR), Pin(num=36, name="p36", func=Pin.types.BIDIR), Pin(num=37, name="p37", func=Pin.types.BIDIR), Pin(num=38, name="p38", func=Pin.types.BIDIR), Pin(num=39, name="p39", func=Pin.types.BIDIR), Pin(num=40, name="p40", func=Pin.types.BIDIR), Pin(num=41, name="p41", func=Pin.types.BIDIR), Pin(num=42, name="p42", func=Pin.types.BIDIR), Pin(num=43, name="p43", func=Pin.types.BIDIR), Pin(num=44, name="p44", func=Pin.types.BIDIR), Pin(num=45, name="p45", func=Pin.types.BIDIR), Pin(num=46, name="p46", func=Pin.types.BIDIR), Pin(num=47, name="p47", func=Pin.types.BIDIR), Pin(num=48, name="p48", func=Pin.types.BIDIR)])

# U3 — BSC014N04LS (BSC014N04LS)
BSC014N04LS += Part(tool=SKIDL, name="BSC014N04LS",
    ref_prefix="U",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR)])

# F2 — SF-2410FP100W-2 (SF-2410FP100W-2)
SF_2410FP100W_2 += Part(tool=SKIDL, name="SF-2410FP100W-2",
    ref_prefix="F",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR)])

# J1 — USB4110-GF-A (USB4110-GF-A)
USB4110_GF_A += Part(tool=SKIDL, name="USB4110-GF-A",
    ref_prefix="J",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR), Pin(num=4, name="p4", func=Pin.types.BIDIR), Pin(num=5, name="p5", func=Pin.types.BIDIR), Pin(num=6, name="p6", func=Pin.types.BIDIR), Pin(num=7, name="p7", func=Pin.types.BIDIR), Pin(num=8, name="p8", func=Pin.types.BIDIR), Pin(num=9, name="p9", func=Pin.types.BIDIR), Pin(num=10, name="p10", func=Pin.types.BIDIR), Pin(num=11, name="p11", func=Pin.types.BIDIR), Pin(num=12, name="p12", func=Pin.types.BIDIR), Pin(num=13, name="p13", func=Pin.types.BIDIR), Pin(num=14, name="p14", func=Pin.types.BIDIR), Pin(num=15, name="p15", func=Pin.types.BIDIR), Pin(num=16, name="p16", func=Pin.types.BIDIR), Pin(num=17, name="p17", func=Pin.types.BIDIR)])

# IC6 — STUSB4500QTR (STUSB4500QTR)
STUSB4500QTR += Part(tool=SKIDL, name="STUSB4500QTR",
    ref_prefix="IC",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR), Pin(num=4, name="p4", func=Pin.types.BIDIR), Pin(num=5, name="p5", func=Pin.types.BIDIR), Pin(num=6, name="p6", func=Pin.types.BIDIR), Pin(num=7, name="p7", func=Pin.types.BIDIR), Pin(num=8, name="p8", func=Pin.types.BIDIR), Pin(num=9, name="p9", func=Pin.types.BIDIR), Pin(num=10, name="p10", func=Pin.types.BIDIR), Pin(num=11, name="p11", func=Pin.types.BIDIR), Pin(num=12, name="p12", func=Pin.types.BIDIR), Pin(num=13, name="p13", func=Pin.types.BIDIR), Pin(num=14, name="p14", func=Pin.types.BIDIR), Pin(num=15, name="p15", func=Pin.types.BIDIR), Pin(num=16, name="p16", func=Pin.types.BIDIR), Pin(num=17, name="p17", func=Pin.types.BIDIR), Pin(num=18, name="p18", func=Pin.types.BIDIR)])

# L1 — SRP7028CC-150M (SRP7028CC-150M)
SRP7028CC_150M += Part(tool=SKIDL, name="SRP7028CC-150M",
    ref_prefix="L",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR)])

# J2 — 691243110009 (691243110009)
part_691243110009 += Part(tool=SKIDL, name="691243110009",
    ref_prefix="J",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR), Pin(num=4, name="p4", func=Pin.types.BIDIR), Pin(num=5, name="p5", func=Pin.types.BIDIR), Pin(num=6, name="p6", func=Pin.types.BIDIR), Pin(num=7, name="p7", func=Pin.types.BIDIR), Pin(num=8, name="p8", func=Pin.types.BIDIR), Pin(num=9, name="p9", func=Pin.types.BIDIR)])

# FB1 — BLM18HE601SN1D (BLM18HE601SN1D)
BLM18HE601SN1D += Part(tool=SKIDL, name="BLM18HE601SN1D",
    ref_prefix="FB",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR)])

# Q1 — STL9P3LLH6 (STL9P3LLH6)
STL9P3LLH6 += Part(tool=SKIDL, name="STL9P3LLH6",
    ref_prefix="Q",
    pins=[Pin(num=1, name="p1", func=Pin.types.BIDIR), Pin(num=2, name="p2", func=Pin.types.BIDIR), Pin(num=3, name="p3", func=Pin.types.BIDIR)])


@subcircuit
def AxxSolder():

    # ─── Power Nets ───────────────────────────────────────────
    VDD  = Net("VDD")
    GND  = Net("GND")
    V3_3 = Net("+3.3V")
    V7_5 = Net("+7.5V")

    # ─── Signal Nets ──────────────────────────────────────────
    BLUE                   = Net("BLUE")
    BOOST                  = Net("BOOST")
    Buzzer                 = Net("Buzzer")
    CC1                    = Net("CC1")
    CC1_                   = Net("CC1_")
    CC2                    = Net("CC2")
    CC2_                   = Net("CC2_")
    CURRENT                = Net("CURRENT")
    EARTH                  = Net("EARTH")
    ENC_A                  = Net("ENC_A")
    ENC_B                  = Net("ENC_B")
    GREEN                  = Net("GREEN")
    H_sense1               = Net("H_sense1")
    H_sense2               = Net("H_sense2")
    Handle_inp1            = Net("Handle_inp1")
    Handle_inp2            = Net("Handle_inp2")
    Heater                 = Net("Heater")
    I_LEAK                 = Net("I_LEAK")
    NRST                   = Net("NRST")
    RED                    = Net("RED")
    S1                     = Net("S1")
    SCL                    = Net("SCL")
    SDA                    = Net("SDA")
    SD_CS                  = Net("SD_CS")
    SHUNT_                 = Net("SHUNT+")
    SHUNT_                 = Net("SHUNT-")
    SPI_CS                 = Net("SPI_CS")
    SPI_DC                 = Net("SPI_DC")
    SPI_MOSI               = Net("SPI_MOSI")
    SPI_RST                = Net("SPI_RST")
    SPI_SCK                = Net("SPI_SCK")
    SW1                    = Net("SW1")
    SW2                    = Net("SW2")
    SW3                    = Net("SW3")
    SWCLK                  = Net("SWCLK")
    SWDIO                  = Net("SWDIO")
    S_sense                = Net("S_sense")
    Stand_inp              = Net("Stand_inp")
    TC                     = Net("TC")
    USART_RX               = Net("USART_RX")
    USART_TX               = Net("USART_TX")
    USB_D_                 = Net("USB_D+")
    USB_D_                 = Net("USB_D-")
    USR1                   = Net("USR1")
    USR2                   = Net("USR2")
    USR3                   = Net("USR3")
    USR4                   = Net("USR4")
    VBUS                   = Net("VBUS")
    VBUS_IN                = Net("VBUS_IN")
    VCC                    = Net("VCC")
    VCCA                   = Net("VCCA")
    VDD_IN                 = Net("VDD_IN")
    VDD_IN_USBCPD          = Net("VDD_IN_USBCPD")
    VSS                    = Net("VSS")
    VSSA                   = Net("VSSA")
    V_bit1                 = Net("V_bit1")
    V_bit2                 = Net("V_bit2")
    V_bit3                 = Net("V_bit3")

    # ─── Components ───────────────────────────────────────────

    # --- Capacitors ---
    c21 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="100n")
    c2 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="10u")
    c14 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="100n")
    c3 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="100n")
    c18 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="100n")
    c35 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="10u")
    c30 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="10u")
    c10 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="10u")
    c17 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="100n")
    c37 = Part(EEV227M035A9MAA, "EEV227M035A9MAA", footprint="CAPAE830X1050N", value="220u")
    c25 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="100n")
    c32 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="10u")
    c9 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="100n")
    c31 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="10u")
    c26 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="100n")
    c13 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="10u")
    c11 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="10u")
    c33 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="100n")
    c7 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="10u")
    c23 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="100n")
    c22 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="100n")
    c29 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="100n")
    c34 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="10u")
    c16 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="100n")
    c19 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="10u")
    c5 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="10u")
    c20 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="10u")
    c8 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="10u")
    c15 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="100n")
    c27 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="100n")
    c24 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="100n")
    c1 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="10u")
    c4 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="1n")
    c6 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="1n")
    c28 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="100n")
    c12 = Part("Device", "C_Small", footprint="Capacitor_SMD:C_0603_1608Metric", value="10u")

    # --- Diodes ---
    d8 = Part("Device", "D_Schottky_Dual_Series_AKC", footprint="footprints:SOT95P230X110-3N", value="BAT54S")
    d6 = Part("Device", "D_Schottky_Dual_Series_AKC", footprint="footprints:SOT95P230X110-3N", value="BAT54S")
    d3 = Part(SMF4L24AT1G, "SMF4L24AT1G", footprint="footprints:SODFL3619X98N", value="SMF4L24AT1G")
    d7 = Part("Device", "D_Schottky_Dual_Series_AKC", footprint="footprints:SOT95P230X110-3N", value="BAT54S")
    d5 = Part("Device", "D_Schottky_Dual_Series_AKC", footprint="footprints:SOT95P230X110-3N", value="BAT54S")
    d10 = Part(PMEG6020ER_115, "PMEG6020ER,115", footprint="footprints:PMEG6020ER115", value="PMEG6020ER")
    d1 = Part(BAV199WQ_7, "BAV199WQ-7", footprint="footprints:SOT65P210X110-3N", value="BAV199WQ-7")
    d2 = Part(BAV199WQ_7, "BAV199WQ-7", footprint="footprints:SOT65P210X110-3N", value="BAV199WQ-7")
    d9 = Part(PMEG6020ER_115, "PMEG6020ER,115", footprint="footprints:PMEG6020ER115", value="PMEG6020ER")
    d4 = Part(SMF4L24AT1G, "SMF4L24AT1G", footprint="footprints:SODFL3619X98N", value="SMF4L24AT1G")

    # --- Fuses ---
    f2 = Part(SF_2410FP100W_2, "SF-2410FP100W-2", footprint="footprints:SF2410FP100W2", value="SF-2410FP100W-2")

    # --- Ferrite Beads ---
    fb1 = Part(BLM18HE601SN1D, "BLM18HE601SN1D", footprint="Resistor_SMD:R_0603_1608Metric", value="BLM18HE601SN1D")

    # --- Fiducials ---
    fid3 = Part("Mechanical", "Fiducial", footprint="Fiducial:Fiducial_0.75mm_Mask1.5mm", value="Fiducial")
    fid2 = Part("Mechanical", "Fiducial", footprint="Fiducial:Fiducial_0.75mm_Mask1.5mm", value="Fiducial")
    fid1 = Part("Mechanical", "Fiducial", footprint="Fiducial:Fiducial_0.75mm_Mask1.5mm", value="Fiducial")

    # --- Mounting Holes ---
    h1 = Part("Mechanical", "MountingHole", footprint="MountingHole:MountingHole_2.5mm", value="MountingHole")
    h2 = Part("Mechanical", "MountingHole", footprint="MountingHole:MountingHole_2.5mm", value="MountingHole")

    # --- Integrated Circuits ---
    ic7 = Part(MAX16171ATA_VY_T, "MAX16171ATA_VY+T", footprint="footprints:SON50P300X200X80-9N", value="MAX16171ATA_VY+T")
    ic2 = Part(OPA2387DSGT, "OPA2387DSGT", footprint="footprints:SON50P200X200X80-9N", value="OPA2387DSGT")
    ic1 = Part(TLV76733DRVR, "TLV76733DRVR", footprint="footprints:SON65P200X200X80-7N", value="TLV76733DRVR")
    ic9 = Part(INA281A5QDBVRQ1, "INA281A5QDBVRQ1", footprint="footprints:SOT95P280X145-5N", value="INA281A5QDBVRQ1")
    ic8 = Part(LTC4440AHMS8E_5_PBF, "LTC4440AHMS8E-5#PBF", footprint="footprints:SOP65P490X110-9N", value="LTC4440AHMS8E")
    ic5 = Part(TPD4E1U06DBVR, "TPD4E1U06DBVR", footprint="SOT95P280X145-6N", value="TPD4E1U06DBVR")
    ic4 = Part(STM32G431CBT6, "STM32G431CBT6", footprint="footprints:QFP50P900X900X160-48N", value="STM32G431CBT6")
    ic6 = Part(STUSB4500QTR, "STUSB4500QTR", footprint="footprints:QFN50P400X400X100-25N-D", value="STUSB4500QTR")

    # --- Connectors ---
    j7 = Part(TSW_108_07_T_S, "TSW-108-07-T-S", footprint="TSW-108-XX-YY-S", value="TSW-108-07-T-S")
    j4 = Part(part_61300611821, "61300611821", footprint="footprints:RHDR6W97P0X254_1X6_1574X250X865P", value="61300611821")
    j8 = Part("Connector", "Conn_01x01_Pin", footprint="", value="Conn_01x01_Pin")
    j1 = Part(USB4110_GF_A, "USB4110-GF-A", footprint="USB4110GFA", value="USB4110-GF-A")
    j2 = Part(part_691243110009, "691243110009", footprint="footprints:691243110009", value="691243110009")

    # --- Inductors ---
    l1 = Part(SRP7028CC_150M, "SRP7028CC-150M", footprint="footprints:INDPM7366X300N", value="SRP7028CC-150M")

    # --- Transistors / MOSFETs ---
    q2 = Part(STL10N3LLH5, "STL10N3LLH5", footprint="footprints:STL10N3LLH5", value="STL10N3LLH5")
    q3 = Part(part_2N7002NXAKR, "2N7002NXAKR", footprint="footprints:SOT95P230X110-3N", value="2N7002NXAKR")
    q1 = Part(STL9P3LLH6, "STL9P3LLH6", footprint="footprints:STL9P3LLH6", value="STL9P3LLH6")

    # --- Resistors ---
    r43 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="100")
    r2 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="360k")
    r11 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="22k")
    r37 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r7 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="360k")
    r35 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r45 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0805_2012Metric", value="100m")
    r36 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r6 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r22 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r21 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="22k")
    r14 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="1k5")
    r42 = Part(WSLP25125L000FEA, "WSLP25125L000FEA", footprint="footprints:RESC6432X89N", value="5m")
    r8 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="360k")
    r44 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0805_2012Metric", value="1M")
    r47 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="100")
    r46 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="100")
    r13 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="100")
    r16 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="100")
    r27 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r34 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="100")
    r23 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r1 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="1k5")
    r24 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="22k")
    r15 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="22k")
    r32 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r9 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="360k")
    r31 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r50 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="10")
    r10 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="220k")
    r30 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r18 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r28 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r19 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r48 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="100")
    r41 = Part("Device", "R_Small", footprint="", value="Heater 2 OHM")
    r29 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r12 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="22k")
    r26 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r33 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r4 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r3 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="220k")
    r49 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="10")
    r20 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r38 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r39 = Part("Device", "R_Small", footprint="", value="Heater")
    r25 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="4k7")
    r5 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="1k5")
    r17 = Part("Device", "R_Small", footprint="Resistor_SMD:R_0603_1608Metric", value="1k5")
    r40 = Part("Device", "R_Small", footprint="", value="Heater")

    # --- Switches ---
    s3 = Part(ADTSM644KVTR, "ADTSM644KVTR", footprint="footprints:ADTSM644RVTR", value="ADTSM644RVTR")
    s1 = Part(ADTSM644KVTR, "ADTSM644KVTR", footprint="footprints:ADTSM644RVTR", value="ADTSM644RVTR")
    s2 = Part(ADTSM644KVTR, "ADTSM644KVTR", footprint="footprints:ADTSM644RVTR", value="ADTSM644RVTR")

    # --- Thermocouples ---
    tc2 = Part("Device", "Thermocouple", footprint="", value="TC")
    tc1 = Part("Device", "Thermocouple", footprint="", value="TC")
    tc3 = Part("Device", "Thermocouple", footprint="", value="TC")

    # --- Display ---
    tft1 = Part(Adafruit_240x320_TFT, "Adafruit_240x320_TFT", footprint="footprints:Adafruit_240x320_TFT", value="~")

    # --- Test Points ---
    tp4 = Part("Connector", "TestPoint", footprint="TestPoint:TestPoint_Pad_D1.0mm", value="DIAG_TP")
    tp1 = Part("Connector", "TestPoint", footprint="TestPoint:TestPoint_Pad_D1.0mm", value="DIAG_TP")
    tp10 = Part("Connector", "TestPoint", footprint="TestPoint:TestPoint_Pad_D1.0mm", value="Current_TP")
    tp2 = Part("Connector", "TestPoint", footprint="TestPoint:TestPoint_Pad_D1.0mm", value="DIAG_TP")
    tp7 = Part("Connector", "TestPoint", footprint="TestPoint:TestPoint_Pad_D1.0mm", value="DIAG_TP")
    tp15 = Part("Connector", "TestPoint", footprint="TestPoint:TestPoint_Pad_D1.0mm", value="DIAG_TP")
    tp6 = Part("Connector", "TestPoint", footprint="TestPoint:TestPoint_Pad_D1.0mm", value="DIAG_TP")
    tp11 = Part("Connector", "TestPoint", footprint="TestPoint:TestPoint_Pad_D1.0mm", value="TC_TP")
    tp3 = Part("Connector", "TestPoint", footprint="TestPoint:TestPoint_Pad_D1.0mm", value="3.3V_TP")
    tp12 = Part("Connector", "TestPoint", footprint="TestPoint:TestPoint_Pad_D1.0mm", value="GND_TP")
    tp17 = Part("Connector", "TestPoint", footprint="TestPoint:TestPoint_Pad_D1.0mm", value="SW_TP")
    tp8 = Part("Connector", "TestPoint", footprint="TestPoint:TestPoint_Pad_D1.0mm", value="DIAG_TP")
    tp14 = Part("Connector", "TestPoint", footprint="TestPoint:TestPoint_Pad_D1.0mm", value="DIAG_TP")
    tp9 = Part("Connector", "TestPoint", footprint="TestPoint:TestPoint_Pad_D1.0mm", value="Current_TP")
    tp13 = Part("Connector", "TestPoint", footprint="footprints:TSW-101-XX-YY-S", value="DIAG_TP")
    tp5 = Part("Connector", "TestPoint", footprint="TestPoint:TestPoint_Pad_D1.0mm", value="DIAG_TP")
    tp16 = Part("Connector", "TestPoint", footprint="TestPoint:TestPoint_Pad_D1.0mm", value="DIAG_TP")

    # --- ICs / Modules ---
    u2 = Part(PEC11J_9215F_S0015, "PEC11J-9220F-S0015", footprint="footprints:PEC11J9215FS0015", value="PEC11J-9215F-S0015")
    u3 = Part(BSC014N04LS, "BSC014N04LS", footprint="footprints:BSC014N04LS", value="BSC014N04LS")


# ─── Run ─────────────────────────────────────────────────────
print("Loading components...")
AxxSolder()
print("✅ All components loaded!")
print("Generating netlist...")
generate_netlist(tool=KICAD9)
print("✅ Netlist generated successfully! Check for AxxSolder_skidl.net in the same folder.")

