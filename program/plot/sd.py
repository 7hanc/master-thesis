

################ SD <-> utility
import matplotlib.pyplot as plt

def plot(lro,lrf,ar,mpf):
    plt.style.use('ggplot')
  
    plt.xlabel('$\sigma_k$')
    #plt.ylabel('Social welfare')
    plt.ylabel('Improvement ratio')
    
    x=[i for i in range(10,510,100)] #標準差
   
    plt.xticks(x)
    
    plt.plot(x, lro, '*-',  label='LSO')
    plt.plot(x, lrf, marker='x',  label='LSF')
    plt.plot(x, ar, marker='o' ,label='AS')
    plt.plot(x, mpf, 'D-',label='MPF')
  
    
    #plt.legend(loc='lower left')
    plt.legend(loc='upper left')
    #plt.show()
    
    plt.tight_layout()
    #plt.savefig('sd.eps')
    plt.savefig('sdir.eps')