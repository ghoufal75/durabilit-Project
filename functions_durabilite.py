#Variable static a intégrer dans la class
normes={"Eco":[400,500,1000,700],"Env": [900,600,700,40],"Soc":[68,60,50,50]}

#Calcule des indicateurs
def calculIndice(self,vb,composante):
    norme_comp=[]
    indices=[]
    if composante=='ec':
        norme_comp=self.normes['Eco']
    elif composante=='en':
        norme_comp=self.normes['Env']
    elif composante=='so':
        norme_comp=self.normes['Soc']
     
    for i in range(0,len(vb)):
        indices.append(vb[i]/norme_comp[i])
    return indices

def calculeValeur(self,ind,fact):
    val=[]
    for i in range(0,len(ind)):
        val.append(round((ind/fact),2))
    return val


def durabilite(self,valeur,seuil):
    vals=0
    seuils=0
    durabilite=0
    d=0
    for i in range(0,len(valeur)):
        vals+=valeur[i]
        seuils+=seuil[i]
    val_moy=vals/4
    sum_seuils=seuils/4
    if val_moy>sum_seuils:
        durabilite=1

    return {"valeur_moyenne" : val_moy,"somme_seuils":sum_seuils,"durabilité" : durabilite}





#End of Functions
