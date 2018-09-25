

################ provider's number <-> income
import matplotlib.pyplot as plt

def plot(lro,lrf,ar,mpf):
    plt.style.use('ggplot')
    
    plt.xlabel('$n$')
    plt.ylabel('Social welfare')
    #plt.ylabel('Average profit of provider')
   
    x=[i for i in range(10,35,5)]
    plt.xticks(x)
    
    
    plt.plot(x, lro, '*-',  label='lro')
    plt.plot(x, lrf, marker='x',  label='lrf')
    plt.plot(x, ar, marker='o' ,label='ar')
    plt.plot(x, mpf, 'D-',label='mpf')
  
    
    plt.legend(bbox_to_anchor=(0.85, -0.15),ncol=4)
    #plt.show()
    
    plt.tight_layout()
    plt.savefig('n.eps')
    #plt.savefig('na.eps')