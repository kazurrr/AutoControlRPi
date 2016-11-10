# AutoControlRPi [![Build Status](https://travis-ci.org/kazurrr/AutoControlRPi.svg?branch=master)](https://travis-ci.org/kazurrr/AutoControlRPi)

## Zależności

`sudo apt-get install bluetooth bluez-utils blueman`

`sudo apt-get install gpsd gpsd-clients python-gps`

## Pierwsze użycie

Supported commands using ISO 9141-2 protocol (Mercedes C W203):
```
  0110: Air Flow Rate (MAF)
  0111: Throttle Position
  021C: DTC OBD Standards Compliance
  ATI: ELM327 version string
  03: Get DTCs
  07: Get DTCs from the current/last driving cycle
  04: Clear DTCs and Freeze data
  011C: OBD Standards Compliance
  0204: DTC Calculated Engine Load
  0205: DTC Engine Coolant Temperature
  0201: DTC Status since DTCs cleared
  010D: Vehicle Speed
  010F: Intake Air Temp
  010C: Engine RPM
  010B: Intake Manifold Pressure
  020F: DTC Intake Air Temp
  020D: DTC Vehicle Speed
  020B: DTC Intake Manifold Pressure
  020C: DTC Engine RPM
  0105: Engine Coolant Temperature
  0104: Calculated Engine Load
  0101: Status since DTCs cleared
  0100: Supported PIDs [01-20]
  ATRV: Voltage detected by OBD-II adapter
  0211: DTC Throttle Position
  0210: DTC Air Flow Rate (MAF)
  0600: Supported MIDs [01-20]
  ```
## Car info model
* Informacje o pojeździe (marka, model, identyfikator pojazdu - VIN)
* Pozycja pojazdu
* Prędkość: 010D
* Obroty silnika: 010C
* Temperatura silnika: 0105
* Napięcie: ATRV
