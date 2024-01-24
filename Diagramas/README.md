# Diagramas

En este documento encontrarás los diagramas del proyecto.

## Conexión general
Este diagrama esta hecho en Mermaid para MarkDown.
```mermaid
graph TD;
    Tx2[Transmisor FM] --> |BNC| Tx1[Antena]
    Rp[Raspberry Pi] --> |Jack 3.5mm| Tx2
    Bt[Batería] --> |USB| Rp
    Mg[Brújula Digital] --> |I2C| Rp;

    Bt --> |USB-C| Tx2;

    R1[Radio 1] --> |FM| Tx1
    R2[Radio 2] --> |FM| Tx1
    R3[Radio 3] --> |FM| Tx1
    R4[Radio 4] --> |FM| Tx1;
```