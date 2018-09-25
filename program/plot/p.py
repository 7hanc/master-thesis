

################ locality <-> utility
import matplotlib.pyplot as plt

def plot(lro,lrf,ar,mpf):
    plt.style.use('ggplot')
    
    #k=Each node is connected to k nearest neighbors in ring topology
    #p=The probability of rewiring each edge
    plt.xlabel('$p$')  
    #plt.ylabel('Improvement ratio')
    plt.ylabel('Social welfare')
    
    #x = [i/10 for i in range(0,11,2)]
    x = [i/100 for i in range(0,21,4)]
    
    plt.plot(x, lro, '*-',  label='LSO')
    plt.plot(x, lrf, marker='x',  label='LSF')
    plt.plot(x, ar, marker='o' ,label='AS')
    plt.plot(x, mpf, 'D-',label='MPF')
  
    
    #plt.legend(loc='upper left')
    plt.legend(bbox_to_anchor=(0.9, -0.15),ncol=4)
    #plt.show()
    
    plt.tight_layout()
    plt.savefig('lows.eps')