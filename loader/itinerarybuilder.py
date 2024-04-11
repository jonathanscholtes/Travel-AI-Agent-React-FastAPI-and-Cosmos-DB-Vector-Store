
import random

class ItineraryBuilder():
    def __init__(self,ships,destinations):
        self.ships = ships
        self.destinations = destinations
        self.ports = ['PORT CANAVERAL, FLORIDA','Fort Lauderdale, Florida','Miami, Florida']
        self.days = [5,6,7]
        self.rooms=[{'name':'Inside View','multiplier':.8},{'name':'Outside View','multiplier':.9},{'name':'Balcony','multiplier':1},{'name':'Suite','multiplier':1.2}]

    def build(self,count:int):
        itinerary = []
        for i in range(0,count):
            d = random.choice(self.days)
            prt = random.choice(self.ports)
            sp = random.choice(self.ships)
            dest = [x['name'] for x in random.choices(self.destinations,k=int(d-4))]
            price = random.randrange(900,1500)
            it = [{'Day':1,'type':'port', 'location':prt}]
            cnt = 2
            for e in dest:
                it.append({'Day':cnt,'type':'sea','location':'Cruise'})
                it.append({'Day':cnt+1,'type':'destination','location':e})    
                cnt+=2            
            it.append({'Day':cnt,'type':'sea','location':'Cruise'})
            it.append({'Day':cnt+1,'type':'port','location':prt})
            
            rms = []
            for r in self.rooms:
                rms.append({'name':r['name'],'price':round(r['multiplier']*price,2)})

            

            itinerary.append({'name':f'{d} Day Caribbean Sea',
                              'ship':{'shipid':sp['shipid'],'description':sp['description']},
                              'prices':rms,
                              'itinerary':it})
            

            
        return itinerary