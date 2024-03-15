import random
import time
from django.db import models
import numpy as np
from sklearn.datasets import load_digits, load_iris

from test_systematique import falsify

# Create your models here.

class Test(models.Model):
    Dataset_Choices = (
        ('Iris', 'Iris'),
        ('Digits', 'Digits'),
    )
    
    nb_input = models.IntegerField()
    seuil_poisoning = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    falsification = models.IntegerField(default=0)
    certificat = models.IntegerField(default=0)
    inconnu = models.IntegerField(default=0)
    temps_ecoulé = models.IntegerField(blank=True, null=True)
    dataset = models.CharField(choices=Dataset_Choices, max_length=100)
    taille_dataset = models.IntegerField(blank=True, null=True)
    
    def analyser_robustesse(self):
        
        start_time = time.time()
        
        if self.dataset == 'Iris':
            X, y = load_iris(return_X_y=True)

            # Créer une liste de paires (x, y) à partir de X et y
            data = list(zip(X, y))
        elif self.dataset == 'Digits':
            X, y = load_digits(return_X_y=True)

            # Créer une liste de paires (x, y) à partir de X et y
            data = list(zip(X, y))
        
        self.taille_dataset = len(data)
        
        # Prendre nb_input éléments aléatoirement dans data
        data_input = []
        i = 0
        while i < self.nb_input:
            index = np.random.randint(0, len(data))
            data_input.append(data[index])
            data.pop(index)
            i += 1
        
        for element in data_input:
            result = falsify.main(data[:10], self.seuil_poisoning, element[0])
            if result == 'Falsified':
                self.falsification += 1
            elif result == 'Certified':
                self.certificat += 1
            else:
                self.inconnu += 1
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.temps_ecoulé = elapsed_time
        
        self.save()