#!/bin/bash
# Script de démarrage pour le projet Django CV

echo "=========================================="
echo "Démarrage du projet Django CV"
echo "=========================================="
echo ""

# Vérifier si l'environnement virtuel existe
if [ -d ".venv" ]; then
    echo "Activation de l'environnement virtuel..."
    source .venv/bin/activate
else
    echo "Création de l'environnement virtuel..."
    python -m venv .venv
    source .venv/bin/activate
    pip install -q -r requirements.txt
fi

echo ""
echo "=========================================="
echo "Serveur démarré sur http://localhost:8000"
echo "(Données chargées depuis initial_data.json)"
echo "=========================================="
echo ""

# Démarrer le serveur
python manage.py runserver
