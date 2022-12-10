from random import randint
# используется для сортировки
from operator import itemgetter

class Composition:
    '''Класс Музыкальная Композиция
       
    '''
    def __init__(self,id,name,duration,comp_id):
        self.id=id
        self.name=name
        self.duration=duration
        self.comp_id=comp_id
    def get_duration(self):
        return self.duration
class Orcestra:
    
    def __init__(self,id,name) -> None:
        '''Принимает уникальный индекс орекстра,
           его название, кол-во сыгранных композиций
           
        '''
        self.id=id
        self.name=name
    def __repr__(self):
        return f'Name: {self.name}, id: {self.id}'
        

class Orcestra_to_Composition:
    '''Обеспечивает связь М:М 
       Между классами Оркестр и Композиция
    '''
    def __init__(self,Orcestra_id,Composition_id):
        self.orc_id=Orcestra_id
        self.comp_id=Composition_id
    def get_orcestra_id(self):
        return self.orc_id
    def get_id_tuple(self):
        return (self.orc_id,self.comp_id)

orcestras=[  
            Orcestra(1,"Лондонский симфонический оркестр"),
            Orcestra(2,"Московский оркестр"),
            Orcestra(3,"Белорусский классический оркестр"),
            Orcestra(4,"Токийский новый оркестр")     
         ]

composition=[
            Composition(1,'Undertale','6:20',4),
            Composition(2,'Seasons. Vivaldi','9:00',1),
            Composition(3,'Asgore','4:10',4),
            Composition(4,'Hopes and dreams','3:20',4),
            Composition(5,'Щелкунчик','20:03',2),
            Composition(6,'Гимн Белоруси','2:13',3)
]





orc_to_comp=[Orcestra_to_Composition(1,1),Orcestra_to_Composition(1,2),
Orcestra_to_Composition(3,3),Orcestra_to_Composition(3,6),Orcestra_to_Composition(2,2)
    ]
def main():
    one_to_many=[(c.name,'Длительность(мин,сек): {}'.format(c.duration),o.name)
            for o in orcestras
            for c in composition
            
            if o.id==c.comp_id]
    print("B1. Сортировка значений по названию в алфавитном порядке")
    print(*sorted(one_to_many,key=itemgetter(0)),sep='\n')
    print()
    

    
    


if __name__=='__main__':
    main()