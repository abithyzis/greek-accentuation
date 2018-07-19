#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from ellinopoula.greek_accentuation.greek_accentuation.syllabify import syllabify


class TestSyllabify(TestCase):

    # Ένα σύμφωνο ανάμεσα σε δύο φωνήεντα συλλαβίζεται με το δεύτερο φωνήεν.
    def test_rule_1(self):
        words = ["έ-να", "ό-λα", "έ-χω"]
        for word in words:
            self.assertEquals(word.split("-"), syllabify(word.replace("-", "")))

    # Στις λέξεις που αρχίζουν από σύμφωνο και ακολουθεί φωνήεν και πάλι σύμφωνο και πάλι φωνήεν,
    # οι συλλαβές είναι ζευγάρια, σύμφωνο φωνήεν
    def test_rule_2(self):
        words = ["μά-τι", "κυ-νη-γώ"]
        for word in words:
            self.assertEquals(word.split("-"), syllabify(word.replace("-", "")))

    # Δύο σύμφωνα ανάμεσα σε δύο φωνήεντα συλλαβίζονται με το δεύτερο φωνήεν μόνο όταν αρχίζει από αυτά ελληνική λέξη.
    def test_rule_3(self):
        words = ["έ-τρε-χε", "νυ-χτε-ρί-δα", "κα-λα-μπό-κι", "μπρο-κο-λο", "μαΐ-ντα-νός", "α-τμός"]
        for word in words:
            self.assertEquals(word.split("-"), syllabify(word.replace("-", "")))

    # Διαφορετικά χωρίζονται: το πρώτο πάει με το φωνήεν που προηγείται και το δεύτερο με το φωνήεν που ακολουθεί.
    def test_rule_3a(self):
        words = ["καρ-διά", "έρ-χο-μαι"]
        for word in words:
            self.assertEquals(word.split("-"), syllabify(word.replace("-", "")))

    # Τρία ή περισσότερα σύμφωνα ανάμεσα σε δύο φωνήεντα συλλαβίζονται με το ακόλουθο φωνήεν
    # μόνο όταν αρχίζει ελληνική λέξη με τουλάχιστον τα δύο πρώτα από αυτά.
    def test_rule_4(self):
        words = ["ε-χθρι-κό", "α-στρά-φτω", "σφυ-ρί-χτρα"]
        for word in words:
            self.assertEquals(word.split("-"), syllabify(word.replace("-", "")))

    # Διαφορετικά χωρίζονται: το πρώτο πάει με το φωνήεν που προηγείται και τα υπόλοιπα με το φωνήεν που ακολουθεί.
    def test_rule_4a(self):
        words = ["άν-θρω-πος"]
        for word in words:
            self.assertEquals(word.split("-"), syllabify(word.replace("-", "")))

    # Τα όμοια σύμφωνα χωρίζονται, δηλαδή το πρώτο πάει με το φωνήεν που προηγείται
    # και το δεύτερο με το φωνήεν που ακολουθεί.
    def test_rule_7(self):
        words = ["άλ-λος", "πολ-λά"]
        for word in words:
            self.assertEquals(word.split("-"), syllabify(word.replace("-", "")))

    # Τα δίψηφα σύμφωνα δε χωρίζονται.
    def test_rule_9(self):
        words = ["πέ-ντε", "μπα-μπάς"]
        for word in words:
            self.assertEquals(word.split("-"), syllabify(word.replace("-", "")))

    # Τα δίψηφα φωνήεντα, οι δίφθογγοι και οι συνδυασμοί αυ και ευ δε χωρίζονται.
    def test_rule_10(self):
        words = ["αί-θου-σα", "αη-δό-νι", "λευ-κός", "πη-γαί-νω", "ου-ρα-νός", "γάι-δα-ρος", "ναύ-της", "ά-γιος",
                 "κα-μπά-να", "κα-ντή-λι", "α-γκι-να-ρα", "κα-τσί-κα", "γυα-λί", "ευ-χή"]
        for word in words:
            self.assertEquals(word.split("-"), syllabify(word.replace("-", "")))
