# 🏙️ StadtinfoAPI

Ein Beispielprojekt zur Demonstration von CI/CD-, Automatisierungs- und Containerisierungstechniken mit Fokus auf Git, Jenkins, Docker und Ansible – entwickelt im Rahmen meiner Bewerbung bei der **Deutschen Rentenversicherung Bund**.

---

## 📌 Projektziel

Die `PersoneninfoAPI` ist eine schlanke REST-API, die Informationen zu ausgewählten Personen bereitstellt. Sie dient als Übungs- und Nachweisplattform für:

- Versionskontrolle mit **Git**
- Automatisiertes Testen und Bauen mit **Jenkins**
- Containerisierung mit **Docker**
- Infrastrukturautomatisierung mit **Ansible**
- Grundlagen der **DevOps-orientierten Softwareentwicklung**

---

## ⚙️ Technologien

| Bereich           | Tools / Technologien       |
|------------------|----------------------------|
| Programmiersprache | Python 3 / FastAPI        |
| Testing          | Pytest                     |
| Versionskontrolle| Git + GitHub               |
| CI/CD            | Jenkins (Pipeline as Code) |
| Containerisierung| Docker                     |
| Deployment       | Ansible                    |
| IDEs             | VS Code, optional IntelliJ |

---

## 🚀 API-Endpunkte

| Methode | Pfad              | Beschreibung                               |
|--------:|-------------------|--------------------------------------------|
| GET     | `/cities`         | Gibt alle verfügbaren Städtenamen zurück    |
| GET     | `/cities/berlin`  | Gibt Detailinformationen zu „Berlin“       |

Die API basiert auf einer statischen JSON-Datei und benötigt keine Datenbank.

---

## 📁 Projektstruktur (Auszug)

```text
stadtinfo-api/
├── app/
│   ├── main.py         # API-Logik
│   └── data.json       # Statische Städtedaten
├── tests/
│   └── test_api.py     # Pytest-Tests
├── requirements.txt    # Python-Abhängigkeiten
├── Dockerfile          # Containerdefinition
├── Jenkinsfile         # CI/CD-Pipeline
├── ansible/
│   ├── inventory.ini
│   └── playbook.yml    # Automatisiertes Deployment
└── README.md           # Dieses Dokument
