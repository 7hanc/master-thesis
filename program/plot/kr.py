
############################## cap/req <-> income
import matplotlib.pyplot as plt

def plot(lro,lrf,ar,mpf):  
    plt.style.use('ggplot')
    

    plt.xlabel('$r_{k-r}$')
    #plt.ylabel('Social welfare')
    #plt.ylabel('Improvement ratio')
    plt.ylabel('The allocated resources')
    
    x = [i/1000 for i in range(600,1500,200)]
    
    plt.plot(x, lro, '*-'  ,label='LSO')
    plt.plot(x, lrf, 'D-'  ,label='LSF')
    plt.plot(x, ar ,marker='o',label='AS')
    plt.plot(x, mpf, marker='x'  ,label='MPF')
    

    #plt.legend(loc='upper right')
    plt.legend(loc='lower right')
    #plt.show()
    plt.tight_layout()
    #plt.savefig('kr.eps')
    #plt.savefig('krir.eps')
    plt.savefig('krres.eps')