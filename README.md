# Conception-et-r-alisation-d-un-syst-me-de-surveillance-environnementale
Ce projet consiste en la conception et la réalisation d’un système intelligent de surveillance environnementale basé sur Raspberry Pi. Le système utilise plusieurs capteurs (DHT22 pour la température et l’humidité, capteur de luminosité et capteur de gaz) afin de collecter des données en temps réel. 
# Objectifs Collecter des données environnementales via capteurs

-Transmettre les données via le protocole MQTT

-Visualiser les données en temps réel avec Node-RED

-Stocker les données dans InfluxDB

-Envoyer des alertes via Telegram Bot

# Technologies utilisées
 Raspberry Pi Pico W

 MicroPython

 Wi-Fi 

 MQTT 

 Node-RED

 InfluxDB

 Telegram Bot API

 Simulation : Wokwi
 
# Capteurs utilisés

 DHT22 → Température & Humidité

 LDR → Luminosité

 Capteur de gaz → Détection de gaz

# Fonctionnement
1.Le Pico W lit les données des capteurs.

2.Les valeurs sont converties en format JSON.

3.Les données sont envoyées toutes les 5 secondes via MQTT.

4.Node-RED :

-Affiche les données sur un dashboard

-Stocke les données dans InfluxDB

-Déclenche une alerte Telegram si la température dépasse 50°C

# Auteur 
Ranim Mili

