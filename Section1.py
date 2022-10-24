#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install pyopenms')


# In[2]:


import pyopenms


# In[3]:


print("AvogadroNumber: ",pyopenms.Constants.AVOGADRO)


# In[4]:


from pyopenms import *


# In[5]:


edb= ElementDB()


# In[18]:


kelement=edb.hasElement("K")
kelement=edb.getElement("K")
print(kelement.getName())
print(kelement.getSymbol())
print(kelement.getMonoWeight())
print(kelement.getAverageWeight())
print ("One mole of oxygen weighs", 2*kelement.getAverageWeight(), "grams")

print("******************************")
isotopes = kelement.getIsotopeDistribution()
for i in isotopes:
    print(i.getMZ())
    print(i.getIntensity())


# In[24]:


isotopes = edb.getElement("N").getIsotopeDistribution().getContainer()
nitrogen_isotope_difference = isotopes[1].getMZ() - isotopes[0].getMZ()
print(nitrogen_isotope_difference)


# In[29]:


magox=EmpiricalFormula("MgO")
print(magox.getElementalComposition())


# In[37]:


pro = ResidueDB().getResidue("Proline")
print(pro.getName())
print(pro.getThreeLetterCode())
print(pro.getOneLetterCode())
print(pro.getPka())
print(pro.getFormula().toString())


# In[43]:


ox = ModificationsDB().getModification("Oxidation")
print(ox.getUniModAccession())
print(ox.getUniModRecordId())
print(ox.getDiffMonoMass())
print(ox.getId())
print(ox.getFullId())
print(ox.getFullName())
print(ox.getDiffFormula())


# In[44]:


uridine = RibonucleotideDB().getRibonucleotide(b"U")

#########  Name

print(uridine.getName())

############
print(uridine.getCode())

###########
print(uridine.getAvgMass())

###############
print(uridine.getMonoMass())

################

print(uridine.getFormula().toString())

##############33
print(uridine.isModified())

#################3
methyladenosine = RibonucleotideDB().getRibonucleotide(b"m1A")

##################33

print(methyladenosine.getName())

############################
print(methyladenosine.isModified())


# In[ ]:




