from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from HomePage.models import PDF
from unittest.mock import patch
import unittest
import tempfile
import shutil
import os

# Para correr las pruebas usar: python manage.py test > tests/resultados.txt 2>&1

MEDIA_ROOT = tempfile.mkdtemp()
MEDIA_PDFS = os.path.join(MEDIA_ROOT, "pdfs")
os.makedirs(MEDIA_PDFS, exist_ok=True)
@override_settings(MEDIA_ROOT=MEDIA_ROOT)

class HomePageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        pdf_content = b"Test PDF content"
        cls.pdf_file = SimpleUploadedFile(
            name="pdfs/test.pdf", 
            content=pdf_content,
            content_type="application/pdf"
        )
        cls.pdf = PDF.objects.create(
            title="Test PDF",
            file=cls.pdf_file
        )
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()
    
    def test_download_existing_pdf(self):
        response = self.client.get(reverse("download_pdf", args=[self.pdf.id]))
        self.assertEqual(response.status_code, 200)
    
    def test_descarga_pdf_no_existente(self):
        response = self.client.get(reverse("download_pdf", args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_view_pdf(self):
        response = self.client.get(
            reverse("view_pdf", args=[self.pdf.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/pdf")

if __name__ == '__main__':
    unittest.main()