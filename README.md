# ⚡ AxxSolder – Soldering Iron Controller

A KiCad schematic designed with **SKiDL (Schematic Entry with Python)** for a feature-rich, USB-C powered soldering iron controller built around an STM32 microcontroller.

---

## 📋 Project Overview

This project defines the full schematic netlist of a soldering iron controller in Python using SKiDL. The design includes power management via USB-C PD, temperature sensing, a boost converter for the heater, an RGB status LED, a rotary encoder for control, and a buzzer for feedback — all managed by an STM32 MCU.

---

## 🔁 How This File Was Created – Back-Tracing from KiCad

The `top.py` SKiDL file in this repository was **not written by hand**. It was reverse-engineered (back-traced) from an existing KiCad schematic file (`AxxSolder.kicad_sch`) using SKiDL's built-in conversion feature.

### What is back-tracing?

Back-tracing means taking an existing schematic design (already drawn in KiCad) and converting it into a Python-based SKiDL script. This allows the design to be:
- Version-controlled with Git
- Modified programmatically using Python
- Reused as a subcircuit in a larger design

### Steps I followed

**Step 1 — Export the netlist from KiCad**

Opened the schematic `AxxSolder.kicad_sch` in KiCad and exported a netlist file:
- In KiCad: `File → Export → Netlist`
- Saved as `my_design.net`

**Step 2 — Convert the netlist to SKiDL using the terminal**

Ran the following command in the terminal:

```bash
netlist_to_skidl -i my_design.net -o my_design -w
```

| Flag | Meaning |
|---|---|
| `-i my_design.net` | Input: the KiCad netlist file |
| `-o my_design` | Output: folder name for the generated SKiDL script |
| `-w` | Overwrite output if it already exists |

**Step 3 — Output**

This generated a `top.py` (also called `main.py`) inside the output folder. This is the SKiDL Python script that defines all components, nets, and connections — which is exactly the file you see in this repository.

**Step 4 — Run the script to regenerate the netlist**

```bash
python top.py
```

This regenerates `top.net` on the Desktop, which can be imported back into KiCad.

> **Note:** This back-tracing feature only works with KiCad designs. Other ECAD tools are not supported by `netlist_to_skidl`.

---


## 🧩 Key Subsystems

| Subsystem | Key Components | Description |
|---|---|---|
| **Microcontroller** | IC4 (STM32, 48-pin) | Main controller: SPI, I2C, UART, SWD, USB |
| **USB-C Power Delivery** | IC6, J1 (USB-C) | Negotiates input power via CC1/CC2 lines |
| **Boost Converter** | IC3, L1, D9 | Steps up voltage for the heater element |
| **Heater Driver** | IC8, U3 (BSC014N04LS MOSFET) | PWM-controlled heater switching |
| **Temperature Sensing** | IC2 (op-amp), Thermocouple (TC net) | Reads tip temperature via thermocouple |
| **RGB Status LED** | D10, R1/R4/R5 | Visual feedback (RED/GREEN/BLUE nets) |
| **Rotary Encoder** | U2 (PEC11J-9215F-S0015) | User input for temperature control |
| **Buzzer** | LS1, Q3 | Audio feedback |
| **LDO Regulator** | IC1 | 3.3V power rail for logic |
| **Current Sensing** | IC9, R49 | Monitors heater current |
| **Handles / Stand** | J2 (9-pin connector) | Detects iron stand and handle inputs |
| **SD Card** | J8 | SPI-based SD card interface |
| **Display (SPI)** | J7 | SPI display (MOSI, SCK, CS, DC, RST) |
| **Debug Interface** | J4, SWCLK, SWDIO | SWD programming and UART debug |

---

## ⚡ Power Rails

| Net | Voltage | Purpose |
|---|---|---|
| `VBUS` | ~5V | USB input bus |
| `+7.5V` | 7.5V | Boosted rail for heater |
| `+3.3V` | 3.3V | MCU and logic power |
| `VDD` | — | Internal MCU VDD |
| `VCCA` | — | Analog supply for MCU |
| `GND` | 0V | Common ground |
| `Earth` | — | Chassis/earth ground |

---

## 🔌 Key Interfaces

| Interface | Nets | Connector |
|---|---|---|
| USB-C (Power + Data) | USB_D+, USB_D−, CC1, CC2, VBUS | J1 |
| SPI Display | SPI_MOSI, SPI_SCK, SPI_CS, SPI_DC, SPI_RST | J7 |
| SD Card | SD_CS + SPI bus | J8 |
| I2C | SCL, SDA | IC4 ↔ IC6 |
| UART | USART_TX, USART_RX | J4 |
| SWD Debug | SWCLK, SWDIO, NRST | J4 |
| Handle/Sensor | H_sense1, H_sense2, S_sense, Stand_inp | J2 |

---

## 🛠️ How to Generate the Netlist

### Requirements
- Python 3.8+
- SKiDL library

### Install SKiDL
```bash
pip install skidl
```

### Run the script
```bash
python top.py
```

This will generate `top.net` on your Desktop (KiCad-compatible netlist).

---

## 🧪 Test Points

The design includes dedicated test points for debugging:

| Test Point | Signal |
|---|---|
| TP1 | CC1_ (USB-PD) |
| TP2 | CC2_ (USB-PD) |
| TP3 | +3.3V |
| TP7 | CC1 |
| TP8 | CC2 |
| TP9 | Current (I_LEAK) |
| TP10 | CURRENT sense |
| TP11 | Thermocouple (TC) |
| TP12 | GND |
| TP13 | USART_RX |
| TP14 | USR4 |
| TP15 | SCL |
| TP16 | SDA |
| TP17 | Heater |

---

## 📦 Bill of Materials (Summary)

| Category | Count | Examples |
|---|---|---|
| Capacitors (10µF) | 14 | Murata GRM188R6YA106MA73J |
| Capacitors (100nF) | 8 | KEMET C0603C104J5RACTU |
| Resistors | 50+ | Various values |
| ICs | 9 | STM32, USB-PD, Boost, Op-Amp |
| MOSFETs | 3 | BSC014N04LS, Q1, Q2, Q3 |
| Diodes | 10 | D1–D10 |
| Connectors | 8 | USB-C, JST, SWD |
| Inductors | 1 | L1 (Boost converter) |
| Test Points | 17 | TP1–TP17 |

---

## 📄 License

This project is for educational/assignment purposes.

---

## 🙏 Acknowledgements

- Schematic design expressed using [SKiDL](https://github.com/devbisme/skidl)
- Original schematic source: `AxxSolder.kicad_sch`
