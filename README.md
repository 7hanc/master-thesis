# Master-Thesis

## Introduction
> Edge computing (EC)
* Nowadays, many applications need low response time.
  * Time-critical applications (ex. AR/VR)
  * Internet-of-Things (IoT) applications
* Edge computing (EC) is an emerging network architecture that brings traditional cloud services to the edge of network.
* The main goal of the Edge Computing is to process data quickly, reduce response time and backhaul traffic load.
> Need for Federation 
* Edge servers is limited by volume and environment constraints. 
* As the user's demands increased and an individual edge provider cannot process the task by itself.
* Edge providers can share their resources by forming federation so the user's demands can be satisfied.
* Different combinations of federation have different profit.
* Not all combinations of federation have ability to earn more profit.
* Goal of Federation: According to the profit of federation, we can determine which servers suitable for forming federation and which are not suitable. 
> Problem decomposition 
* Federation problem consists of three sub-problems. 
  * How to efficiently examine possible federation results.
  * How to maximize the profit and satisfy the demand of EC users by allocating their tasks to EC servers. 
  * How to distribute the profit of the federation to all participants that no participant has the incentive to leave the federation.
> Problem setting 
* We consider pay-per-use payments for users and heterogeneous service costs for EC servers. 
* We consider three types of resource requests. 
  * local-service-only, local-service-first and any-service
* We consider two types of EC service policies.
  * local-request-first and maximal-profit-first
* We proposed EC server federation formation mechanism to maximize the profit in each federation and ensure stable federation. 
> System architecture
<img src="https://i.imgur.com/0jFnTtG.png" width=50% height=50% /> 

## Related work
<img src="https://i.imgur.com/YvMVUUT.png" width=50% height=50% /> 

## The proposed approach
> Different types of users and providers
<img src="https://i.imgur.com/P3VAcbB.png" width=50% height=50% /> 
<img src="https://i.imgur.com/HrWWu0T.png" width=50% height=50% /> 

> We formulate a characteristic function as a integer programming problem.
* Subject to four constraints

> Merge and split mechanism   
<img src="https://i.imgur.com/0bydOi3.png" width=20% height=20% /> **Merge:**<img src="https://i.imgur.com/JEC7zUf.png" width=30% height=30% /> **Split:**<img src="https://i.imgur.com/QAstKos.png" width=30% height=30% />

**In merge: (Check if merge happen)**   
<img src="https://i.imgur.com/Iln7V95.png" width=50% height=50% /> 

## Experimental results
> Simulation settings
* Each configuration was simulated for 50 times and the result belonging to the same configuration is averaged.
* We use python’s library called PuLP to solve integer programming problem.
* We use normal distribution to generate four parameters.
  * resource's capacity of provider
  * resource's cost of provider
  * resource's request from user
  * resource's price of user
> Performance metrics 
* Compared with:
  * Local service only (LSO)
  * Local service first (LSF)
  * Any service (AS)
  * Maximum profit first (MPF)
* Performance metrics 
  * Social welfare
    * Total profit of coalition structure
  * The amount of allocated resources 



## Conclusions 
* We proposed EC server federation formation mechanism to maximize the profit in each federation and ensure stable federation. 
* We consider pay-per-use payments for users and heterogeneous service costs for EC servers and support users propose locality requests.
* Our simulation results show that, in most of the federation settings
  * MPF strategy can earn more profit than other strategies.
  * MPF strategy may serve less resource's request than LSF strategy.
