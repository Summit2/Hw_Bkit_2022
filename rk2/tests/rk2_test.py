import pytest
from main import Orcestra,Composition,Orcestra_to_Composition

def test_Composition():
    obj=Composition(1,'Asgore',"2:40",23)
    assert obj.get_duration()=='2:40'
def test_Orc():
    name='Tokyo new orcestra'
    
    obj=Orcestra(1,name)
    assert obj.__repr__()==f'Name: {name}, id: {1}'


def test_Orc_to_Comp():
    obj=Orcestra_to_Composition(1,42)
    assert obj.get_id_tuple()==(1,42)


