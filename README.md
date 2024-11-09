# PocoDeFernet :beers:

## Descripción :page_with_curl:
El script `PocoDeFernet.py` está diseñado para explotar una vulnerabilidad conocida que involucra la manipulación de archivos PDF con código PHP incrustado. Este tipo de vulnerabilidad permite la ejecución de código arbitrario en un servidor web configurado para procesar PHP dentro de archivos PDF.

## Objetivo :dart:
El objetivo principal de `PocoDeFernet.py` es establecer un entorno de prueba para replicar y explotar esta vulnerabilidad, permitiendo a los investigadores de seguridad y entusiastas de la ciberseguridad comprender mejor cómo se puede comprometer un sistema utilizando archivos PDF maliciosos.

## Funcionamiento :gear:
El script realiza las siguientes acciones:
1. Instala Apache2 si no está ya instalado.
2. Configura Apache para procesar archivos PDF como si fueran scripts PHP.
3. Escribe código PHP en un archivo PDF, que cuando se accede, permite la ejecución de comandos del sistema.
4. Reinicia el servicio de Apache para aplicar los cambios.
5. Muestra la dirección IP local del servidor donde se aloja el archivo PDF, facilitando el acceso al archivo malicioso desde otra máquina.

## Instrucciones de Uso :clipboard:
Para ejecutar el script correctamente, debes tener privilegios de superusuario. Ejecuta el script con el siguiente comando:
```bash
sudo python3 PocoDeFernet.py
```

Autor :man_technologist: https://www.tiktok.com/@unhackerencapital


Este README explica de manera clara y detallada el propósito del script, cómo funciona, instrucciones para su uso, y el entorno en el que ha sido testeado. Además, incluye un llamado a la responsabilidad sobre su uso, y enlaza con la cuenta de TikTok para más información y seguimiento del autor.
