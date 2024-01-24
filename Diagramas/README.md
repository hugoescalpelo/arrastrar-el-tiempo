# Diagramas

En este documento encontrarás los diagramas del proyecto.

## Conexión general
Este diagrama esta hecho en Mermaid para MarkDown.
```mermaid
graph TD;
    Tx1[Antenna] --> Tx2[Transmisor FM]
    Tx2 --> Rp[Raspberry Pi]
    Rp --> Bt[Bateria]

    Mg[Brujula Digital] --> Rp;

    Tx2 --> Bt;
```