# Software Name: Analog Clock

**Author:** Bocaletto Luca

**Website:** [www.elektronoide.it](https://www.elektronoide.it)

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

# Nome del Software: Analog Clock

**Autore:** Bocaletto Luca

**Sito Web:** [www.elektronoide.it](https://www.elektronoide.it)

## Descrizione

Il software "Analog Clock" è un'applicazione per la visualizzazione di un orologio analogico su una finestra grafica. L'orologio visualizza l'orario corrente con lancette per le ore e i minuti, oltre a tacche per i minuti e numeri per le ore.

## Caratteristiche Principali

- Visualizzazione dell'orario corrente con lancette delle ore e dei minuti.
- Tacche dei minuti e numeri delle ore per indicare l'orario in modo chiaro.
- Utilizza il modulo PySide6 per la creazione dell'interfaccia grafica.
- Supporta l'antialiasing per ottenere una visualizzazione più fluida.
- Aggiorna l'orologio ogni secondo grazie a un timer.
- Personalizzazione dei colori delle lancette delle ore e dei minuti.

## Utilizzo

L'applicazione viene avviata, e un'interfaccia grafica mostra l'orologio analogico. Le lancette delle ore e dei minuti indicano l'orario corrente, mentre le tacche dei minuti e i numeri delle ore facilitano la lettura dell'orario.

## Componenti Principali

- **AnalogClockWindow:** Questa classe rappresenta la finestra dell'orologio analogico. Gestisce il rendering dell'orologio e il timer per l'aggiornamento.
- **HOUR_HAND_POLYGON** e **MINUTE_HAND_POLYGON:** Definiscono i poligoni per le lancette delle ore e dei minuti.
- **HOUR_COLOR** e **MINUTE_COLOR:** Specificano i colori per le lancette delle ore e dei minuti.
- **BACKGROUND_COLOR:** Il colore di sfondo dell'orologio.
- **getCurrentTime():** Restituisce l'orario corrente.

## Esecuzione

L'applicazione viene eseguita tramite il blocco principale `if __name__ == "__main__"`. Inizia creando un'applicazione grafica (`QGuiApplication`), quindi crea una finestra dell'orologio (`AnalogClockWindow`) e la mostra. L'applicazione gira in un ciclo principale finché l'utente non la chiude.

Questo software è utile come esempio di come creare un'applicazione grafica semplice con PySide6 e può essere personalizzato ulteriormente per aggiungere funzionalità aggiuntive o stili grafici.
