
############################## cost/price <-> utility
import matplotlib.pyplot as plt

def plot(lro,lrf,ar,mpf):  
    plt.style.use('ggplot')
    

    plt.xlabel('$r_{c-p}$')
    #plt.ylabel('Social welfare')
    #plt.ylabel('Improvement ratio')
    plt.ylabel('The allocated resources')
    
    
    x = [i/1000 for i in range(600,1500,200)]
   
    plt.plot(x, lro, '*-' ,  label='LSO')
    plt.plot(x, lrf, 'D-' ,  label='LSF')
    plt.plot(x, ar, marker='o' ,  label='AS')
    plt.plot(x, mpf, marker='x' ,  label='MPF')
    
    #plt.legend(loc='upper left')
    plt.legend(loc='lower left')
    #plt.show()
    
    plt.tight_layout()
    #plt.savefig('cp.eps')
    #plt.savefig('cpir.eps')
    plt.savefig('cpres.eps')