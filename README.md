# Analog Clock

**Author:** Bocaletto Luca

**Language:** Python

## Description

The software "Analog Clock" is an application for displaying an analog clock on a graphical window. The clock shows the current time with hour and minute hands, as well as minute markers and hour numbers.

![Screenshot 2023-10-14 175010](https://github.com/elektronoide/Analog-Clock/assets/134635227/ce0cfdaf-60ab-434f-98ac-2493b73da219)

## Key Features

- Display of the current time with hour and minute hands.
- Minute markers and hour numbers for clear time indication.
- Utilizes the PySide6 module for creating the graphical interface.
- Supports antialiasing for smoother rendering.
- Updates the clock every second using a timer.
- Customization of colors for the hour and minute hands.

## Usage

The application is launched, and a graphical interface displays the analog clock. The hour and minute hands indicate the current time, while minute markers and hour numbers make it easy to read the time.

## Main Components

- **AnalogClockWindow:** This class represents the window for the analog clock. It manages the rendering of the clock and the update timer.
- **HOUR_HAND_POLYGON** and **MINUTE_HAND_POLYGON:** Define the polygons for the hour and minute hands.
- **HOUR_COLOR** and **MINUTE_COLOR:** Specify the colors for the hour and minute hands.
- **BACKGROUND_COLOR:** The background color of the clock.
- **getCurrentTime():** Returns the current time.

## Execution

The application is executed through the main block `if __name__ == "__main__."` It begins by creating a graphical application (`QGuiApplication`), then creates a clock window (`AnalogClockWindow`) and displays it. The application runs in a main loop until the user closes it.

This software serves as an example of creating a simple graphical application with PySide6 and can be further customized to add additional features or graphic styles.

---

**Note**: Ensure that you have installed all the necessary dependencies before running the application.

**Maintainer Update**

My current GitHub account is **@bocaletto-luca**, which is now the official maintainer of all projects previously published under the **@Elektronoide** account. Please direct any issues, pull requests, or stars to **@bocaletto-luca** for future updates.

---
