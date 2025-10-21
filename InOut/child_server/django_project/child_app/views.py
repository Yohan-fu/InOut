from rest_framework import viewsets
from .models import Visitor
from .serializers import VisitorSerializer
import requests
import os

MASTER_API_URL = os.getenv("MASTER_API_URL", None)
# MASTER_API_URL doit terminer par / (ex: http://master_server:8000/api/)

class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all().order_by("-entry_time")
    serializer_class = VisitorSerializer

    def perform_create(self, serializer):
        # sauvegarde locale
        instance = serializer.save()
        data = VisitorSerializer(instance).data
        # tentative d'envoi au maître
        if MASTER_API_URL:
            try:
                # post vers MASTER_API_URL + "visitors/"
                url = MASTER_API_URL.rstrip("/") + "/visitors/"
                resp = requests.post(url, json=data, timeout=5)
                if resp.status_code in (200, 201):
                    # optionnel: marquer comme "pushed" si tu as un champ
                    print("✅ transféré au maître")
                else:
                    print("⚠️ réponse inattendue du maître:", resp.status_code)
            except Exception as e:
                print("⚠️ impossible de joindre le maître, données conservées localement.", e)
