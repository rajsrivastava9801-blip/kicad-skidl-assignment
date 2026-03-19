# Circuit Overview – AxxSolder Soldering Iron Controller

## 1. Introduction

This document explains the circuit design of the AxxSolder soldering iron controller. The schematic is written in Python using the **SKiDL** library, which allows hardware designs to be version-controlled and described programmatically.

---

## 2. Block Diagram (Signal Flow)

```
[USB-C Connector J1]
        |
        ├── CC1 / CC2 ──► [USB-PD Controller IC6] ──► VBUS negotiation
        |
        └── VBUS ──────► [P-FET Q1] ──► VDD_IN_USBCPD
                                              |
                              ┌───────────────┘
                              |
                    [LDO IC1] ──► +3.3V ──► MCU, Logic
                              |
                    [Boost Converter IC3] ──► +7.5V ──► Heater Driver
                                                              |
                                                    [IC8 + MOSFET U3]
                                                              |
                                                         [Heater Element]

[STM32 IC4 (MCU)]
    ├── SPI  ──► Display (J7), SD Card (J8)
    ├── I2C  ──► IC6 (USB-PD)
    ├── UART ──► Debug (J4)
    ├── SWD  ──► Programmer (J4)
    ├── ADC  ──► Thermocouple (IC2), Current sense (IC9), Handle inputs
    ├── PWM  ──► Heater control, Buzzer (LS1)
    └── GPIO ──► RGB LED, Encoder (U2), Switches (SW1/SW2/SW3)
```

---

## 3. Power Subsystem

### 3.1 USB-C Input
- **J1** is a USB-C connector supporting both data (USB 2.0) and power.
- **CC1** and **CC2** lines connect to the USB-PD controller **IC6**, which negotiates the power contract (e.g., 20V/5A for fast charging profiles).
- **VBUS** carries the negotiated input voltage into the circuit.

### 3.2 Input Power Switch (Q1, Q2)
- **Q1** is a P-channel MOSFET that gates VBUS into `VDD_IN_USBCPD`.
- **IC7** drives the gate of Q2 for controlled turn-on/off.
- A fuse **F1** protects the main VDD rail.

### 3.3 3.3V LDO (IC1)
- Converts VDD down to **+3.3V** for all digital logic (MCU, sensors, display).
- Decoupled with multiple 10µF and 100nF capacitors.

### 3.4 Boost Converter (IC3)
- Converts the input voltage up to **+7.5V** to power the heater driver.
- Uses inductor **L1**, diode **D9**, and capacitors **C30/C31/C32/C33** for the switching loop.
- **FB** pin monitors the output via a resistor divider (R7, R8, R11).

---

## 4. Heater Control Subsystem

### 4.1 Heater Driver (IC8)
- Receives a PWM signal (`/Heater` net) from the STM32 MCU (IC4 pin 5).
- Drives the gate of **U3** (BSC014N04LS N-channel MOSFET) via the `TG` pin.
- The MOSFET switches the heater element on/off at high frequency.

### 4.2 Current Sensing (IC9)
- Monitors heater current through a shunt resistor.
- Output connected to `CURRENT` net → ADC input of MCU (IC4 pin 6).
- Test point **TP10** available for probing.

---

## 5. Temperature Sensing

### 5.1 Thermocouple Interface (IC2)
- **IC2** is a dual op-amp used to amplify the thermocouple signal.
- `TC` net carries the amplified temperature signal to MCU ADC (IC4 pin 11).
- The two op-amp stages (IC2A and IC2B) condition RED and GREEN (iron tip) signals respectively.
- Test point **TP11** allows direct measurement.

---

## 6. USB-C Power Delivery (IC6)

- **IC6** is a USB-C PD controller handling the full PD negotiation.
- Communicates with the MCU via **I2C** (SCL/SDA).
- Monitors CC1/CC2 for cable orientation and power role.
- Internal regulators: `VREG_1V2` and `VREG_2V7` decoupled by C12/C13.
- **VBUS_EN_SNK** and **VBUS_VS_DISCH** control VBUS switching.

---

## 7. Microcontroller (IC4 – STM32)

The STM32 MCU is the brain of the system. Key pin assignments:

| Function | Pin(s) | Net |
|---|---|---|
| Heater PWM | 5 | `/Heater` |
| Current ADC | 6 | `/CURRENT` |
| Reset | 7 | `/NRST` |
| Encoder A | 8 | `/ENC_A` |
| I_LEAK monitor | 9 | `/I_LEAK` |
| VBUS sense | 10 | `/VBUS_IN` |
| Thermocouple ADC | 11 | `/TC` |
| Handle input 1 | 12 | `/Handle_inp1` |
| Handle input 2 | 13 | `/Handle_inp2` |
| Stand input | 14 | `/Stand_inp` |
| MCU switch 2 | 15 | `/SW2` |
| USR2/3/4 | 16–18 | GPIO test pads |
| GND | 19, 23, 3, 35, 4, 47 | GND |
| VCCA | 20–21 | Analog supply |
| SD_CS | 22 | `/SD_CS` |
| SPI_CS | 28 | `/SPI_CS` |
| SPI_MOSI | 29 | `/SPI_MOSI` |
| USART_TX | 31 | `/USART_TX` |
| USART_RX | 32 | `/USART_RX` |
| USB_D− | 33 | `/USB_D-` |
| USB_D+ | 34 | `/USB_D+` |
| SWDIO | 37 | `/SWDIO` |
| SWCLK | 38 | `/SWCLK` |
| SCL | 39 | `/SCL` |
| Encoder B | 40 | `/ENC_B` |
| CC1_ | 43 | `/CC1_` |
| Buzzer | 44 | `/Buzzer` |
| SW3 | 45 | `/SW3` |
| SDA | 46 | `/SDA` |

---

## 8. User Interface

### 8.1 Rotary Encoder (U2)
- **PEC11J-9215F-S0015** encoder with built-in push button.
- ENC_A / ENC_B → MCU for rotation direction.
- Switch output → SW1 net.
- Debounced by RC filters (C28/C29, R47/R48).

### 8.2 RGB LED
- Three separate LEDs (or a single RGB) driven via:
  - **RED** net → R1, D10 (pin 1)
  - **GREEN** net → R5, F2
  - **BLUE** net → R4, D10 (pin 2)
- PWM-dimmable from MCU.

### 8.3 Buzzer (LS1)
- Driven by Q3 (NPN transistor) via R34/R37.
- Control signal from MCU pin 44 (`/Buzzer`).

### 8.4 Switches (SW1, SW2, SW3)
- Three tactile switches debounced with RC (C21/C22/C23).
- Pull-up via R30/R31/R32, with software filtering in MCU.

---

## 9. Connectivity

| Connector | Purpose |
|---|---|
| J1 (USB-C) | Power input + USB 2.0 data |
| J2 (9-pin) | Handle connector (H_sense, Stand_inp, S_sense) |
| J3 | USR4 GPIO breakout |
| J4 (SWD/UART) | Programming and debug |
| J7 (SPI Display) | OLED or TFT display |
| J8 (SD Card) | SD card via SPI |

---

## 10. Decoupling Strategy

- Every power supply pin of IC4 (STM32) is decoupled with dedicated capacitors.
- 10µF bulk caps (Murata GRM188R6YA106MA73J) placed near power entry.
- 100nF high-frequency caps (KEMET C0603C104J5RACTU) placed at each IC supply pin.
- All capacitors use the 0603 SMD footprint.
